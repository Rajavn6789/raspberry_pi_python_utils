import RPi.GPIO as GPIO
import time

# use board layout for pin numbers
GPIO.setmode(GPIO.BOARD)

# set output pins
segments = (7, 11, 12, 13, 15, 16, 18, 22)

# segments state for displaying different digits
digits = {
    '0': (1, 1, 1, 1, 1, 1, 0, 0),
    '1': (0, 1, 1, 0, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1, 0),
    '3': (1, 1, 1, 1, 0, 0, 1, 0),
    '4': (0, 1, 1, 0, 0, 1, 1, 0),
    '5': (1, 0, 1, 1, 0, 1, 1, 0),
    '6': (1, 0, 1, 1, 1, 1, 1, 0),
    '7': (1, 1, 1, 0, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1, 0),
    '9': (1, 1, 1, 1, 0, 1, 1, 0)
}


# initialize GPIO pins
def init():
    for segment in segments:
        GPIO.setup(segment, GPIO.OUT)
        GPIO.output(segment, 0)


# dot_segment_blink
def dot_segment_blink(num=3):
    for x in range(num):
        for x in range(3):
            GPIO.output(22, True)
            time.sleep(0.1)
            GPIO.output(22, False)
            time.sleep(0.1)
        time.sleep(0.6)
    time.sleep(1)


# turns off all GPIO pins
def reset_segments():
    for segment in segments:
        GPIO.output(segment, 0)


# test connection of all LED segments
def led_segments_check():
    for segment in segments:
        GPIO.output(segment, True)
        time.sleep(0.5)
        GPIO.output(segment, False)
    time.sleep(1)


# countdown timer
def count_down_timer():
    for key in sorted(digits.iterkeys(), reverse=True):
        segIndex = 0
        for segment in segments:
            GPIO.output(segment, digits[key][segIndex])
            segIndex += 1
        time.sleep(1)
    reset_segments()  # reset before displaying next digit


# init
init()

# test all led segments
dot_segment_blink(1)
led_segments_check()

# count down timer
dot_segment_blink(1)
count_down_timer()
dot_segment_blink(1)

GPIO.cleanup()
