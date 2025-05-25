import click
from src.app.infrastructure.sqlite_cache_repository import FlightSearchCacheRepository
from src.app.utils.export_itinearies import export_itineraries_to_csv  # your existing function
import json
import csv
from src.app.utils.base64_parser import parse_itinerary
@click.command()
@click.option('--query-date', help='Only export results from this query date (YYYY-MM-DD)')
@click.option('--output', default='export.csv', help='Output CSV file name')
def main(query_date, output):
    """Export cached flight itineraries to CSV"""

    cache_repo = FlightSearchCacheRepository()
    results = cache_repo.export_cached_responses(query_date=query_date)

    if not results:
        click.echo("No cached results found for export.")
        return

    total_exported = 0

    # Open CSV once, write all rows incrementally
    # So your export_itineraries_to_csv() needs to be adjusted for this,
    # or you can handle CSV writing here fully.

    # For simplicity, we rewrite export_itineraries_to_csv here to accept a file handle.

    import csv


    fieldnames = ['itinerary_id', 'share_id', 'price_usd', 'price_before_discount', 'price_eur', 
              'provider', 'included_checked_bags', 'included_hand_bags', 'flight_code', 
              'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'carrier_name', "booking_url", 
              "price_change_likely",
              "is_hidden_city",
              "is_virtual_interlining",
              "is_throwaway_ticket"]

    with open(output, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for result in results:
            # The cached response string is probably in a certain key,
            # adjust 'cached_response_field' to your actual dict key holding this string
            cached_response_field = None
            # For example, if result looks like {'response': 'ItineraryOneWay:eyJ...'}
            if 'itineraries' in result:
                cached_response_field = result['itineraries']
            
            if not cached_response_field:
                continue
            
            for itin in cached_response_field:
                row = parse_itinerary(itin)
                writer.writerow(row)
                total_exported += 1

    click.echo(f"Exported {total_exported} itineraries to {output}")