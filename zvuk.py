from machine import UART

uart = UART(2, baudrate=9600, tx=19, rx=13)

def vystrel():
    # prehrá skladbu č.1 (napr. 0001.mp3)
    cmd = 0x07
    data = 1
    checksum = (cmd + data) & 0xFF
    uart.write(bytearray([0xAA, cmd, data, checksum]))