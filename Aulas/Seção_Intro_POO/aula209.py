# Execuandi ideias
import random
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def create_random_person(cls):
        name_in_def = random.choice(people_list)
        age_in_def = random.randint(1, 100)
        return cls(name_in_def, age_in_def)
    
people_list = ['Igor', 'Ana', 'Duda', 'Gabriel', 'Joao', 'Isaque', 'Thiago']

p1 = Person.create_random_person()
print(p1.name, p1.age)