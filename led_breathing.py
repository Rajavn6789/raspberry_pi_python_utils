import RPi.GPIO as GPIO
import time

LED_PIN = 7

# Pin layout (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)

# Initialize
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)


def generate_pwm_signal():
    """
    Generate a 1000hz pwm signal
    Note:
    Period = 1/F = 1/1000 = 0.001 s = 1 ms
    1) Ton = 0.8ms
    Duty Cycle = Ton/Period = 0.8/1 = 0.8
    Vout = Vmax * dutyCycle = 3.3 * 0.8 = 2.64v
    2) Ton = 0.5ms
    Duty Cycle = Ton/Period = 0.5/1 = 0.5
    Vout = Vmax * dutyCycle = 3.3 * 0.5 = 1.65v
    """

    pwm = GPIO.PWM(LED_PIN, 1000)
    pwm.start(0)
    return pwm


try:
    pwm = generate_pwm_signal()
    while True:
        # Increase duty cycle: 0~100 by 4 each step
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(0.5)
        # Increase duty cycle: 100~0 by -4 each step
        for dc in range(100, -1, -5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(0.5)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
