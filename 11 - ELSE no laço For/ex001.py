nomes = ['Maria', 'Stephane', 'Yandra','Jairo','Cleilton', 'Maycon', 'Carlos', 'Marcos', 'Bianca', 'Dayane', 'Marcos Aurélio', 'Gutemberg']

contador = 0
for nome in nomes:
    if nome[0] == 'M':
        print(nome)
        contador += 1
    if contador > 10:
        break
else:
    print('*** FIM DA LISTA ***')