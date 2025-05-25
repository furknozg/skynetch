from typing import Dict, Any
from src.app.ports.api_client import FlightSearchClient
from datetime import datetime, timedelta
from src.app.ports.flight_cache import CacheRepository

class SearchService:
    def __init__(self, api_client: FlightSearchClient, cache_repo: CacheRepository):
        self.api_client = api_client
        self.cache_repo = cache_repo


    def search(self, search_params: Dict[str, Any], bypass_cache: bool) -> Dict[str, Any]:
        # Extract the outbound start date as the "query_date"
        query_date = search_params.get("outbound_start", "")[:10]  # e.g., "2023-07-22"
        
        if not bypass_cache:
            cached = self.cache_repo.get_cached_response(search_params, query_date, max_age_minutes=1440)
            if cached is not None:
                return cached
    

        fresh_result = self.api_client.search_one_way_flights(search_params)
        self.cache_repo.cache_response(search_params, fresh_result, query_date)
        return fresh_result