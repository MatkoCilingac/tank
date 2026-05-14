from machine import Pin, PWM
from config import PREDNA_LED_R, PREDNA_LED_G, PREDNA_LED_B, ZADNA_LED_R

predna_r = PWM(Pin(PREDNA_LED_R), freq=1000)
predna_g = PWM(Pin(PREDNA_LED_G), freq=1000)
predna_b = PWM(Pin(PREDNA_LED_B), freq=1000)
zadna_r = PWM(Pin(ZADNA_LED_R), freq=1000)


def nastav_jas_led(led, jas):
    jas = min(max(int(jas), 0), 255)

    pwm = int(jas * 1023 / 255)

    if led == "front":
        predna_r.duty(pwm)
        predna_g.duty(pwm)
        predna_b.duty(pwm)

    elif led == "rear":
        zadna_r.duty(pwm)


def vypni_ledky():
    predna_r.duty(0)
    predna_g.duty(0)
    predna_b.duty(0)

    zadna_r.duty(0)