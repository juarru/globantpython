import requests
import json
import datetime

url = "http://api.openweathermap.org/data/2.5/weather?q=Bogota,co&appid=1508a9a4840a5574c822d70ca2132032"


def get_external_weather():
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

def generate_response_json(response_string: str):
    response_json = json.loads(response_string)

    final_response = {
        "location_name": "Bogota, CO",
        "temperature": response_json["main"]["temp"],
        "wind": "Wind speed:" + str(response_json["wind"]["speed"]) + " m/s",
        "cloudiness": response_json["weather"][0]["description"],
        "pressure": str(response_json["main"]["pressure"]) + " hpa",
        "humidity": str(response_json["main"]["humidity"]) + "%",
        "sunrise": response_json["sys"]["sunrise"],
        "sunset": response_json["sys"]["sunset"],
        "geo_coordinates": "[" + str(round(response_json["coord"]["lat"], 2)) + "," + str(round(response_json["coord"]["lon"], 2)) + "]",
        "requested_time": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    return final_response


