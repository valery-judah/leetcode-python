#!/bin/bash
# This script is executed every time a new terminal is opened in VSCode.

# Exit early if this is a non-interactive VSCode task
if [ -n "$VSCODE_TASK" ]; then
  return 0
fi

# Prevent prompt noise and conda auto-activation
# - Show venv only once (let your shell/theme handle it)
# - Keep Conda's base from auto-activating in VS Code terminals
export VIRTUAL_ENV_DISABLE_PROMPT=1
export CONDA_CHANGEPS1=no
export CONDA_AUTO_ACTIVATE_BASE=false

# If conda is active already in this shell, deactivate it
if command -v conda >/dev/null 2>&1; then
  # Make this persistent so future shells don't auto-activate base
  conda config --set auto_activate_base false >/dev/null 2>&1 || true
  if [ -n "${CONDA_SHLVL:-}" ] && [ "${CONDA_SHLVL:-0}" -gt 0 ]; then
    conda deactivate >/dev/null 2>&1 || true
  fi
fi

# Ensure Homebrew is on PATH so user-level tools (e.g., fzf) resolve in VS Code
if ! command -v brew >/dev/null 2>&1; then
  if [ -x "/opt/homebrew/bin/brew" ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)" 2>/dev/null || true
  elif [ -x "/usr/local/bin/brew" ]; then
    eval ""$(/usr/local/bin/brew shellenv)"" 2>/dev/null || true
  fi
fi

# Prefer an existing project venv if present and compatible. Only fall back
# to locating a system Python when we need to create/recreate the venv.

# If an existing venv is present and is >= 3.11, just activate it and exit.
if [ -x "venv/bin/python" ]; then
  VENV_VER=$(venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "")
  if [ -n "$VENV_VER" ]; then
    VMAJOR=${VENV_VER%%.*}
    VMINOR=${VENV_VER#*.}
    if [ "$VMAJOR" -gt 3 ] || { [ "$VMAJOR" -eq 3 ] && [ "$VMINOR" -ge 11 ]; }; then
      # Activate and open an interactive shell
      source venv/bin/activate
      echo "Using $(python --version)"
      exec "$SHELL" -il
    fi
  fi
fi

# Find a Python interpreter that is >= 3.11 (prefer 3.12/3.11)

find_python_ge_311() {
  for candidate in python3.12 python3.11 python3; do
    if command -v "$candidate" >/dev/null 2>&1; then
      local ver
      ver=$("$candidate" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "")
      if [ -n "$ver" ]; then
        local major=${ver%%.*}
        local minor=${ver#*.}
        if [ "$major" -gt 3 ] || { [ "$major" -eq 3 ] && [ "$minor" -ge 11 ]; }; then
          echo "$candidate"
          return 0
        fi
      fi
    fi
  done
  return 1
}

REQUIRED_PY=$(find_python_ge_311)
if [ -z "$REQUIRED_PY" ]; then
  echo "Python >=3.11 is required to (re)create the venv, but no system Python was found on PATH." >&2
  if [ -x "venv/bin/python" ]; then
    echo "Existing venv found; starting shell without re-creation." >&2
    source venv/bin/activate 2>/dev/null || true
    exec "$SHELL" -il
  fi
  echo "- macOS/Homebrew: brew install python@3.11 (or 3.12)" >&2
  echo "- Ensure brew is on PATH (e.g., echo 'eval \"\$(brew shellenv)\"' >> ~/.zprofile)" >&2
  echo "Continuing without venv activation so the terminal still opens..." >&2
  exec "$SHELL" -il
fi

create_venv() {
  echo "Creating virtual environment with $REQUIRED_PY..."
  "$REQUIRED_PY" -m venv venv
}

# 2) Create or align venv to Python 3.11
if [ -d "venv" ]; then
  CUR_VER=$(./venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "")
  DESIRED_VER=$("$REQUIRED_PY" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
  if [ "$CUR_VER" != "$DESIRED_VER" ]; then
    echo "Existing venv uses Python $CUR_VER; recreating with $DESIRED_VER..."
    rm -rf venv
    create_venv
  fi
else
  create_venv
fi

# 3) Activate the virtual environment
source venv/bin/activate
echo "Using $(python --version)"

# 4) Install/update dependencies using the Makefile target (best-effort)
if command -v make >/dev/null 2>&1; then
  echo "Installing dependencies..."
  make install || echo "Dependency install failed (continuing). Run 'make install' manually if needed."
fi

echo "Environment setup complete. Opening shell..."
exec "$SHELL" -il
