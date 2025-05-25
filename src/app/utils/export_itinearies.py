import csv
import json

def export_itineraries_to_csv(cached_response_json: str, csv_filename: str):
    data = json.loads(cached_response_json)

    if 'itineraries' not in data or not data['itineraries']:
        print("No itineraries found in cached response")
        return 0  # 0 entries exported

    itineraries = data['itineraries']

    fieldnames = [
        'id',
        'price_amount',
        'outbound_origin',
        'outbound_destination',
        'outbound_duration',
        'inbound_origin',
        'inbound_destination',
        'inbound_duration',
    ]

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for itin in itineraries:
            row = {
                'id': itin.get('id'),
                'price_amount': itin.get('price', {}).get('amount'),
                'outbound_origin': itin.get('outbound', {}).get('sectorSegments', [{}])[0].get('segment', {}).get('source', {}).get('station', {}).get('code'),
                'outbound_destination': itin.get('outbound', {}).get('sectorSegments', [{}])[0].get('segment', {}).get('destination', {}).get('station', {}).get('code'),
                'outbound_duration': itin.get('outbound', {}).get('duration'),
                'inbound_origin': itin.get('inbound', {}).get('sectorSegments', [{}])[0].get('segment', {}).get('source', {}).get('station', {}).get('code'),
                'inbound_destination': itin.get('inbound', {}).get('sectorSegments', [{}])[0].get('segment', {}).get('destination', {}).get('station', {}).get('code'),
                'inbound_duration': itin.get('inbound', {}).get('duration'),
            }
            writer.writerow(row)

    print(f"Exported {len(itineraries)} itineraries to {csv_filename}")
    return len(itineraries)