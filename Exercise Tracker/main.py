from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

date = datetime.now().strftime("%d/%m/%Y")
hours = datetime.now().strftime("%X")
sheety_auth = os.getenv("AUTH")
sheety_url = os.getenv("SHEETY_URL")

exercise = input("Tell me which exercises you did: ")

api_key = os.getenv("API_KEY")
app_id = os.getenv("APP_ID")

upload_header = {
    'x-app-id': app_id,
    'x-app-key': api_key
  }

upload_params = {
    'query': exercise
}

upload_data = requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise", json = upload_params,
                            headers = upload_header)
upload_data = upload_data.json()

sheety_params = {}

sheety_headers = {
   "Authorization": sheety_auth
}

for exercise in upload_data["exercises"]:
    sheety_params = {
        "workout": {
            "date": date,
            "time": hours,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    upload_sheety = requests.post(url = sheety_url, json=sheety_params, headers = sheety_headers)
    print(upload_sheety.text)


