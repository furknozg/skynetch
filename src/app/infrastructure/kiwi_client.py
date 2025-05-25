import requests
from typing import Dict, Any
from src.app.ports.api_client import FlightSearchClient
from dotenv import load_dotenv
import os

load_dotenv()

class KiwiFlightSearchClient(FlightSearchClient):
    BASE_URL = "https://kiwi-com-cheap-flights.p.rapidapi.com/one-way"

    def __init__(self):
        self.headers = {
            "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com",
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        }

    def search_one_way_flights(self, params: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.get(self.BASE_URL, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()