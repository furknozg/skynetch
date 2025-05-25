from abc import ABC, abstractmethod
from typing import Optional

class CacheRepository(ABC):
    @abstractmethod
    def get_cached_response(self, query_params: dict, query_date: str, max_age_minutes: int = 60) -> Optional[dict]:
        """Return cached response dict if found and fresh enough, else None."""
        pass

    @abstractmethod
    def cache_response(self, query_params: dict, response: dict, query_date: str) -> None:
        """Cache the response with query parameters and query date."""
        pass