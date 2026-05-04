from machine import Pin, PWM
from config import *

lavy_motor_in1 = Pin(LAVY_MOTOR_IN1, Pin.OUT)
lavy_motor_in2 = Pin(LAVY_MOTOR_IN2, Pin.OUT)
lavy_enb = PWM(Pin(LAVY_ENB), freq=1000)

pravy_motor_in1 = Pin(PRAVY_MOTOR_IN1, Pin.OUT)
pravy_motor_in2 = Pin(PRAVY_MOTOR_IN2, Pin.OUT)
pravy_enb = PWM(Pin(PRAVY_ENB), freq=1000)

otocny_motor_in1 = Pin(OTOCNY_MOTOR_IN1, Pin.OUT)
otocny_motor_in2 = Pin(OTOCNY_MOTOR_IN2, Pin.OUT)
otocny_motor_enb = PWM(Pin(OTOCNY_MOTOR_ENB), freq=1000)


def vypni_motory():
    lavy_motor_in1.off()
    lavy_motor_in2.off()
    pravy_motor_in1.off()
    pravy_motor_in2.off()

    otocny_motor_in1.off()
    otocny_motor_in2.off()

    lavy_enb.duty(0)
    pravy_enb.duty(0)
    otocny_motor_enb.duty(0)


def otacanie_tanku(value):
    rychlost = min(abs(value), 1023)

    if value > 0:
        lavy_motor_in1.on()
        lavy_motor_in2.off()
        pravy_motor_in1.off()
        pravy_motor_in2.on()
    elif value < 0:
        lavy_motor_in1.off()
        lavy_motor_in2.on()
        pravy_motor_in1.on()
        pravy_motor_in2.off()
    else:
        lavy_motor_in1.off()
        lavy_motor_in2.off()
        pravy_motor_in1.off()
        pravy_motor_in2.off()

    lavy_enb.duty(rychlost)
    pravy_enb.duty(rychlost)


def dopredu_dozadu(value):
    rychlost = min(abs(value), 1023)

    if value > 0:
        lavy_motor_in1.on()
        lavy_motor_in2.off()
        pravy_motor_in1.on()
        pravy_motor_in2.off()
    elif value < 0:
        lavy_motor_in1.off()
        lavy_motor_in2.on()
        pravy_motor_in1.off()
        pravy_motor_in2.on()
    else:
        lavy_motor_in1.off()
        lavy_motor_in2.off()
        pravy_motor_in1.off()
        pravy_motor_in2.off()

    lavy_enb.duty(rychlost)
    pravy_enb.duty(rychlost)


def otacanie_hlavy(rychlost, smer):
    rychlost = min(abs(rychlost), 1023)
    otocny_motor_enb.duty(rychlost)

    if smer == "left":
        otocny_motor_in1.on()
        otocny_motor_in2.off()
    elif smer == "right":
        otocny_motor_in1.off()
        otocny_motor_in2.on()
    else:
        otocny_motor_in1.off()
        otocny_motor_in2.off()
        otocny_motor_enb.duty(0)