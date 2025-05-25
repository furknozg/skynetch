import click
from pathlib import Path
from dotenv import set_key, load_dotenv

ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
print(ENV_PATH)
@click.command()
@click.argument("key")
@click.argument("value")
def main(key: str, value: str):
    """Set an environment variable in the .env file."""
    load_dotenv(ENV_PATH)
    set_key(str(ENV_PATH), key, value)
    click.echo(f"Set {key}={value} in .env")

if __name__ == "__main__":
    main()