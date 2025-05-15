from datetime import datetime
from typing import List, Optional
from .models import WeatherData, AirQualityData

class DataRepository:
    def __init__(self):
        self.weather_data: List[WeatherData] = []
        self.air_quality_data: List[AirQualityData] = []

    def add_weather(self, weather: WeatherData) -> WeatherData:
        self.weather_data.append(weather)
        return weather

    def add_air_quality(self, air_quality: AirQualityData) -> AirQualityData:
        self.air_quality_data.append(air_quality)
        return air_quality

    def get_weather_closest(self, timestamp: str) -> Optional[WeatherData]:
        if not self.weather_data:
            return None
        dt = datetime.fromisoformat(timestamp)
        closest = min(self.weather_data, key=lambda x: abs(x.timestamp - dt))
        return closest

    def get_air_quality_closest(self, timestamp: str) -> Optional[AirQualityData]:
        if not self.air_quality_data:
            return None
        dt = datetime.fromisoformat(timestamp)
        closest = min(self.air_quality_data, key=lambda x: abs(x.timestamp - dt))
        return closest
