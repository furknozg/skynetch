
import click
from .setenv import main as setenv_cmd  # Relative import
from .search import main as search_cmd
from .export import main as export_cmd
from .inspect import main as inspect_cmd

@click.group()
def main():
    """Flight Data CLI"""
    pass

main.add_command(setenv_cmd, name="setenv")
main.add_command(search_cmd, name="search")
main.add_command(export_cmd, name="export")
main.add_command(inspect_cmd, name="inspect")

if __name__ == "__main__":
    main()