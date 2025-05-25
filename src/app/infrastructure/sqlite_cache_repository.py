import sqlite3
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from src.app.ports.flight_cache import CacheRepository

class FlightSearchCacheRepository(CacheRepository):
    def __init__(self, db_path: str = "flight_cache.db"):
        self.db_path = db_path
        self._ensure_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _ensure_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS flight_cache (
                    query_hash TEXT PRIMARY KEY,
                    response TEXT,
                    timestamp TEXT,
                    query_date TEXT
                )
            """)
            conn.commit()

    def _generate_hash(self, query_params: dict) -> str:
        query_string = json.dumps(query_params, sort_keys=True)
        return hashlib.sha256(query_string.encode()).hexdigest()

    def get_cached_response(self, query_params: dict, query_date: str, max_age_minutes: int = 60):
        query_hash = self._generate_hash(query_params)
        cutoff_time = (datetime.utcnow() - timedelta(minutes=max_age_minutes)).isoformat()

        with self._connect() as conn:
            cursor = conn.execute("""
                SELECT response, timestamp FROM flight_cache
                WHERE query_hash = ? AND query_date = ?
                ORDER BY timestamp DESC
                LIMIT 1
            """, (query_hash, query_date))
            row = cursor.fetchone()

        if not row:
            return None

        # Check if cached record is still fresh
        response_json, timestamp_str = row
        if timestamp_str < cutoff_time:
            return None
        return json.loads(response_json)

    def cache_response(self, query_params: dict, response: dict, query_date: str):
        query_hash = self._generate_hash(query_params)
        timestamp = datetime.utcnow().isoformat()

        with self._connect() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO flight_cache (query_hash, response, timestamp, query_date)
                VALUES (?, ?, ?, ?)
            """, (query_hash, json.dumps(response), timestamp, query_date))
            conn.commit()
