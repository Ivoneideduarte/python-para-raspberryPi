'''
def adicionaLista(valor, lista=[]): # Mantém a lista como valor padrão
    lista.append(valor)
    return lista
'''

def adicionaLista(valor, lista=None):
    if lista == None:
        lista = [] # Limpa a lista
        lista.append(valor)
        return lista

print(adicionaLista(7))