# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

citys_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_list = ['BA', 'SP', 'MG', 'RJ']

def zipper(*args):
    args_list = iter(list(args))

    for lista in args_list:
        try:
            prox_list = next(args_list)
            if len(lista) < len(prox_list):
                shorter_list = lista
                biggest_list = prox_list
            else:
                shorter_list = prox_list
                biggest_list = lista
        except StopIteration:
            break

# Com ajuda da resolução:
    list_union = [
        (shorter_list[i], biggest_list[i])
        for i in range(len(shorter_list))
    ]

# Sem ajuda: 
    for c in range(len(shorter_list)):
        shorter_list[c] = (shorter_list[c], biggest_list[c])

    return shorter_list


print(zipper(states_list, citys_list))