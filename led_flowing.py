import RPi.GPIO as GPIO
import time

LED_PINS = [7, 11, 12, 13]

# Pin layout (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)


# Initialize
def initialize():
    for PIN in LED_PINS:
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.LOW)


# Destroy
def destroy():
    for PIN in LED_PINS:
        GPIO.output(PIN, GPIO.LOW)
    GPIO.cleanup()


def loop():
    while True:
        # Forward flow
        for PIN in LED_PINS:
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(PIN, GPIO.LOW)
        time.sleep(1)
        # Reverse flow
        for PIN in reversed(LED_PINS):
            GPIO.output(PIN, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(PIN, GPIO.LOW)
        time.sleep(1)


try:
    initialize()
    loop()
except KeyboardInterrupt:
    destroy()
