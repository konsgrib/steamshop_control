from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.brightness = 70
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('imageMAX_BR.jpg')
camera.stop_preview()