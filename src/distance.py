import RPi.GPIO as GPIO
import time
import signal
import sys

from sensor import SensorABC

class SensorSonar(SensorABC):
    def __init__(self, pin_trigger: int, pin_echo: int) -> None:
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)

    def get_data(self):
        GPIO.output(self.pin_trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pin_trigger, False)
        while 0 == GPIO.input(self.pin_echo):
            start_time = time.time()
        while 1 == GPIO.input(self.pin_echo):
            stop_time = time.time()        
        
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2
        return int(distance)