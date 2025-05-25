import click
import sqlite3
import json


@click.command()
@click.option('--db-path', default='flight_cache.db', help='Path to the SQLite cache file')
def main(db_path):
    """Inspect cached flight responses and check for 'data' field content."""
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT query_date, timestamp, LENGTH(response), response FROM flight_cache")

    entries = cursor.fetchall()
    if not entries:
        click.echo("No cache entries found.")
        return

    for i, (query_date, timestamp, length, response) in enumerate(entries, start=1):
        try:
            data = json.loads(response)
            flights = data.get("data", [])
            click.echo(f"\n--- Entry {i} ---")
            click.echo(f"Query Date: {query_date}")
            click.echo(f"Timestamp: {timestamp}")
            click.echo(f"Response Size: {length} bytes")
            click.echo(f"Flights Found: {len(flights)}")
            if flights:
                click.echo(f"Sample flight keys: {list(flights[0].keys())}")
        except json.JSONDecodeError as e:
            click.echo(f"\nEntry {i}: Failed to decode response: {e}")

    conn.close()