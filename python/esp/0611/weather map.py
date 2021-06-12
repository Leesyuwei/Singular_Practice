import urequests as req
import ujson

apiURL = '{url}?q={city}&appid={key}'.format(
    url='http://api.openweathermap.org/data/2.5/weather',
    city='Taipei',
    key='34b1feab0ac8361b882a567b840aee21')

r = req.get(apiURL)
if r.status_code != 200:
    print("Bad request")
else:
    print("Data saved")
    data = ujson.loads(r.text)

    # weather = 'weather = {wthr}'.format(wthr=data["weather"][0]["main"])
    temp = 'temp = {tmp}\u00b0C'.format(tmp=data['main']['temp'] - 273.15)
    humidity = 'humidity = {hmd}%'.format(hmd=data['main']['humidity'])

    print(weather)
    print(temp)
    print(humidity)

# a = {
#     "coord": {
#         "lon": 121.5319,
#         "lat": 25.0478
#     },
#     "weather": [{
#         "id": 803,
#         "main": "Clouds",
#         "description": "broken clouds",
#         "icon": "04n"
#     }],
#     "base":
#     "stations",
#     "main": {
#         "temp": 303.33,
#         "feels_like": 310.33,
#         "temp_min": 301.38,
#         "temp_max": 304.31,
#         "pressure": 1009,
#         "humidity": 77
#     },
#     "visibility":
#     10000,
#     "wind": {
#         "speed": 1.34,
#         "deg": 140,
#         "gust": 4.92
#     },
#     "clouds": {
#         "all": 75
#     },
#     "dt":
#     1623412007,
#     "sys": {
#         "type": 2,
#         "id": 266033,
#         "country": "TW",
#         "sunrise": 1623359014,
#         "sunset": 1623408215
#     },
#     "timezone":
#     28800,
#     "id":
#     1668341,
#     "name":
#     "Taipei",
#     "cod":
#     200
# }
# {
#     'timezone':
#     28800,
#     'cod':
#     200,
#     'dt':
#     1623412007,
#     'base':
#     'stations',
#     'weather': [{
#         'id': 803,
#         'icon': '04n',
#         'main': 'Clouds',
#         'description': 'broken clouds'
#     }],
#     'sys': {
#         'country': 'TW',
#         'sunrise': 1623359014,
#         'sunset': 1623408215,
#         'id': 266033,
#         'type': 2
#     },
#     'name':
#     'Taipei',
#     'clouds': {
#         'all': 75
#     },
#     'coord': {
#         'lon': 121.532,
#         'lat': 25.0478
#     },
#     'visibility':
#     10000,
#     'wind': {
#         'gust': 4.92,
#         'speed': 1.34,
#         'deg': 140
#     },
#     'id':
#     1668341,
#     'main': {
#         'feels_like': 310.33,
#         'pressure': 1009,
#         'temp_min': 301.38,
#         'humidity': 77,
#         'temp_max': 304.31,
#         'temp': 303.33
#     }
# }
