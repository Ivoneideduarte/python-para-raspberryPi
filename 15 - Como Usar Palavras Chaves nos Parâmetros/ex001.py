cores = ['0 - Não informada', '1 - Vermelho', '2 - Amarelo', '3 - Laranja', '4 - Verde', '5 - Azul', '6 - Branca']
tensoes = [0, 1.8, 1.8, 1.8, 2, 2.5, 2.5]

def resistorLED(tensaoCircuito, tensaoLED = 0, corLED = 0, corrente = 20):
    print('Tensão de alimentação: {}Volts'.format(tensaoCircuito))
    if(tensaoLED == 0):
        if(corLED == 0):
            tensaoLED = 1.8
        else:
            tensaoLED = tensoes[corLED]
    print('Tensão do LED: {}Volts'.format(tensaoLED))
    print('Cor do LED: {}'.format(cores[corLED]))
    print('Corrente Limite para o LED: {}mA (Miliamperes)'.format(corrente))
    print('Resistor Calculado: {}Ohms'.format((tensaoCircuito - tensaoLED)/(corrente/1000)))
print(resistorLED(tensaoCircuito = 5, tensaoLED = 2, corLED=1))
