from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.routing import APIRouter
from backend.services import DataService
from backend.repositories import DataRepository
from backend.models import WeatherData, AirQualityData
from pydantic import ValidationError
from typing import Optional

app = FastAPI()

repository = DataRepository()
service = DataService(repository)

router = APIRouter()

class WeatherAPI:
    def __init__(self, service: DataService):
        self.service = service

    async def post(self, data: WeatherData):
        try:
            saved = self.service.save_weather(data)
            return {"message": "Weather data saved", "data": saved.dict()}
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

class AirQualityAPI:
    def __init__(self, service: DataService):
        self.service = service

    async def post(self, data: AirQualityData):
        try:
            saved = self.service.save_air_quality(data)
            return {"message": "Air quality data saved", "data": saved.dict()}
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

class ReadingAPI:
    def __init__(self, service: DataService):
        self.service = service

    async def get(self, timestamp: str, data_type: str):
        if data_type not in ("weather", "air_quality"):
            raise HTTPException(status_code=400, detail="Invalid 'type' parameter")
        result = self.service.get_closest_reading(timestamp, data_type)
        if result is None:
            raise HTTPException(status_code=404, detail="No data found")
        return result.dict()

weather_api = WeatherAPI(service)
air_quality_api = AirQualityAPI(service)
reading_api = ReadingAPI(service)

@router.post("/weather")
async def weather_post(data: WeatherData):
    return await weather_api.post(data)

@router.post("/air_quality")
async def air_quality_post(data: AirQualityData):
    return await air_quality_api.post(data)

@router.get("/reading")
async def reading_get(timestamp: str, type: str):
    return await reading_api.get(timestamp, type)

app.include_router(router)
