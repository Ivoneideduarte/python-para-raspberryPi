import RPi.GPIO as gpio
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600) # O objeto arduino contém a comunicação serial

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)

while (True):
    VALOR_RECEBIDO = arduino.readline()

    if(VALOR_RECEBIDO.decode("uft-8") < "300"):
        gpio.output(20, gpio.HIGH)
    else:
        gpio.output(20, gpio.LOW)
