from typing import List, Optional
from datetime import datetime
from backend.models import AirQualityData, WeatherData

class DataRepository:
    def __init__(self):
        self.weather_data: List[WeatherData] = []
        self.air_quality_data: List[AirQualityData] = []

    def add_weather(self, data: WeatherData):
        self.weather_data.append(data)

    def add_air_quality(self, data: AirQualityData):
        self.air_quality_data.append(data)

    def get_closest_weather(self, timestamp: datetime) -> Optional[WeatherData]:
        if not self.weather_data:
            return None
        return min(self.weather_data, key=lambda d: abs(d.timestamp - timestamp))

    def get_closest_air_quality(self, timestamp: datetime) -> Optional[AirQualityData]:
        if not self.air_quality_data:
            return None
        return min(self.air_quality_data, key=lambda d: abs(d.timestamp - timestamp))
