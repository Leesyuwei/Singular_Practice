from microbit import *
import radio
radio.config(channel=7)
radio.on()

while 1:
    motion=accelerometer.get_x()
    if motion>100:
        radio.send('left')
        display.show(Image.ARROW_E)
    elif motion<-100:
        radio.send('right')
        display.show(Image.ARROW_W)
    else:
        radio.send('None')
        display.show('0')
    sleep(500)