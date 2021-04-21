# Importação dos pacotes
import RPi.GPIO as gpio
from time import sleep

# Configuração da forma de endereço dos pinos
gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.OUT)    # Definindo a porta 5 como saída
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)

for x in range(1, 10): # Faz o LED piscar 10 vezes
    # Define as portas como ligadas ou desligadas
    gpio.output(5, gpio.HIGH)
    gpio.output(6, gpio.LOW)
    gpio.output(13, gpio.LOW)
    sleep(0.5)
    gpio.output(5, gpio.LOW)
    gpio.output(6, gpio.HIGH)
    gpio.output(13, gpio.LOW)
    sleep(0.5)
    gpio.output(5, gpio.LOW)
    gpio.output(6, gpio.LOW)
    gpio.output(13, gpio.HIGH)
    sleep(0.5)

# Depois que o programa termina é necessário desligar as configurações da gpio
gpio.cleanup()