from microbit import *
import radio
radio.config(channel=7)
radio.on()

class servo:
    def __init__(self,pin):
        self.degree=0
        self.pin=pin
        self.pin.set_analog_period(20)
        self.angle(0)

    def angle(self,idegree=None):
        if idegree==None:
            self.degree=0
        else:
            self.degree=idegree

        self.pin.write_analog(int((0.5+(self.degree/90))*(1023/20)))

servo1=servo(pin0)
while 1:
    motion=radio.receive()
    if motion=='left':
        display.show(Image.ARROW_E)
        servo1.angle(45)
    elif motion=='right':
        display.show(Image.ARROW_W)
        servo1.angle(135)
    else:
        display.show('0')
        servo1.angle(90)
    sleep(500)