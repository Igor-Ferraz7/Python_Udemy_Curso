"""
Da aula 119:
--> Chaves em dicts podem ser apenas valores imutáveis:
-> (str, int, float, bool, tuple e etc.)
Da aula 121:
"""
person = {
    'Nome': 'Igor',
    'Idade': 18
}

print(person, '\n')
print(person.items(), '\n')

test = person.items()

for item in person.items():
    print(item)

person.setdefault('senha', None)

print(person)