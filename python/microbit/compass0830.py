from microbit import *
N=Image("00900:"
        "00900:"
        "00900:"
        "09990:"
        "00900")
E=Image("00000:"
        "00090:"
        "99999:"
        "00090:"
        "00000")
S=Image("00900:"
        "09990:"
        "00900:"
        "00900:"
        "00900")
W=Image("00000:"
        "09000:"
        "99999:"
        "09000:"
        "00000")
compass.calibrate()
while 1:
    A=compass.heading()
    if A<45:
        display.show(N)
    elif A<135:
        display.show(E)
    elif A<225:
        display.show(S)
    elif A<315:
        display.show(W)
    else:
        display.show(N)