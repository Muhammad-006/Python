import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': os.getenv("alpha_api_key")
}
news_parameters = {
    'q': COMPANY_NAME,
    "from": "2024-08-08&",
    "sortBy": "popularity&",
    'apiKey': os.getenv("news_api_key")
}

alpha_data = requests.get(url = 'https://www.alphavantage.co/query', params = alpha_parameters)
alpha_data.raise_for_status()
alpha_data = alpha_data.json()
# yesterday = float(alpha_data['Time Series (Daily)']['2024-08-07']['4. close'])
# day_before = float(alpha_data['Time Series (Daily)']['2024-08-06']['4. close'])

yesterday = 204.545 # used this because apikey expired
day_before = 191.457 # used this because apikey expired

percent_change = ((yesterday - day_before) / day_before) * 100
if -5 >= percent_change or percent_change >= 5:
    news_data = requests.get(url = 'https://newsapi.org/v2/everything', params = news_parameters)
    news_data.raise_for_status()
    news_data = news_data.json()
    if -5 >= percent_change:
        percent_change = f"🔻{-1 * percent_change}"
    elif percent_change >= 5:
        percent_change = f"🔺{percent_change}"
    for i in range (3):
        news_title = news_data['articles'][i]['title']
        news_description = news_data['articles'][i]['description']
        client = Client(os.getenv("acount_sid"), os.getenv("auth_token"))
        message = client.messages.create(body = f"TSLA: {percent_change}\nHeadline: {news_title}\n"
                                                f"Brief: {news_description}",
                                         to="+923175102855",
                                         from_="+18158648252")


