from microbit import *
display.show(Image( "00900:"
                    "00900:"
                    "00900:"
                    "00900:"
                    "00900"))
a1=Image("90000:"
        "90000:"
        "90000:"
        "90000:"
        "90000")
a2=Image("09000:"
        "09000:"
        "09000:"
        "09000:"
        "09000")
a3=Image("00900:"
        "00900:"
        "00900:"
        "00900:"
        "00900")
a4=Image("00090:"
        "00090:"
        "00090:"
        "00090:"
        "00090")
a5=Image("00009:"
        "00009:"
        "00009:"
        "00009:"
        "00009")
a=[a1, a2, a3, a4, a5]
i=2
while 1:
    if button_a.is_pressed():
        i=i-1
    if button_b.is_pressed():
        i=i+1
    if i<=0:
        i=0
    if i>=4:
        i=4
    display.show(a[i])
    sleep(100)
