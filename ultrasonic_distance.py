import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# Set GPIO Pins
BUZZER_PIN = 7
TRIGGER_PIN = 11
ECHO_PIN = 12

# Set GPIO direction (IN / OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Initialize Pins
GPIO.output(BUZZER_PIN, GPIO.LOW)
GPIO.output(TRIGGER_PIN, GPIO.LOW)


def warn_buzzer():
    "Actvates buzzer by setting BUZZER_PIN on and off"

    GPIO.output(BUZZER_PIN, True)
    time.sleep(0.3)
    GPIO.output(BUZZER_PIN, False)
    time.sleep(0.1)


def calculate_distance():
    """
    Calculates distance based on time difference

    Note:
    Speed of sound is 34,000 cm/s or 340 m/s
    velocity = 2d / time

    Returns:
    distance in cm.
    """

    # Shoot Ultrasonic signal
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    # Calculate Time
    startTime = 0
    endTime = 0
    while GPIO.input(ECHO_PIN) == 0:
        startTime = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        endTime = time.time()

    # Calculate Distance
    timeElapsed = endTime - startTime
    distance = (34300 * timeElapsed) / 2
    return distance


try:
    while True:
        distance = calculate_distance()
        print("Measured Distance = %.1f cm" % distance)
        if distance < 5:
            warn_buzzer()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
