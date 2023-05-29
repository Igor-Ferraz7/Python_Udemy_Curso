# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self.name = name
        self.manufacturer = None
        self.motor = None
    
    @property
    def set_manufacturer(self):
        return self.manufacturer
    
    @set_manufacturer.setter
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    
    @property
    def set_motor(self):
        return self.motor
    
    @set_motor.setter
    def set_motor(self, motor):
        self.motor = motor

class Manufacturer:
    def __init__(self, name):
        self.name = name

class Motor:
    def __init__(self, name):
        self.name = name

volkswagen = Manufacturer('Volkswagen')
fiat = Manufacturer('Fiat')
ford = Manufacturer('Ford')

motor_10 = Motor(1.0)

fusca = Car('Fusca')
fusca.set_manufacturer = volkswagen.name
fusca.set_motor = motor_10.name

uno = Car('Uno')


print(fusca.name, fusca.manufacturer, fusca.motor)