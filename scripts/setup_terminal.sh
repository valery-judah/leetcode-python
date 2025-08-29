#!/bin/bash
# This script is executed every time a new terminal is opened in VSCode.

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

# Find a Python interpreter that is >= 3.11 (prefer 3.12/3.11),
# and avoid hard-failing when not present so the terminal still opens.

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
  echo "Python >=3.11 is required but not found on PATH." >&2
  echo "- macOS/Homebrew: brew install python@3.11 (or 3.12)" >&2
  echo "- Ensure brew is on PATH (e.g., echo 'eval \"$($(which brew) shellenv)\"' >> ~/.zprofile)" >&2
  echo "Continuing without venv activation so the terminal still opens..." >&2
  exec "$SHELL"
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

# 4) Install/update dependencies using the Makefile target
echo "Installing dependencies..."
if command -v make >/dev/null 2>&1; then
  make install || echo "Dependency install failed (continuing). Run 'make install' manually if needed."
else
  echo "'make' not found; skipping dependency installation."
fi

echo "Environment setup complete."

# The final line of this script should be to execute an interactive login shell,
# otherwise the terminal will close after running the script.
exec "$SHELL" -il
