import RPi.GPIO as gpio
from time import sleep

arduino = serial.Serial('/dev/ttyACM0', 9600)

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)

for x in range(1, 10):
    gpio.output(20, gpio.HIGH)
    arduino.write(b'0')
    sleep(0.5)
    gpio.output(20, gpio.LOW)
    arduino.write(b'1')
    sleep(0.5)

gpio.cleanup()
