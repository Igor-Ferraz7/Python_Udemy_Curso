# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import pprint, copy
products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

increased_products = copy.deepcopy(products)

# increased_products = [
#     copy.deepcopy(product)
#     for product in increased_products
# ]

increased_products = [
    {**product, 'preco': product['preco'] * 1.1}
    for product in increased_products
]

pprint.pprint(increased_products)
print()


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

sorted_products_by_name = copy.deepcopy(increased_products)
sorted_products_by_name = sorted(sorted_products_by_name, reverse=True, key= lambda dict: dict['nome'])

pprint.pprint(sorted_products_by_name)
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

sorted_products_by_price = copy.deepcopy(increased_products)
sorted_products_by_price = sorted(sorted_products_by_price, key= lambda dict: dict['preco'])

pprint.pprint(sorted_products_by_price)