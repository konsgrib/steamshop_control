import os
import glob
import time

import board
import busio
import digitalio
import adafruit_max31855
import RPi.GPIO as GPIO

# DS18B20 sensor related code
os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")


BASE_DIR = "/sys/bus/w1/devices/"
DEVICE_FOLDER = glob.glob(BASE_DIR + "28*")[0]
DEVICE_FILE = DEVICE_FOLDER + "/w1_slave"

# max31855 related conf
SPI = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
CS = digitalio.DigitalInOut(board.D5)
MAX31855 = adafruit_max31855.MAX31855(SPI, CS)


# DS18B20 sensor related code
def read_temp_raw():
    try:
        f = open(DEVICE_FILE, "r")
        lines = f.readlines()
        f.close()
        return lines
    except:
        raise Exception(f"Pleae check if {DEVICE_FILE} exists")


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2 :]
        temp_c = float(temp_string) / 1000.0
        return temp_c


# MAX 6675 K related code
def read_max():
    GPIO.setmode(GPIO.BCM)
    SPI = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    CS = digitalio.DigitalInOut(board.D5)
    MAX31855 = adafruit_max31855.MAX31855(SPI, CS)
    val = 0
    for i in range(10):
        val += MAX31855.temperature
        time.sleep(0.2)
    return val / 10
