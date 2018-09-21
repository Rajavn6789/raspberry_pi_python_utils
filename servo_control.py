import RPi.GPIO as GPIO
import time

SIGNAL_PIN = 7

# Pin layout (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)

# Initialize
GPIO.setup(SIGNAL_PIN, GPIO.OUT)
GPIO.setup(SIGNAL_PIN, GPIO.LOW)


def generate_pwm_signal():
    """
    Generate a 50hz or 20ms pulse
    """
    pwm = GPIO.PWM(SIGNAL_PIN, 50)
    pwm.start(7.5)
    return pwm


try:
    while True:
        pwm = generate_pwm_signal()
        # 0 degree
        pwm.ChangeDutyCycle(7.5)
        time.sleep(2)
        # -90 degree
        pwm.ChangeDutyCycle(2.5)
        time.sleep(2)
        # +90 degree
        pwm.ChangeDutyCycle(12.5)
        time.sleep(2)
except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
