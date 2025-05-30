import requests
from datetime import datetime
MY_LAT = 13.082680
MY_LNG = 80.270721
MY_TIME_ZONE = 'IST'
#
# response = requests.get(url = 'http://api.open-notify.org/iss-now.json' )
# response.raise_for_status()
#
#
# latitude = response.json()['iss_position']['latitude']
# longitude = response.json()['iss_position']['longitude']
# print((latitude, longitude ))
parameters = {
    'lat' : MY_LAT,
    'lng' : MY_LNG,
    'formatted':  0

}
response = requests.get(url = 'https://api.sunrise-sunset.org/json', params = parameters )
response.raise_for_status()
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

now =datetime.now()
print(f'now {now.hour}')
print(f'sunset {sunset.split('T')[1].split(':')[0]}')
print(f'sunrise {sunrise.split('T')[1].split(':')[0]}')


