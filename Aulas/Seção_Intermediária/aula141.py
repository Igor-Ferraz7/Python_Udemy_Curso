# fazendo um dictionary comprehension com keys e values ja criados em outro dicionario: 

products2 = { 
    'nome': 'p1', 'preco': 340,
    'nome': 'p2', 'preco': 456,
}

new_products2 = { 
    key: value for key, value in products2.items()
}

print(new_products2)

# fazendo um dictionary comprehension com keys e values ja criados em uma lista com tuplas:

lista = [
    ('key1', 'value1'),
    ('key2', 'value2') 
]

dictionary_comprehension = {
    key: value for key, value in lista
}

print(dictionary_comprehension)

# fazendo set comprehension:

set1 = set(i for i in range(10))

print(set1)