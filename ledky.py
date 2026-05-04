from machine import Pin
import neopixel
from config import PREDNA_RGB_PIN, ZADNA_RGB_PIN, POCET_LED

predna_rgb_pin = Pin(PREDNA_RGB_PIN, Pin.OUT)
zadna_rgb_pin = Pin(ZADNA_RGB_PIN, Pin.OUT)

predna_led_matica = neopixel.NeoPixel(predna_rgb_pin, POCET_LED)
zadna_led_matica = neopixel.NeoPixel(zadna_rgb_pin, POCET_LED)


def nastav_jas_led(led, jas):
    jas = min(max(jas, 0), 255)

    if led == "front":
        for i in range(POCET_LED):
            predna_led_matica[i] = (jas, jas, jas)
        predna_led_matica.write()

    elif led == "rear":
        for i in range(POCET_LED):
            zadna_led_matica[i] = (jas, 0, 0)
        zadna_led_matica.write()


def vypni_ledky():
    for i in range(POCET_LED):
        predna_led_matica[i] = (0, 0, 0)
        zadna_led_matica[i] = (0, 0, 0)

    predna_led_matica.write()
    zadna_led_matica.write()