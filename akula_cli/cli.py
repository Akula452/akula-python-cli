"""Main CLI module for Akula Python CLI."""

import click
import platform
import sys
from akula_cli import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    """Akula CLI - A cross-platform command-line tool for Windows and Linux."""
    pass


@cli.command()
@click.option('--name', default='World', help='Name to greet.')
def hello(name):
    """Say hello to someone."""
    click.echo(f'Hello, {name}!')
    click.echo(f'Running on: {platform.system()} {platform.release()}')


@cli.command()
def version():
    """Show the CLI version and system information."""
    click.echo(f'Akula CLI version: {__version__}')
    click.echo(f'Python version: {sys.version}')
    click.echo(f'Platform: {platform.platform()}')


@cli.command()
def sysinfo():
    """Display detailed system information."""
    click.echo('=== System Information ===')
    click.echo(f'System: {platform.system()}')
    click.echo(f'Release: {platform.release()}')
    click.echo(f'Version: {platform.version()}')
    click.echo(f'Machine: {platform.machine()}')
    click.echo(f'Processor: {platform.processor()}')
    click.echo(f'Python Version: {platform.python_version()}')
    click.echo(f'Python Implementation: {platform.python_implementation()}')


@cli.command()
@click.argument('text')
def echo(text):
    """Echo back the provided text."""
    click.echo(f'You said: {text}')


if __name__ == '__main__':
    cli()
