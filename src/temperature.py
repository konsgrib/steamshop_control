import os
import glob
import time

import board
import busio
import digitalio
import adafruit_max31855
import RPi.GPIO as GPIO

from sensor import SensorABC


class SensorDS(SensorABC):
    def __init__(self, device_id: str) -> None:
        self.device_id = device_id
        self.device_path = "/sys/bus/w1/devices/"
        try:
            self.device_file = f"{glob.glob(self.device_path + self.device_id)[0]}/w1_slave"
        except:
            self.device_file = None

    def _read_sensor_data_raw(self):
        with open(self.device_file, "r") as f:
            lines = f.readlines()
        return lines    

    def get_data(self) -> float:
        try:
            lines = self._read_sensor_data_raw()
            while lines[0].strip()[-3:] != "YES":
                time.sleep(0.2)
                lines = self._read_sensor_data_raw()
            equals_pos = lines[1].find("t=")
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2 :]
                temp_c = round(float(temp_string) / 1000.0, 1)

                return temp_c
            else:
                return -10000
        except Exception as e:
            print(str(e))
            return -1000000
    
        
class SensorMAX(SensorABC):
    def __init__(self, pin_name) -> None:
        GPIO.setmode(GPIO.BCM)
        self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.cs = digitalio.DigitalInOut(getattr(board, pin_name))
        self.device = adafruit_max31855.MAX31855(self.spi, self.cs)

    def get_data(self):
        val = 0
        for i in range(10):
            val +=  self.device.temperature
            time.sleep(0.2)
        return val / 10

