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
    def __init__(self, name) -> None:
        self.name = name
        self._motor = None
        self._manufacturer = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer


class Motor:
    def __init__(self, name) -> None:
        self.name = name
        

class Manufacturer:
    def __init__(self, name) -> None:
        self.name = name


volkswagem = Manufacturer("Volkswagem")
fiat = Manufacturer("Fiat")

motor2_0 = Motor("Motor 2.0")
motor3_0 = Motor("Motor 3.0")

fusca = Car("Fusca")
fusca.motor = motor2_0
fusca.manufacturer = volkswagem

uno = Car("Uno")
uno.motor = motor3_0
uno.manufacturer = fiat

for car in [fusca, uno]:
    print(car.name, car.motor.name, car.manufacturer.name)
