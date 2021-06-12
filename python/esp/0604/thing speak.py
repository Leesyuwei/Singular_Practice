import urequests as req
import time

while 1:
    apiURL = "{url}?key={key}&field1={temp}&field2={humid}".format(
        url="http://api.thingspeak.com/update",
        key="JQL2E0C28434TOZT",
        temp=25,
        humid=40)

    r = req.get(apiURL)

    if r.status_code != 200:
        print("Bad request")
    else:
        print("Data saved, id:", r.text)

    print("content", r.content)
    print("text", r.text)

    time.sleep(15)