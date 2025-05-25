
import click
from .setenv import main as setenv_cmd  # Relative import
from .search import main as search_cmd

@click.group()
def main():
    """Flight Data CLI"""
    pass

main.add_command(setenv_cmd, name="setenv")

main.add_command(search_cmd, name="search")

if __name__ == "__main__":
    main()