import gc
import webrepl
import network
from machine import Pin
import dht
import time


def do_connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(False)
    ap_if.active(True)
    ap_if.config(authmode=4, password="micropythoN")
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("STA network config:", sta_if.ifconfig())
    print("AP network config:", ap_if.ifconfig())


do_connect("Lee Family", "25096635")
webrepl.start(password="1111")

temp = 0
hum = 0

d = dht.DHT11(Pin(2))
while 1:
    try:
        d.measure()
    except:
        pass
    else:
        temp = d.temperature()
        hum = d.humidity()
    print('\n{}{}C'.format(temp, "\u00b0"))
    print('{}%'.format(hum))
    time.sleep(1)

gc.collect()