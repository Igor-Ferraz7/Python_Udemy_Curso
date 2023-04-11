lista = ['teste 1', 'teste 2']
lista.insert(0, 'ola') #insere e move o resto
lista[0] = 'teste 0' #substitui
print(lista)

lista_a = [1, 2, 3, 4]
lista_b = lista_a #ela se conecta com a lista_a
lista_c = lista_a.copy() #copia a lista
