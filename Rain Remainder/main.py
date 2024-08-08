import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

will_rain = False

parameters = {
    'lat': 33.684422,
    'lon': 73.047882,
    'appid': os.getenv("my_key"),
    'cnt': 4
}
weather_forecast = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
weather_forecast.raise_for_status()
weather_forecast = weather_forecast.json()['list']
every_weather = [int(single['weather'][0]['id']) for single in weather_forecast]
for weather_id in every_weather:
    if weather_id < 700:
        will_rain = True
        break
if will_rain:
    client = Client(os.getenv("acount_sid"), os.getenv("auth_token"))
    message = client.messages.create(body = "It's going to rain today. Remember to take an ☂️", to = "+923175102855",
                                     from_= "+18158648252")
print(message.status)