from fastapi import APIRouter
from fastapi import status

from v1.utils.weather_utils import get_external_weather, generate_response_json

router = APIRouter(prefix="/api/v1")


@router.get("/weather/", status_code=status.HTTP_200_OK)
def get_weather():
    response_string = get_external_weather()
    response_json = generate_response_json(response_string)

    return response_json
