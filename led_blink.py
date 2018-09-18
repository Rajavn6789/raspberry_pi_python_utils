import RPi.GPIO as GPIO
import time

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
GPIO.setup(7, GPIO.OUT)

for x in range(0, 3):
    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)

GPIO.cleanup()
