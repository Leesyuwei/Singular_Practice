import network


def connect():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(False)
    ap_if.active(True)
    ap_if.config(authmode=4, password="micropythoN")
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect("SingularClass1", "Singular#1234")
        while not sta_if.isconnected():
            pass
    print("STA network config:", sta_if.ifconfig())
    print("AP network config", ap_if.ifconfig())


connect()