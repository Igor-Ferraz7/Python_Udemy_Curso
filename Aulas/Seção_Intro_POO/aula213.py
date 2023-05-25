# setter -> metodo que configura o valor de um atributo qualquer.
# getter -> método que obtêm (mas não salva) determinado valor de um atributo qualquer.

class Pen:
    def __init__(self, color):
        # self.color = color
        self._color = color
    
    @property # Obter o valor
    def color(self):
        return self._color
    
    @color.setter # Configurar o valor
    def color(self, color):
        self._color = color

P1 = Pen('Blue')
P1.color = 'Pink'
print(P1.color)