# Contributing to Akula Python CLI

Thank you for your interest in contributing to Akula Python CLI! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/akula-python-cli.git
   cd akula-python-cli
   ```
3. Install in development mode:
   ```bash
   pip install -e .
   ```

## Development Setup

### Prerequisites
- Python 3.7 or higher
- pip
- git

### Installation for Development
```bash
# Install dependencies
pip install -r requirements.txt

# Install in editable mode
pip install -e .
```

## Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes to the code

3. Test your changes:
   ```bash
   # Test the CLI
   akula --help
   akula hello --name "Test"
   
   # Or run directly
   python -m akula_cli.cli --help
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

## Adding New Commands

To add a new command to the CLI:

1. Open `akula_cli/cli.py`
2. Add a new function decorated with `@cli.command()`
3. Use Click decorators for options and arguments
4. Add a docstring to describe the command

Example:
```python
@cli.command()
@click.option('--option', default='value', help='Description')
def mycommand(option):
    """Description of what this command does."""
    click.echo(f'Running command with {option}')
```

## Testing

Before submitting a pull request:

1. Test on Linux (if possible)
2. Test on Windows (if possible)
3. Verify all existing commands still work
4. Test your new feature/fix thoroughly

## Reporting Issues

When reporting issues, please include:

- Your operating system (Windows/Linux version)
- Python version
- Full error message and stack trace
- Steps to reproduce the issue

## Questions?

Feel free to open an issue for any questions or discussions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
