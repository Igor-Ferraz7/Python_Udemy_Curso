import pprint, copy
products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

increased_products = [
    {**product, 'preco': round(product['preco'] * 1.1, 2)}
    for product in copy.deepcopy(products)
]

pprint.pprint(products)
print()
pprint.pprint(increased_products)
print()


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

sorted_products_by_name = sorted(
    copy.deepcopy(increased_products),
    reverse=True,
    key= lambda dict: dict['nome']
    )

pprint.pprint(sorted_products_by_name)
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

sorted_products_by_price = sorted(
    copy.deepcopy(increased_products),
    key= lambda dict: dict['preco']
    )

pprint.pprint(sorted_products_by_price)