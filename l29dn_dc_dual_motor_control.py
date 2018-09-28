import RPi.GPIO as GPIO
from time import sleep

# Motor A
EN_A_PIN = 12  # pwm support
INPUT1_PIN = 13
INPUT2_PIN = 15

# Motor B
EN_B_PIN = 32  # pwm support
INPUT3_PIN = 31
INPUT4_PIN = 33

# Pin layout (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)

# Initialize
GPIO.setup(EN_A_PIN, GPIO.OUT)
GPIO.setup(INPUT1_PIN, GPIO.OUT)
GPIO.setup(INPUT2_PIN, GPIO.OUT)

GPIO.setup(EN_B_PIN, GPIO.OUT)
GPIO.setup(INPUT3_PIN, GPIO.OUT)
GPIO.setup(INPUT4_PIN, GPIO.OUT)

GPIO.setup(EN_A_PIN, GPIO.LOW)
GPIO.setup(INPUT1_PIN, GPIO.LOW)
GPIO.setup(INPUT2_PIN, GPIO.LOW)

GPIO.setup(EN_B_PIN, GPIO.LOW)
GPIO.setup(INPUT3_PIN, GPIO.LOW)
GPIO.setup(INPUT4_PIN, GPIO.LOW)


def generate_pwm1_signal():
    pwm1 = GPIO.PWM(EN_A_PIN, 1000)
    pwm1.start(50)
    return pwm1


def generate_pwm2_signal():
    pwm2 = GPIO.PWM(EN_B_PIN, 1000)
    pwm2.start(50)
    return pwm2


def forward():
    GPIO.output(INPUT1_PIN, GPIO.HIGH)
    GPIO.output(INPUT2_PIN, GPIO.LOW)
    GPIO.output(INPUT3_PIN, GPIO.HIGH)
    GPIO.output(INPUT4_PIN, GPIO.LOW)
    print("forwarding")
    return


def reverse():
    GPIO.output(INPUT1_PIN, GPIO.LOW)
    GPIO.output(INPUT2_PIN, GPIO.HIGH)
    GPIO.output(INPUT3_PIN, GPIO.LOW)
    GPIO.output(INPUT4_PIN, GPIO.HIGH)
    print("reversing")
    return


def stop():
    GPIO.output(INPUT1_PIN, GPIO.LOW)
    GPIO.output(INPUT2_PIN, GPIO.LOW)
    GPIO.output(INPUT3_PIN, GPIO.LOW)
    GPIO.output(INPUT4_PIN, GPIO.LOW)
    print("stopped")
    return


try:
    pwm1 = generate_pwm1_signal()
    pwm2 = generate_pwm2_signal()
    while True:
        # Move Forward
        forward()
        sleep(2)
        stop()
        # Move Reverse
        reverse()
        sleep(2)
        stop()
except KeyboardInterrupt:
        pwm1.stop()
        pwm2.stop()
        stop()
        GPIO.cleanup()
