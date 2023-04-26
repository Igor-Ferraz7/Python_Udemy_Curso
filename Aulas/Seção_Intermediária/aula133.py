lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

def exibir(lista_ordenada):
    for item in lista_ordenada:
        print(item)

lista1 = sorted(lista, key= lambda item: item['nome'])
lista2 = sorted(lista, key= lambda item: item['sobrenome'])

exibir(lista1)
print()
exibir(lista2)