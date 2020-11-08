from microbit import *
import radio
radio.config(channel=7)
radio.on()

while 1:
    motion=radio.receive()
    if motion=='left':
        display.show(Image.ARROW_E)
    elif motion=='right':
        display.show(Image.ARROW_W)
    else:
        display.show('0')
    sleep(500)