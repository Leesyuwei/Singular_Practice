from microbit import *
while 1:
    temp=temperature()
    display.show(temp)
    sleep(500)