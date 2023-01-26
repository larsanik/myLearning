import json
import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if response.status_code == 200:
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    print('Координаты МКС: ' +
          position['latitude'] + ', ' + position['longitude'])
else:
    print("Хьюстон, у нас проблема:", response.status_code)

# json_string = '{"first": "Emmet", "last": "Brown", "prefix": "Dr."}'
#
# name = json.loads(json_string)
#
# print(name)
#
# print(name['prefix'], name['first'], name['last'])

