from pydantic import BaseModel, Field, validator # type: ignore
from datetime import datetime
from typing import Optional

class AirQualityData(BaseModel):
    timestamp: datetime = Field(..., alias="time")
    pm10: Optional[float]
    pm2_5: Optional[float]

class WeatherData(BaseModel):
    timestamp: datetime = Field(..., alias="time")
    temperature_celsius: float
    pressure_hpa: float
    humidity_percent: float

    @validator("temperature_celsius")
    def temp_valid(cls, v):
        if not (-50 <= v <= 60):
            raise ValueError("Temperature out of realistic range")
        return v

    @validator("pressure_hpa")
    def pressure_valid(cls, v):
        if not (300 <= v <= 1100):
            raise ValueError("Pressure out of realistic range")
        return v

    @validator("humidity_percent")
    def humidity_valid(cls, v):
        if not (0 <= v <= 100):
            raise ValueError("Humidity out of realistic range")
        return v
