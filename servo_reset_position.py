import RPi.GPIO as GPIO
import time

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
GPIO.setup(7, GPIO.OUT)

try:
    while True:
        GPIO.output(7, True)
        time.sleep(0.0015)
        GPIO.output(7, False)
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
