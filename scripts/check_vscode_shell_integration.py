#!/usr/bin/env python3
"""
Diagnose VS Code terminal shell integration for zsh.

Prints PASS/WARN/FAIL checks for:
- VS Code terminal detection
- VSCODE_SHELL_INTEGRATION environment variable
- VS Code CLI availability (code / code-insiders)
- Shell integration path discovery via CLI
- PATH hygiene for common user bin directories
- rc integration hints for the selected shell (zsh or bash)

Exit code:
- 0: Likely healthy (integration detected or resolvable)
- 1: Issues detected that likely prevent integration in VS Code

Usage:
  python3 scripts/check_vscode_shell_integration.py [--shell zsh|bash] [--json]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional, Dict, Any


@dataclass
class CheckResult:
    label: str
    status: str  # PASS | WARN | FAIL
    details: str = ""


@dataclass
class Diagnostics:
    shell: str
    term_program: str
    vscode_shell_integration_env: Optional[str]
    vscode_shell_integration_env_exists: Optional[bool]
    code_cli: Optional[str]
    code_cli_path: Optional[str]
    integration_path_from_cli: Optional[str]
    path_contains_usr_local_bin: bool
    path_contains_local_bin: bool
    rc_repo_has_integration: Optional[bool]
    rc_home_has_integration: Optional[bool]


def which_first(*candidates: str) -> Optional[str]:
    for c in candidates:
        p = shutil.which(c)
        if p:
            return p
    return None


def locate_integration_with_cli(cli: str, shell: str) -> Optional[str]:
    try:
        out = subprocess.run(
            [cli, "--locate-shell-integration-path", shell],
            check=False,
            capture_output=True,
            text=True,
            timeout=3,
        )
        path = out.stdout.strip()
        if path and Path(path).is_file():
            return path
    except Exception:
        return None
    return None


def probe(shell: str) -> Diagnostics:
    env = os.environ
    term_program = env.get("TERM_PROGRAM", "")
    vsi_env = env.get("VSCODE_SHELL_INTEGRATION")
    vsi_env_exists = None
    if vsi_env:
        vsi_env_exists = Path(vsi_env).is_file()

    code_cli_path = which_first("code-insiders", "code")
    code_cli = None
    if code_cli_path:
        # Return the executable name as used (not full path) for clarity
        code_cli = Path(code_cli_path).name

    integration_path = locate_integration_with_cli(code_cli, shell) if code_cli else None

    path_contains_usr_local = "/usr/local/bin" in os.environ.get("PATH", "")
    path_contains_localbin = str(Path.home() / ".local/bin") in os.environ.get("PATH", "")

    # Check for integration patterns in zshrc files
    rc_name = "zshrc" if shell == "zsh" else "bashrc" if shell == "bash" else None
    repo_rc = Path.cwd() / rc_name if rc_name else None
    home_rc = Path.home() / f".{rc_name}" if rc_name else None
    patterns = (
        "VSCODE_SHELL_INTEGRATION",
        f"--locate-shell-integration-path {shell}",
    )

    def file_has_patterns(p: Path) -> Optional[bool]:
        if not p.is_file():
            return None
        try:
            text = p.read_text(errors="ignore")
            return any(s in text for s in patterns)
        except Exception:
            return None

    rc_repo_has = file_has_patterns(repo_rc) if repo_rc else None
    rc_home_has = file_has_patterns(home_rc) if home_rc else None

    return Diagnostics(
        shell=shell,
        term_program=term_program,
        vscode_shell_integration_env=vsi_env,
        vscode_shell_integration_env_exists=vsi_env_exists,
        code_cli=code_cli,
        code_cli_path=code_cli_path,
        integration_path_from_cli=integration_path,
        path_contains_usr_local_bin=path_contains_usr_local,
        path_contains_local_bin=path_contains_localbin,
        rc_repo_has_integration=rc_repo_has,
        rc_home_has_integration=rc_home_has,
    )


def evaluate(diag: Diagnostics) -> Dict[str, Any]:
    checks: list[CheckResult] = []

    # VS Code terminal detection
    if diag.term_program.lower() == "vscode":
        checks.append(CheckResult("VS Code terminal", "PASS", f"TERM_PROGRAM={diag.term_program}"))
    else:
        checks.append(CheckResult("VS Code terminal", "WARN", f"TERM_PROGRAM={diag.term_program!r}"))

    # Env var presence
    if diag.vscode_shell_integration_env:
        if diag.vscode_shell_integration_env_exists:
            checks.append(CheckResult(
                "VSCODE_SHELL_INTEGRATION env",
                "PASS",
                f"{diag.vscode_shell_integration_env}",
            ))
        else:
            checks.append(CheckResult(
                "VSCODE_SHELL_INTEGRATION env",
                "FAIL",
                f"Set but not found: {diag.vscode_shell_integration_env}",
            ))
    else:
        checks.append(CheckResult("VSCODE_SHELL_INTEGRATION env", "WARN", "not set"))

    # Code CLI
    if diag.code_cli_path:
        checks.append(CheckResult("VS Code CLI", "PASS", f"{diag.code_cli} at {diag.code_cli_path}"))
    else:
        checks.append(CheckResult("VS Code CLI", "WARN", "code/code-insiders not on PATH"))

    # Integration path via CLI
    if diag.code_cli_path:
        if diag.integration_path_from_cli:
            checks.append(CheckResult(
                "Integration path via CLI",
                "PASS",
                diag.integration_path_from_cli,
            ))
        else:
            checks.append(CheckResult("Integration path via CLI", "WARN", "not found via CLI"))
    else:
        checks.append(CheckResult("Integration path via CLI", "WARN", "skipped (CLI missing)"))

    # PATH hygiene
    checks.append(CheckResult(
        "/usr/local/bin in PATH",
        "PASS" if diag.path_contains_usr_local_bin else "WARN",
        str(diag.path_contains_usr_local_bin),
    ))
    checks.append(CheckResult(
        f"{str(Path.home() / '.local/bin')} in PATH",
        "PASS" if diag.path_contains_local_bin else "WARN",
        str(diag.path_contains_local_bin),
    ))

    # zshrc hints
    rc_label = f"{diag.shell}rc has integration block"
    if diag.rc_home_has_integration is True or diag.rc_repo_has_integration is True:
        checks.append(CheckResult(rc_label, "PASS", "detected"))
    elif diag.rc_home_has_integration is None and diag.rc_repo_has_integration is None:
        checks.append(CheckResult(rc_label, "WARN", f"no {diag.shell}rc found to inspect"))
    else:
        checks.append(CheckResult(rc_label, "WARN", "not detected"))

    # Overall verdict
    problems = 0
    if diag.term_program.lower() == "vscode":
        # In VS Code, integration is expected. Consider FAIL if neither env nor CLI-derived path present.
        if not diag.vscode_shell_integration_env and not diag.integration_path_from_cli:
            problems += 1
    else:
        # Not in VS Code; don't fail hard on integration absence.
        pass

    status = "ok" if problems == 0 else "issues"

    return {
        "status": status,
        "checks": [asdict(c) for c in checks],
        "diagnostics": asdict(diag),
        "recommendations": recommendations(diag),
    }


def recommendations(diag: Diagnostics) -> list[str]:
    recs: list[str] = []

    if diag.term_program.lower() != "vscode":
        recs.append("Open VS Code integrated terminal (View → Terminal) to test integration.")

    if not diag.vscode_shell_integration_env:
        recs.append("Ensure VS Code Terminal › Shell Integration is enabled in settings.")

    if not diag.code_cli_path:
        recs.append("Install the 'code' CLI: Command Palette → Shell Command: Install 'code' in PATH.")

    if diag.term_program.lower() == "vscode" and not diag.integration_path_from_cli and not diag.vscode_shell_integration_env:
        recs.append("Restart VS Code after updating, then open a fresh terminal.")
        recs.append("Confirm default profile is zsh: Terminal: Select Default Profile → zsh.")

    if not diag.path_contains_usr_local_bin:
        recs.append("Add /usr/local/bin to PATH early in ~/.zshrc (already done in this repo).")
    if not diag.path_contains_local_bin:
        recs.append("Add ~/.local/bin to PATH early in ~/.zshrc (already done in this repo).")

    if not (diag.rc_home_has_integration or diag.rc_repo_has_integration):
        recs.append(f"Add a guarded VS Code integration block to ~/.{diag.shell}rc (present in repo '{diag.shell}rc').")

    return recs


def colorize(status: str, no_color: bool) -> str:
    if no_color:
        return status
    colors = {
        "PASS": "\x1b[32mPASS\x1b[0m",
        "WARN": "\x1b[33mWARN\x1b[0m",
        "FAIL": "\x1b[31mFAIL\x1b[0m",
    }
    return colors.get(status, status)


def main() -> int:
    ap = argparse.ArgumentParser(description="Check VS Code shell integration health")
    ap.add_argument("--shell", choices=["zsh", "bash"], default="zsh", help="Shell to check (default: zsh)")
    ap.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    ap.add_argument("--no-color", action="store_true", help="Disable ANSI colors")
    args = ap.parse_args()

    diag = probe(args.shell)
    result = evaluate(diag)

    if args.__dict__["json"]:
        print(json.dumps(result, indent=2))
    else:
        print("VS Code zsh Shell Integration Check")
        print("-" * 40)
        for c in result["checks"]:
            print(f"[{colorize(c['status'], args.no_color)}] {c['label']}: {c['details']}")
        if result["recommendations"]:
            print("\nRecommendations:")
            for r in result["recommendations"]:
                print(f"- {r}")

    return 0 if result["status"] == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
