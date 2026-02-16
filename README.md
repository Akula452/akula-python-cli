# Akula Python CLI

A cross-platform command-line interface tool built with Python that works seamlessly on both Windows and Linux operating systems.

## Features

- ✅ Cross-platform compatibility (Windows & Linux)
- ✅ Easy to install and use
- ✅ Multiple useful commands
- ✅ System information display
- ✅ Built with Click for excellent CLI experience

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### Prerequisites

Before installation, ensure you have:
- Python 3.7 or higher
- pip (Python package installer)
- setuptools and wheel (will be installed automatically with pip)

### Method 1: Quick Install (Recommended)

This method automatically handles all build dependencies:

```bash
git clone https://github.com/Akula452/akula-python-cli.git
cd akula-python-cli
pip install -e .
```

### Method 2: Install with requirements file

```bash
git clone https://github.com/Akula452/akula-python-cli.git
cd akula-python-cli
pip install -r requirements.txt
pip install -e .
```

### Method 3: Using setup.py directly (for advanced users)

**Note:** This method is only needed for specific build scenarios. Most users should use Method 1 instead.

If you need to use setup.py directly and encounter import errors:

```bash
pip install --upgrade setuptools wheel
python setup.py develop
```

### Verification

After installation, verify that the CLI is installed correctly:
```bash
akula --version
```

## Usage

### Available Commands

#### 1. Hello Command
Greet someone with a friendly message:
```bash
akula hello
akula hello --name "Your Name"
```

#### 2. Version Command
Display version and system information:
```bash
akula version
```

#### 3. System Info Command
Display detailed system information:
```bash
akula sysinfo
```

#### 4. Echo Command
Echo back any text you provide:
```bash
akula echo "Hello from Akula CLI!"
```

#### 5. Help
Get help on available commands:
```bash
akula --help
akula hello --help
```

## Platform-Specific Instructions

### Linux

On Linux, you might need to use `pip3` instead of `pip`:
```bash
pip3 install -e .
```

If you get permission errors, you can install in user mode:
```bash
pip install --user -e .
```

### Windows

On Windows, make sure Python and pip are added to your PATH. You can then run:
```bash
pip install -e .
```

If you're using PowerShell and encounter execution policy errors, you may need to run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Development

### Project Structure

```
akula-python-cli/
├── akula_cli/
│   ├── __init__.py      # Package initialization and version
│   └── cli.py           # Main CLI implementation
├── setup.py             # Setup script for installation
├── pyproject.toml       # Modern Python project configuration
├── requirements.txt     # Package dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

### Running without installation

You can also run the CLI directly without installation:
```bash
python -m akula_cli.cli --help
python -m akula_cli.cli hello
```

## Uninstallation

To uninstall the CLI:
```bash
pip uninstall akula-cli
```

## License

MIT License

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Akula452