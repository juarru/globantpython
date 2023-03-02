import requests
import json
import os
import datetime as dat
from cachier import cachier
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


def create_json_response(city: str, country: str):
    response_string = get_external_weather(city.capitalize(), country.lower())
    response_json = generate_response_json(city.capitalize(), country.upper(), response_string)

    return response_json


@cachier(stale_after=dat.timedelta(minutes=2))
def get_external_weather(city: str, country: str):
    payload = {}
    headers = {}
    q = city + "," + country
    appid = os.getenv('EXTERNAL_API_APPID')
    url = os.getenv('EXTERNAL_API_URL') + "?q=" + q + "&appid=" + appid

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def generate_response_json(city: str, country: str, response_string: str):
    response_json = json.loads(response_string)

    final_response = {
        "location_name": city + ", " + country,
        "temperature": str(convert_celsius(response_json["main"]["temp"])) + " ºC",
        "wind": "Wind speed: " + str(response_json["wind"]["speed"]) + " m/s",
        "cloudiness": response_json["weather"][0]["description"],
        "pressure": str(response_json["main"]["pressure"]) + " hpa",
        "humidity": str(response_json["main"]["humidity"]) + "%",
        "sunrise": datetime.fromtimestamp(response_json["sys"]["sunrise"]).strftime("%H:%M:%S"),
        "sunset": datetime.fromtimestamp(response_json["sys"]["sunset"]).strftime("%H:%M:%S"),
        "geo_coordinates": "[" + str(round(response_json["coord"]["lat"], 2)) + "," + str(round(response_json["coord"]["lon"], 2)) + "]",
        "requested_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    return final_response


def convert_celsius(temp: float):
    return round((temp - 273.15), 2)


