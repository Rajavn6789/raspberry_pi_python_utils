import RPi.GPIO as GPIO
import time

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
ControlPins = [7, 11, 13, 15]

for pin in ControlPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

seg = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
       ]

try:
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPins[pin], seg[halfstep][pin])
            time.sleep(0.001)
except KeyboardInterrupt:
        GPIO.cleanup()
