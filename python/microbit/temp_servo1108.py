from microbit import *
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
    temp=temperature()
    display.show(temp)
    servo1.angle((temp-15)*6)
    sleep(500)