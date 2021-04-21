i = 5
def pergunta(mensagem, tentativas = i, lembrete = 'Tente novamente!'):
    while True:
        resposta = input(mensagem)
        if resposta in ('s', 'S', 'sim', 'SIM', 'Sim'):
            return True
        if resposta in ('n', 'N', 'nao', 'NAO', 'Nao', 'não', 'Não', 'NÃO'):
            return False
        tentativas -= 1
        if tentativas <= 0:
            print('Resposta Inválida!')
            return -1
        print(lembrete)

pergunta('Você é homem? ')
