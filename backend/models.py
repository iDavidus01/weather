from pydantic import BaseModel, Field, validator
from datetime import datetime

class WeatherData(BaseModel):
    timestamp: datetime
    temperature_celsius: float = Field(...)
    pressure_hpa: float = Field(...)
    humidity_percent: float = Field(...)

    @validator('temperature_celsius')
    def check_temperature(cls, v):
        if not (-90 <= v <= 60):
            raise ValueError("temperature out of realistic range")
        return v

    @validator('pressure_hpa')
    def check_pressure(cls, v):
        if not (300 <= v <= 1100):
            raise ValueError("pressure out of realistic range")
        return v

    @validator('humidity_percent')
    def check_humidity(cls, v):
        if not (0 <= v <= 100):
            raise ValueError("humidity must be 0-100%")
        return v

class AirQualityData(BaseModel):
    timestamp: datetime
    pm10: float
    pm2_5: float
