citys_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_list = ['BA', 'SP', 'MG', 'RJ']

# Podemos fazer:

def lists_union(l1, l2):
    min_range = min(len(l1), len(l2))

    return [(l1[index], l2[index]) for index in range(min_range)]

print(lists_union(citys_list, states_list))

# Ou podemos simplismnete fazer:

print(list(zip(citys_list, states_list)))