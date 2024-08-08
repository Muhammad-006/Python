from dotenv import load_dotenv
import requests
import os
from datetime import datetime

hours = float(input("How many hours did you manage to work today?"))

USERNAME = "muhammad06"
load_dotenv()

user_parameters = {
    "token": os.getenv('API_TOKEN'),
    "username": USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes'
}


# user_entry = requests.post(url = "https://pixe.la/v1/users", json = user_parameters)

graph_configurations = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

graph_header = {
    "X-USER-TOKEN": os.getenv("API_TOKEN")
}

# graph_creation = requests.post(url = f"https://pixe.la/v1/users/{USERNAME}/graphs",
#                                  json = graph_configurations,
#                                  headers = graph_header)

date = datetime.now()

graph_values = {
    "date": f"{date.strftime("%Y%m%d")}",
    "quantity": f"{hours}"
}

graph_value_entry = requests.post(url = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1", json = graph_values,
                                  headers = graph_header)
