import network
from config import WIFI_NAZOV, WIFI_HESLO

def spusti_wifi():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(
        essid=WIFI_NAZOV,
        password=WIFI_HESLO,
        channel=1,
        authmode=network.AUTH_WPA_WPA2_PSK
    )

    while not ap.active():
        pass

    print("Wi-Fi AP spustený")
    print("IP adresa:", ap.ifconfig()[0])

    return ap