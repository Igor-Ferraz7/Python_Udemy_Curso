# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

camisetas_n = [
    ('preta', 'branca'),
    ['p', 'm', 'g'],
    {'masculino', 'feminino', 'unisex'},
    ['algodão', 'poliéster']
]

print_iter(product(*camisetas_n))
print_iter(product(*camisetas))