#tuplas são listas imutáveis

lista = ['a', 'b', 'c', 'd']
lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

for item in lista_enumerada:
    print(item) # não é executado pois a lista ja foi "consumida"
tst = list(enumerate(lista))
print(tst)