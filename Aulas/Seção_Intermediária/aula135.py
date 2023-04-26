person = {
    'Nome': 'Igor',
    'Idade': 18
}

second_person = {
    'nome': 'Duda',
    'idade': 20
}

people = {**person, **second_person}
print(people)

def test(*args, **kwargs):
    print(f'Unnamed arguments: {args}')
    print(kwargs)
    for key, value in kwargs.items():
        print(f'Key: {key}\nValue: {value}')

test(2, 4, 'ola', **person)