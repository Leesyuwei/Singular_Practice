import network
from machine import Pin
import time


def do_connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(False)
    ap_if.active(True)
    ap_if.config(authmode=4, password="micropythoN")
    # if not sta_if.isconnected():
    #     print("connecting to network...")
    #     sta_if.active(True)
    #     sta_if.connect(ssid, password)
    #     while not sta_if.isconnected():
    #         pass
    # print("STA network config:", sta_if.ifconfig())
    print("AP network config:", ap_if.ifconfig())


#do_connect("SingularClass1", "Singular#1234")

sw = Pin(2, Pin.OUT)
ans = "1234"
sw.on()
while 1:
    pwd = input("input password")

    if pwd == ans:
        sw.off()
        time.sleep(3)
        sw.on()
    else:
        sw.on()
