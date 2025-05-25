import click
import json
from src.app.infrastructure.kiwi_client import KiwiFlightSearchClient
from src.app.utils.query_builder import build_search_params
from src.app.infrastructure.sqlite_cache_repository import FlightSearchCacheRepository
from src.app.services.search_service import SearchService
@click.command()
@click.option('--source', default='Country:GB', help='Source location (e.g., Country:GB or City:london_gb)')
@click.option('--destination', default='City:dubrovnik_hr', help='Destination (e.g., City:dubrovnik_hr)')
@click.option('--outbound-start', default='2023-07-22T00:00:00', help='Outbound start date in ISO format')
@click.option('--outbound-end', default='2023-07-23T00:00:01', help='Outbound end date in ISO format')
@click.option('--price-start', type=int, help='Minimum price')
@click.option('--price-end', type=int, help='Maximum price')
@click.option('--days', default='SUNDAY,MONDAY,TUESDAY', help='Outbound flight days (comma-separated)')
@click.option('--adults', default=1, type=int, help='Number of adults')
@click.option('--children', default=0, type=int, help='Number of children')
@click.option('--infants', default=0, type=int, help='Number of infants')
def main(source, destination, outbound_start, outbound_end, price_start, price_end, days,
                   adults, children, infants):
    """Search one-way flights using Kiwi API"""
    client = KiwiFlightSearchClient()
    cache_repo = FlightSearchCacheRepository()  # defaults to flight_cache.db in cwd
    service = SearchService(api_client=client, cache_repo=cache_repo)

    params = build_search_params(
        source=source,
        destination=destination,
        outbound_start=outbound_start,
        outbound_end=outbound_end,
        price_start=price_start,
        price_end=price_end,
        outbound_days=[d.strip().upper() for d in days.split(',')],
        adults=adults,
        children=children,
        infants=infants,
    )

    try:
        results = service.search(params)
        click.echo(json.dumps(results, indent=2))
    except Exception as e:
        click.echo(f"Error: {e}", err=True)