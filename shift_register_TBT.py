import RPi.GPIO as GPIO

DATA_PIN = 7
SHCP_CLOCK_PIN = 11
STCP_OUTPUT_PIN = 12

pins = [DATA_PIN, SHCP_CLOCK_PIN, STCP_OUTPUT_PIN]

# Pin layout (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)


# Initialize
def initialize():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.setup(pin, GPIO.LOW)


# Destroy
def destroy():
    for PIN in LED_PINS:
        GPIO.output(PIN, GPIO.LOW)
    GPIO.cleanup()


# Sends one bit of data via DATA_PIN
def send_data(data):
    GPIO.output(DATA_PIN, data)
    time.sleep(0.1)
    return


# Clears one bit of data from DATA_PIN
def clear_data():
    GPIO.output(DATA_PIN, 0)
    time.sleep(0.1)
    return


# Sends a clock pulse to store one bit of data in DATA_PIN
def store_bit():
    GPIO.output(SHCP_CLOCK_PIN, 1)
    time.sleep(0.1)
    GPIO.output(SHCP_CLOCK_PIN, 0)
    return


# Outputs stored bits to O/P pins
def output_stored_bit():
    GPIO.output(STCP_OUTPUT_PIN, 1)
    time.sleep(0.1)
    GPIO.output(STCP_OUTPUT_PIN, 0)
    return

"""
TODO:
1) Shifting and DeShifting bits https://www.youtube.com/watch?v=LwuzVUjXPh4
2) Daisy chaining 2 74HC595 https://www.arduino.cc/en/Tutorial/ShiftOut
"""

try:
    initialize()
    While True:
        # Forward Loop
        for i in range(8):
            send_data(1)
            store_bit()
            clear_data()
            output_stored_bit()
        # Reverse Loop
        for i in range(8):
            send_data(0)
            store_bit()
            clear_data()
            output_stored_bit()
except KeyboardInterrupt:
    destroy()
