import requests
from datetime import datetime
from typing import Optional

class airClient:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude
        self.base_url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    def fetch_current_data(self) -> Optional[dict]:
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "hourly": "pm10,pm2_5"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
