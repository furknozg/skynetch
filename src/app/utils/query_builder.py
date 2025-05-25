from typing import List, Optional, Dict, Any

def build_search_params(
    source: Optional[str] = None,
    destination: Optional[str] = None,
    outbound_start: Optional[str] = None,
    outbound_end: Optional[str] = None,
    currency: str = "usd",
    locale: str = "en",
    adults: int = 1,
    children: int = 0,
    infants: int = 0,
    handbags: int = 1,
    holdbags: int = 0,
    cabin_class: str = "ECONOMY",
    sort_by: str = "QUALITY",
    sort_order: str = "ASCENDING",
    apply_mixed_classes: str = "true",
    allow_return_from_different_city: str = "true",
    allow_change_inbound_destination: str = "true",
    allow_change_inbound_source: str = "true",
    allow_different_station_connection: str = "true",
    enable_self_transfer: str = "true",
    allow_overnight_stopover: str = "true",
    enable_true_hidden_city: str = "true",
    enable_throwaway_ticketing: str = "true",
    price_start: Optional[int] = None,
    price_end: Optional[int] = None,
    max_stops_count: Optional[int] = None,
    outbound_days: Optional[List[str]] = None,
    transport_types: str = "FLIGHT",
    content_providers: str = "FLIXBUS_DIRECTS,FRESH,KAYAK,KIWI",
    limit: int = 20,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "currency": currency,
        "locale": locale,
        "adults": adults,
        "children": children,
        "infants": infants,
        "handbags": handbags,
        "holdbags": holdbags,
        "cabinClass": cabin_class,
        "sortBy": sort_by,
        "sortOrder": sort_order,
        "applyMixedClasses": apply_mixed_classes,
        "allowReturnFromDifferentCity": allow_return_from_different_city,
        "allowChangeInboundDestination": allow_change_inbound_destination,
        "allowChangeInboundSource": allow_change_inbound_source,
        "allowDifferentStationConnection": allow_different_station_connection,
        "enableSelfTransfer": enable_self_transfer,
        "allowOvernightStopover": allow_overnight_stopover,
        "enableTrueHiddenCity": enable_true_hidden_city,
        "enableThrowAwayTicketing": enable_throwaway_ticketing,
        "transportTypes": transport_types,
        "contentProviders": content_providers,
        "limit": limit,
    }

    if source:
        params["source"] = source
    if destination:
        params["destination"] = destination
    if outbound_start:
        params["outboundDepartmentDateStart"] = outbound_start
    if outbound_end:
        params["outboundDepartmentDateEnd"] = outbound_end
    if price_start is not None:
        params["priceStart"] = price_start
    if price_end is not None:
        params["priceEnd"] = price_end
    if max_stops_count is not None:
        params["maxStopsCount"] = max_stops_count
    if outbound_days:
        params["outbound"] = ",".join(outbound_days)

    return params
