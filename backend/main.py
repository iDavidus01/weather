from fastapi import FastAPI, HTTPException, Request
from fastapi.routing import APIRouter
from backend.services import DataService
from backend.repositories import DataRepository
from pydantic import ValidationError

app = FastAPI()

repository = DataRepository()
service = DataService(repository)

router = APIRouter()

class WeatherAPI:
    def __init__(self, service: DataService):
        self.service = service

    async def post(self, request: Request):
        data = await request.json()
        try:
            saved = self.service.save_weather(data)
            return {"message": "Weather data saved", "data": saved.dict()}
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

class AirQualityAPI:
    def __init__(self, service: DataService):
        self.service = service

    async def post(self, request: Request):
        data = await request.json()
        try:
            saved = self.service.save_air_quality(data)
            return {"message": "Air quality data saved", "data": saved.dict()}
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

class ReadingAPI:
    def __init__(self, service: DataService):
        self.service = service

    async def get(self, request: Request):
        params = request.query_params
        timestamp = params.get("timestamp")
        data_type = params.get("type")

        if not timestamp or not data_type:
            raise HTTPException(status_code=400, detail="Missing 'timestamp' or 'type' parameter")

        try:
            result = self.service.get_closest_reading(timestamp, data_type)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())

        if result is None:
            raise HTTPException(status_code=404, detail="No data found")

        return result.dict()

weather_api = WeatherAPI(service)
air_quality_api = AirQualityAPI(service)
reading_api = ReadingAPI(service)

@router.post("/weather")
async def weather_post(request: Request):
    return await weather_api.post(request)

@router.post("/air_quality")
async def air_quality_post(request: Request):
    return await air_quality_api.post(request)

@router.get("/reading")
async def reading_get(request: Request):
    return await reading_api.get(request)

app.include_router(router)
