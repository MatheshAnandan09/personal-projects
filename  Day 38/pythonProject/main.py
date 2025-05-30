import requests
from datetime import datetime
import os




URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

API_ID =os.environ.get('API_ID')
API_KEY =os.environ.get('API_KEY')
AUTH= os.environ.get('AUTH')
headers = {
    'x-app-id' : API_ID,
    'x-app-key' : API_KEY,

}
answer = str(input('How many kilometers you ran today?'))
parameters = {
    'query' : answer
}

response = requests.post(url = URL, json= parameters,headers = headers)
result = response.json()


date = datetime.today().strftime('%d/%m/%Y')

time = datetime.today().strftime('%I:%M:%S')

shitty_url = 'https://api.sheety.co/615bffecbadea749aba8f59fd884c8e8/workouts/sheet1'
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        'Authorization': AUTH
    }


    response = requests.post(url = shitty_url, json= sheet_inputs, headers=headers)
    print(response.text)

