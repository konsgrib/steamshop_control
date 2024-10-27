import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 18
pinEcho = 24


def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, close)

# # set GPIO input and output channels
# GPIO.setup(pinTrigger, GPIO.OUT)
# GPIO.setup(pinEcho, GPIO.IN)

# while True:
# 	# set Trigger to HIGH
# 	GPIO.output(pinTrigger, True)
# 	# set Trigger after 0.01ms to LOW
# 	time.sleep(0.00001)
# 	GPIO.output(pinTrigger, False)

# 	startTime = time.time()
# 	stopTime = time.time()

# 	# save start time
# 	while 0 == GPIO.input(pinEcho):
# 		startTime = time.time()

# 	# save time of arrival
# 	while 1 == GPIO.input(pinEcho):
# 		stopTime = time.time()

# 	# time difference between start and arrival
# 	TimeElapsed = stopTime - startTime
# 	# multiply with the sonic speed (34300 cm/s)
# 	# and divide by 2, because there and back
# 	distance = (TimeElapsed * 34300) / 2

# 	print ("Distance: %.1f cm" % distance)
# 	time.sleep(1)


# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


# set Trigger to HIGH
GPIO.output(pinTrigger, True)
# set Trigger after 0.01ms to LOW
time.sleep(0.00001)
GPIO.output(pinTrigger, False)


def get_distance_2():
    print("Start...")

    startTime = time.time()
    stopTime = time.time()
    cnt_distance = 0
    cnt = 0
    print("Start loop...")
    for i in range(5):
        print("Start", i)
        # save start time
        while 0 == GPIO.input(pinEcho):
            startTime = time.time()

        # save time of arrival
        while 1 == GPIO.input(pinEcho):
            stopTime = time.time()
        # GPIO.cleanup()
        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        print(distance)
        if distance < 2000:
            print(distance)
            cnt_distance += distance
            cnt += 1
    print("Stop...")
    GPIO.cleanup()
    # print ("Distance: %.1f cm" % distance)
    distance = distance / cnt
    print("Distance: %.1f cm" % distance)
    return int(distance)
