from .repositories import DataRepository
from .models import WeatherData, AirQualityData

class DataService:
    def __init__(self, repository: DataRepository):
        self.repository = repository

    def save_weather(self, data: dict) -> WeatherData:
        weather = WeatherData(**data)
        return self.repository.add_weather(weather)

    def save_air_quality(self, data: dict) -> AirQualityData:
        air_quality = AirQualityData(**data)
        return self.repository.add_air_quality(air_quality)

    def get_closest_reading(self, timestamp: str, data_type: str):
        if data_type == "weather":
            return self.repository.get_weather_closest(timestamp)
        elif data_type == "air_quality":
            return self.repository.get_air_quality_closest(timestamp)
        else:
            return None
