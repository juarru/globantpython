from fastapi import APIRouter
from fastapi import status

from v1.utils.weather_utils import create_json_response

router = APIRouter(prefix="/api/v1")


@router.get("/weather", status_code=status.HTTP_200_OK)
def get_weather(city: str, country: str):
    return create_json_response(city, country)
