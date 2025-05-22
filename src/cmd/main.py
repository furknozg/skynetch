
import click
from .setenv import main as setenv_cmd  # Relative import

@click.group()
def main():
    """Flight Data CLI"""
    pass

main.add_command(setenv_cmd, name="setenv")

if __name__ == "__main__":
    main()