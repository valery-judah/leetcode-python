#!/bin/bash
# This script is executed every time a new terminal is opened in VSCode.

# 1. Check for virtual environment and create if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  /usr/bin/python3 -m venv venv
fi

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Install/update dependencies using the Makefile target
echo "Installing dependencies..."
make install

echo "Environment setup complete."

# The final line of this script should be to execute the shell,
# otherwise the terminal will close after running the script.
exec "$SHELL"
