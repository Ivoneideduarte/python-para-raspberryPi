nomes = ['Maria', 'Stephane', 'Yandra','Jairo','Cleilton', 'Maycon', 'Carlos', 'Marcos', 'Bianca', 'Dayane', 'Marcos Aurélio', 'Gutemberg']

for n in range( len(nomes) ):
    if nomes[n][0] == 'M':
        print(nomes[n], ' é um nome que começa com M')
        #continue
    if len(nomes[n]) == 3:
        print(nomes[n], ' possui 3 letras')
        #break