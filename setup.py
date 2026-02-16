"""Setup script for Akula Python CLI."""

try:
    from setuptools import setup, find_packages
except ImportError:
    import sys
    print("Error: setuptools is not installed.", file=sys.stderr)
    print("\nPlease install setuptools first:", file=sys.stderr)
    print("  pip install --upgrade setuptools wheel", file=sys.stderr)
    print("\nOr use the recommended installation method:", file=sys.stderr)
    print("  pip install -e .", file=sys.stderr)
    sys.exit(1)

import os

# Read the version from __init__.py
version = {}
with open(os.path.join("akula_cli", "__init__.py")) as f:
    exec(f.read(), version)

# Read the README for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="akula-cli",
    version=version["__version__"],
    author="Akula452",
    description="A cross-platform command-line tool for Windows and Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akula452/akula-python-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "akula=akula_cli.cli:cli",
        ],
    },
)
