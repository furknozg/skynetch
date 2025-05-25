from abc import ABC, abstractmethod
from typing import Dict, Any

class FlightSearchClient(ABC):
    @abstractmethod
    def search_one_way_flights(self, params: Dict[str, Any]) -> Dict[str, Any]:
        pass