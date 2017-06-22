from flask import Flask, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
DEMO_LED_PIN = 11


def turn_on():
    GPIO.output(DEMO_LED_PIN, GPIO.LOW)
    return "LED ON"


def turn_off():
    GPIO.output(DEMO_LED_PIN, GPIO.HIGH)
    return "LED OFF"


def blink():
    return "BLINK"


@app.route('/raspberry')
def raspberry():
    paras = request.args
    led_demo = paras.get("led")
    if led_demo == "on":
        return turn_on()
    elif led_demo == "off":
        return turn_off()
    elif led_demo == "blink":
        return blink()
    return 'ok'


@app.route('/')
def led_control():
    qs = request.args
    print(qs.get("led"))
    if qs.get("led") == "on":
        return "light_on"
    else:
        return "light_off"


def init_raspberry():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DEMO_LED_PIN, GPIO.OUT)


if __name__ == '__main__':
    init_raspberry()
    app.run(host="0.0.0.0", debug=True, port=80)
