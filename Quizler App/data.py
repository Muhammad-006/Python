import requests
import html

dictionary = {
    "amount": 10,
    'type': "boolean"
}
question_data = requests.get(url = "https://opentdb.com/api.php", params = dictionary)
question_data.raise_for_status()
question_data = question_data.json()['results']
