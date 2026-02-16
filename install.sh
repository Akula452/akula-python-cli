#!/bin/bash
# Installation script for Linux/macOS

echo "Installing Akula Python CLI..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
required_version="3.7"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
    echo "Error: Python 3.7 or higher is required. You have Python $python_version"
    exit 1
fi

echo "Python version check passed: $(python3 --version)"
echo ""

# Install the package
echo "Installing package..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
fi

pip3 install -e .

# Verify installation
echo ""
echo "Verifying installation..."
if command -v akula &> /dev/null; then
    echo "✓ Installation successful!"
    echo ""
    echo "Run 'akula --help' to get started"
    akula --version
else
    echo "⚠ Warning: 'akula' command not found in PATH"
    echo "You may need to add ~/.local/bin to your PATH"
    echo "Add this line to your ~/.bashrc or ~/.zshrc:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
fi
