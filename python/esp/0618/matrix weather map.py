import urequests as req
import ujson
import time

from machine import Pin, SPI
from micropython import const
import framebuf

_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)


class Matrix8x8:
    def __init__(self, spi, cs, num):
        self.spi = spi
        self.cs = cs
        self.cs.init(cs.OUT, True)
        self.buffer = bytearray(8 * num)
        self.num = num
        fb = framebuf.FrameBuffer(self.buffer, 8 * num, 8, framebuf.MONO_HLSB)
        self.framebuf = fb
        # Provide methods for accessing FrameBuffer graphics primitives. This is a workround
        # because inheritance from a native class is currently unsupported.
        # http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
        self.fill = fb.fill  # (col)
        self.pixel = fb.pixel  # (x, y[, c])
        self.hline = fb.hline  # (x, y, w, col)
        self.vline = fb.vline  # (x, y, h, col)
        self.line = fb.line  # (x1, y1, x2, y2, col)
        self.rect = fb.rect  # (x, y, w, h, col)
        self.fill_rect = fb.fill_rect  # (x, y, w, h, col)
        self.text = fb.text  # (string, x, y, col=1)
        self.scroll = fb.scroll  # (dx, dy)
        self.blit = fb.blit  # (fbuf, x, y[, key])
        self.init()

    def _write(self, command, data):
        self.cs(0)
        for m in range(self.num):
            self.spi.write(bytearray([command, data]))
        self.cs(1)

    def init(self):
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(command, data)

    def brightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def show(self):
        for y in range(8):
            self.cs(0)
            for m in range(self.num):
                self.spi.write(
                    bytearray([_DIGIT0 + y, self.buffer[(y * self.num) + m]]))
            self.cs(1)


spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = Matrix8x8(spi, Pin(15), 4)  # 設定傳輸協定, Pin CS, matrix數量

# s = "ABCDEF"
# while True:
#     for a in range(len(s)):
#         display.fill(0)
#         display.text(s[a:a + 4], 0, 0, 1)
#         for i in range(0, 8):
#             display.scroll(-1, 0)
#             display.show()
#             time.sleep(0.5)

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

        weather = data["weather"][0]["main"]
        temperature = data['main']['temp'] - 273.15
        humidity = data['main']['humidity']
        temperature_display = str(round(temperature) * 10) + "C"
        humidity_display = str(humidity) + '%'

        print('weather = {wthr}'.format(wthr=data["weather"][0]["main"]))
        print('temp = {tmp}\u00b0C'.format(tmp=data['main']['temp'] - 273.15))
        print('humidity = {hmd}%'.format(hmd=data['main']['humidity']))

        weather_dict = {
            "Thunderstorm": "THDR",
            "Drizzle": "DRZL",
            "Rain": "RAIN",
            "Snow": "SNOW",
            "Mist": "MIST",
            "Smoke": "SMOK",
            "Haze": "HAZE",
            "Dust": "DUST",
            "Fog": "FOG",
            "Sand": "SAND",
            "Dust": "DUST",
            "Ash": "ASH",
            "Squall": "SQUL",
            "Tornado": "TRND",
            "Clear": "CLR",
            "Clouds": "CLDS"
        }
        if weather in weather_dict.keys():
            weather = weather_dict[weather]
        else:
            weather = weather

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

        wait = 5

        display.brightness(1)  # 亮度設定
        display.fill(0)
        display.text(weather, 0, 1, 1)
        display.show()
        time.sleep(wait)

        display.fill(0)
        display.text(temperature_display, 0, 1, 1)
        display.rect(24, 0, 1, 1, 1)
        display.rect(16, 7, 1, 1, 1)
        display.show()
        time.sleep(wait)

        display.fill(0)
        display.text(humidity_display, 0, 1, 1)
        display.show()
        time.sleep(wait)
