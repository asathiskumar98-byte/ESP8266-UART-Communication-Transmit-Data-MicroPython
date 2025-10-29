from machine import UART

import utime

uart = UART(0, baudrate=115200)

while True:
    utime.sleep_ms(2000)
    uart.write('Sathiskumar\n')
    