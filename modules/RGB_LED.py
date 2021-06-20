import RPi.GPIO as GPIO

# The pins are on GPIO format
redPin = 12
greenPin = 19
bluePin = 13


def blink(pin):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn():
    blink(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)

'''
def main(cmd):
    while True:
        if cmd == "red on":
            return redOn()
        elif cmd == "red off":
            return redOff()
        elif cmd == "green on":
            return greenOn()
        elif cmd == "green off":
            return greenOff()
        elif cmd == "blue on":
            return blueOn()
        elif cmd == "blue off":
            return blueOff()
        elif cmd == "yellow on":
            return yellowOn()
        elif cmd == "yellow off":
            return yellowOff()
        elif cmd == "cyan on":
            return cyanOn()
        elif cmd == "cyan off":
            return cyanOff()
        elif cmd == "magenta on":
            return magentaOn()
        elif cmd == "magenta off":
            return magentaOff()
        elif cmd == "white on":
            return whiteOn()
        elif cmd == "white off":
            return whiteOff()
        else:
            return ("Not a valid command")

main("red on")
'''