from backend.models import WeatherData, AirQualityData
from backend.repositories import DataRepository
from typing import Union

class DataService:
    def __init__(self, repository: DataRepository):
        self.repository = repository

    def save_weather(self, data_dict: dict) -> WeatherData:
        data = WeatherData(**data_dict)
        self.repository.add_weather(data)
        return data

    def save_air_quality(self, data_dict: dict) -> AirQualityData:
        data = AirQualityData(**data_dict)
        self.repository.add_air_quality(data)
        return data

    def get_closest_reading(self, timestamp: str, data_type: str) -> Union[WeatherData, AirQualityData, None]:
        from datetime import datetime
        dt = datetime.fromisoformat(timestamp)
        if data_type == "weather":
            return self.repository.get_closest_weather(dt)
        elif data_type == "air_quality":
            return self.repository.get_closest_air_quality(dt)
        else:
            return None
