import base64
import json
from datetime import datetime

def decode_base64_json(b64string):
    decoded_bytes = base64.b64decode(b64string)
    return json.loads(decoded_bytes)

def parse_route_data(route_data):
    parts = route_data.split(':')
    # parts might look like ['FR', '5967', 'STN', '1756659600', 'DBV', '1756668900', 'economy', 'False', '', '', '']
    try:
        outbound_origin = parts[2]  # 'STN'
        outbound_time_start = int(parts[3])
        outbound_destination = parts[4]  # 'DBV'
        outbound_time_end = int(parts[5])

        # calculate duration in minutes
        duration_sec = outbound_time_end - outbound_time_start
        duration_min = duration_sec // 60

        return outbound_origin, outbound_destination, duration_min
    except Exception as e:
        return None, None, None

def decode_base64_cached_data(encoded_str):
    """
    Decode the cached Base64-encoded string after the first colon,
    then parse it as JSON.
    """
    try:
        prefix, b64data = encoded_str.split(':', 1)  # split at first colon only
        decoded_bytes = base64.b64decode(b64data)
        decoded_str = decoded_bytes.decode('utf-8')
        data = json.loads(decoded_str)
        return data
    except Exception as e:
        print(f"Failed to decode or parse cached data: {e}")
        return None

def parse_itinerary(itinerary):
    # Extract main details
    itinerary_id = itinerary.get('id')
    share_id = itinerary.get('shareId')

    # Price info (amount, before discount, EUR)
    price_info = itinerary.get('price', {})
    price_amount = price_info.get('amount')
    price_before_discount = price_info.get('priceBeforeDiscount')

    price_eur = itinerary.get('priceEur', {}).get('amount')

    # Provider info
    provider = itinerary.get('provider', {})
    provider_name = provider.get('name')

    # Bags info
    bags_info = itinerary.get('bagsInfo', {})
    included_checked_bags = bags_info.get('includedCheckedBags')
    included_hand_bags = bags_info.get('includedHandBags')

    # Sector details (first segment)
    sector = itinerary.get('sector', {})
    sector_segments = sector.get('sectorSegments', [])
    first_segment = sector_segments[0]['segment'] if sector_segments else {}

    flight_code = first_segment.get('code')
    departure_airport = first_segment.get('source', {}).get('station', {}).get('name')
    arrival_airport = first_segment.get('destination', {}).get('station', {}).get('name')
    departure_time = first_segment.get('source', {}).get('localTime')
    arrival_time = first_segment.get('destination', {}).get('localTime')
    carrier_name = first_segment.get('carrier', {}).get('name')

    # Return a summary dict
    return {
        "itinerary_id": itinerary_id,
        "share_id": share_id,
        "price_usd": price_amount,
        "price_before_discount": price_before_discount,
        "price_eur": price_eur,
        "provider": provider_name,
        "included_checked_bags": included_checked_bags,
        "included_hand_bags": included_hand_bags,
        "flight_code": flight_code,
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "carrier_name": carrier_name
    }