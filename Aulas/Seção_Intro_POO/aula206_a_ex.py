# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def save(self):
        return [self.name, self.age]

FILE_PATH = "Aulas\\Seção_Intro_POO\\aula206.json"

p1 = Person('Igor', 18)
p2 = Person('Duda', 20)
p3 = Person('Gabriel', 19)

people_list = [
    p1, p2, p3
]
people_list= [
    vars(person)
    for person in people_list
]

def do_dump():
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(
            people_list,
            file,
            ensure_ascii=False,
            indent=2,
        )

if __name__ == '__main__':
    print('THIS aula206_a_ex IS A MAIN')
    do_dump()
