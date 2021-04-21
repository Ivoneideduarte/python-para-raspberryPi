#IMPORTA BIBLIOTECA PARA CONTROLAR GPIOS
import RPi.GPIO as gpio

#DEFINE PADRÃO DE NUMERAÇÃO DE PORTAS
gpio.setmode(gpio.BCM)

#FUNÇÃO PARA DEFINIR O MODO DAS PORTAS
def pinMode(*portas, modo):
    for porta in portas:
        gpio.setup(porta, modo)

#FUNÇÃO PARA LIGAR OU DESLIGAR AS PORTAS
def digitalWrite(*portas, nivel):
    for porta in portas:
        gpio.output(porta, nivel)

#DEFINE AS PORTAS EM MODO OUTPUT
pinMode(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27, modo=gpio.OUT)

#EXEMPLO
digitalWrite(12, 15, 20, 21, 5, 6, nivel=gpio.HIGH)
digitalWrite(12, 15, 20, 21, 5, 6, nivel=gpio.LOW)