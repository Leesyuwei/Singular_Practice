from microbit import *
import radio
radio.config(channel=7)
radio.on()

while 1:
    display.show(str(radio.receive()))