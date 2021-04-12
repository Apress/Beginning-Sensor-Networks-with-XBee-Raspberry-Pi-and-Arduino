#
# Beginning Sensor Networks 2nd Edition
# 
# XBee Sensor Node Example: Reading a BMP280 sensor.
# This demonstrates how to use an I2C driver. 
#
# Dr. Charles Bell
#
from machine import I2C
from bmp280 import BMP280
from time import sleep

import xbee

# BMP280 address
BMP_ADDR = 0x77
# Target address to send data
TARGET_64BIT_ADDR = b'\x00\x13\xA2\x00\x40\x8C\xCD\x0F'
wait_time = 15 # seconds between measurements
cycles = 10 # number of repeats 
bmp280 = BMP280(I2C(1, freq=100000), BMP_ADDR)

for x in range(cycles):
    # Read temperature & baraometric pressure
    temp_c = bmp280.temperature
    pressure = bmp280.pressure

    # Convert temperature to proper units
    print("Temperature: %.2f Celsius" % temp_c)
    temp_f = (temp_c * 9.0 / 5.0) + 32.0
    print("Temperature: %.2f Fahrenheit" % temp_f)
    print("Barometric Pressure: %.4f" % pressure)

    # Send data to coordinator
    message = "C: %.2f, F: %.2f, B: %.4f" % (temp_c, temp_f, pressure)
    print("Sending: %s" % message)
    try:
        xbee.transmit(TARGET_64BIT_ADDR, message)
        print("Data sent successfully")
    except Exception as e:
        print("Transmit failure: %s" % str(e))
    
    # Wait between cycles
    sleep(wait_time)
    
