import json
import requests
import turtle


def move_iss(lat, long):
    global iss
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()


screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape('iss.gif')
iss.shape('iss.gif')


url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if response.status_code == 200:
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    # print('Координаты МКС: ' +
    #       position['latitude'] + ', ' + position['longitude'])
    lat = float(position['latitude'])
    long = position['longitude']
    move_iss(lat, long)
else:
    print("Хьюстон, у нас проблема:", response.status_code)

turtle.mainloop()

# json_string = '{"first": "Emmet", "last": "Brown", "prefix": "Dr."}'
#
# name = json.loads(json_string)
#
# print(name)
#
# print(name['prefix'], name['first'], name['last'])

