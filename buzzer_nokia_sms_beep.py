import RPi.GPIO as GPIO
from time import sleep
import os

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
GPIO.setup(12, GPIO.OUT)

loop_count = 0


# define a function called morsecode
def nokia_tone():
    # Dot Dot Dot
    GPIO.output(12, GPIO.HIGH)
    sleep(.1)
    GPIO.output(12, GPIO.LOW)
    sleep(.1)
    GPIO.output(12, GPIO.HIGH)
    sleep(.1)
    GPIO.output(12, GPIO.LOW)
    sleep(.1)
    GPIO.output(12, GPIO.HIGH)
    sleep(.1)

    # Dash Dash Dash
    GPIO.output(12, GPIO.LOW)
    sleep(.2)
    GPIO.output(12, GPIO.HIGH)
    sleep(.2)
    GPIO.output(12, GPIO.LOW)
    sleep(.2)
    GPIO.output(12, GPIO.HIGH)
    sleep(.2)
    GPIO.output(12, GPIO.LOW)
    sleep(.2)
    GPIO.output(12, GPIO.HIGH)
    sleep(.2)
    GPIO.output(12, GPIO.LOW)
    sleep(.2)

    # Dot Dot Dot
    GPIO.output(12, GPIO.HIGH)
    sleep(.1)
    GPIO.output(12, GPIO.LOW)
    sleep(.1)
    GPIO.output(12, GPIO.HIGH)
    sleep(.1)
    GPIO.output(12, GPIO.LOW)
    sleep(.1)
    GPIO.output(12, GPIO.HIGH)
    sleep(.1)
    GPIO.output(12, GPIO.LOW)
    sleep(.7)


os.system('clear')
print("Morse Code")

loop_count = input("How many times would you like SOS to loop?: ")

while loop_count > 0:
    loop_count = loop_count - 1
    nokia_tone()
