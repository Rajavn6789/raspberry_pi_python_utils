import RPi.GPIO as GPIO
import time

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
GPIO.setup(12, GPIO.OUT)

for x in range(0, 3):
    GPIO.output(12, True)
    time.sleep(0.3)
    GPIO.output(12, False)
    time.sleep(0.3)

GPIO.cleanup()
