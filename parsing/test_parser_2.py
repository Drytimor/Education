import requests
from parsing.apikey import API_Token

params = {"q": "Курск", "appid": API_Token, "units": "metric"}
data = {}
headers = {}

response = requests.get(r"https://api.openweathermap.org/data/2.5/weather", params=params)

print(response.headers)