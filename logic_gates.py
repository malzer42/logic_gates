"""
Author(s): Pierre Abraham Mulamba
Date of creation (modification): 2020.03.10 (2020.03.10)

"""
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

leds = {'red': 37, 'green': 15, 'yellow': 13, 'white': 11}
buttons = {'button1': 33, 'button2': 18}
buttonStates = {'button1State': False, 'button2State': False}
ledStates = {'redLedState': False, 'yellowLedState': False, 'greenLedState': False, 'whiteLedState': False}

[GPIO.setup(led, GPIO.OUT) for led in leds.values()]
[GPIO.setup(button, GPIO.IN) for button in buttons.values()]

try:
    while True:

        if GPIO.input(buttons['button1']):
            buttonStates['button1State'] = True
        else:
            buttonStates['button1State'] = False

        if GPIO.input(buttons['button2']):
            buttonStates['button2State'] = True
        else:
            buttonStates['button2State'] = False

        ledStates['redLedState'] = buttonStates['button1State'] and buttonStates['button2State']
        ledStates['yellowLedState'] = buttonStates['button1State'] or buttonStates['button2State']
        ledStates['whiteLedState'] = not buttonStates['button1State'] and not buttonStates['button2State']
        # ledStates['greenLedState'] = not buttonStates['button1State'] or buttonStates['button2State']
        ledStates['greenLedState'] = (buttonStates['button1State'] and not buttonStates['button2State']) or \
                                     (not buttonStates['button1State'] and buttonStates['button2State'])
        GPIO.output(leds['red'], ledStates['redLedState'])
        GPIO.output(leds['yellow'], ledStates['yellowLedState'])
        GPIO.output(leds['white'], ledStates['whiteLedState'])
        GPIO.output(leds['green'], ledStates['greenLedState'])

        buttonStates['button1State'] = False
        buttonStates['button2State'] = False
except KeyboardInterrupt as keyboard_interrupt:
    print(f"{keyboard_interrupt} \n")
except Exception as exception:
    print(f"Unknown Exceptions Occurred! - {exception}")
finally:
    GPIO.cleanup()
