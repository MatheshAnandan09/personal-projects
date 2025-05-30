
import requests
from twilio.rest import Client
api_key = '808586cd50f90df36d69317c1b91fd18'
ACCOUNT_SID = 'AC9a96f9dfce462e439a590ac872b45bca'
AUTH_TOKEN = '1f77352c1f4458c69fcbfa66cab35a3e'
PH_NUM = '+16202061443'
parameters = {
    'lat' : 13.082680,
    'lon' : 80.270721,
    'appid': api_key,
    'cnt' : 4
}


response = requests.get(url = 'https://api.openweathermap.org/data/2.5/forecast', params= parameters)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for i in range(len(weather_data)-1):
    weather_code = [weather_data['list'][i]['weather'][0]['id'] for i in range(len(weather_data)-1)]
    if weather_code[i] <700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body = 'Hey it will rain bring ☔️☔️☔️☔️ Umbrella',from_ = PH_NUM,to= '+916379841562',)