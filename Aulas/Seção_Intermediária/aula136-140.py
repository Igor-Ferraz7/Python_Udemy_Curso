import pprint

products = [
    {'nome': 'p1', 'preco': 340},
    {'nome': 'p2', 'preco': 456},
]

new_products = [
    {**product, 'preco': product['preco'] * 2}
    if product['preco'] < 400 else {**product} # o que vier ANTES do for é MAPEAMENTO
    for product in products 
    if product['preco'] > 400 # o que vier DEPOIS do for é FILTRO
]


pprint.pprint(new_products, sort_dicts=False, width=40)