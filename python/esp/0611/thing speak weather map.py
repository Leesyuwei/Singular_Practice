import urequests as req
import ujson
import time

while 1:
    apiURL1 = '{url}?q={city}&appid={key}'.format(
        url='http://api.openweathermap.org/data/2.5/weather',
        city='Taipei',
        key='34b1feab0ac8361b882a567b840aee21')

    r = req.get(apiURL1)

    if r.status_code != 200:
        print("Bad request")
    else:
        print("Data saved")
        data = ujson.loads(r.text)

        # weather = 'weather = {wthr}'.format(wthr=data["weather"][0]["main"])
        temperature = data['main']['temp'] - 273.15
        humidity = data['main']['humidity']

        # print(weather)
        print('temp = {tmp}\u00b0C'.format(tmp=data['main']['temp'] - 273.15))
        print('humidity = {hmd}%'.format(hmd=data['main']['humidity']))

        apiURL2 = "{url}?key={key}&field1={temp}&field2={humid}".format(
            url="http://api.thingspeak.com/update",
            key="JQL2E0C28434TOZT",
            temp=temperature,
            humid=humidity)

        r = req.get(apiURL2)

        if r.status_code != 200:
            print("Bad request")
        else:
            print("Data saved")

    time.sleep(15)