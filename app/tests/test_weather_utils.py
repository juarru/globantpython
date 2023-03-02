import sys
sys.path.append("app")
from utils.weather_utils import convert_celsius, get_external_weather, generate_response_json


def test_convert_celsius_ok():
    result = convert_celsius(300)
    assert result == 26.85


def test_get_external_weather_ok():
    response = get_external_weather("Bogota", "co")
    assert type(response) is str


def test_generate_response_json_ok():
    response = get_external_weather("Bogota", "co")
    result = generate_response_json("Bogota", "CO", response)

    assert result["location_name"] == "Bogota, CO"
