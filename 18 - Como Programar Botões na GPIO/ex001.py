# Importação dos pacotes
import RPi.GPIO as gpio
from time import sleep

# Configuração da forma de endereço dos pinos
gpio.setmode(gpio.BCM)  # Número fixo de cada porta

gpio.setup(5, gpio.OUT) # Definindo a porta 5 como OUTPUT
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)

gpio.setup(23, gpio.IN, gpio.PUD_UP) # Definindo a porta 23 como INPUT_PULL_UP
gpio.setup(24, gpio.IN, gpio.PUD_UP) # Definindo a porta 24 como INPUT_PULL_UP
gpio.setup(25, gpio.IN, gpio.PUD_DOWN) # Definindo a porta 25 como INPUT_PULL_DOWN

while True: # Função de Loop
    if gpio.input(23) == gpio.LOW: # Verifica o estado do botão e se estiver igual a desligado, desliga o LED
        gpio.output(5, gpio.LOW) # Desliga o LED
    else:
        gpio.output(5, gpio.HIGH)

    if gpio.input(24) == gpio.LOW:
        gpio.output(5, gpio.HIGH)
    else:
        gpio.output(5, gpio.LOW)

    gpio.output(13, gpio.input(25))

# Depois que o programa termina é necessário desligar as configurações da gpio
gpio.cleanup()