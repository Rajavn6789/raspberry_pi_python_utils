import RPi.GPIO as GPIO
import time

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
GPIO.setup(7, GPIO.OUT)

# setup PWM
p = GPIO.PWM(7, 50)

# start PWM
p.start(7.5)

try:
    while True:
        # neutral
        p.ChangeDutyCycle(7.5)
        time.sleep(3)
        # -90 degree
        p.ChangeDutyCycle(2.5)
        time.sleep(3)
        # +90 degree
        p.ChangeDutyCycle(12.5)
        time.sleep(3)
except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
