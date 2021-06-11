from machine import Pin
import dht
import time

d = dht.DHT11(Pin(2))

while 1:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(temp, '\u00b0', 'C')
    print(hum, "%\n")
    time.sleep(1)