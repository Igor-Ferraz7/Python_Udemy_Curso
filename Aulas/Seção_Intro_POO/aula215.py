# Associação: USAR outra classe/objeto
# Nele, um atributo da classe se comunica/relaciona com outra classe.
class Writer:
    def __init__(self) -> None:
        self._tool = None # Atributo que se relaciona com a classe "Tools"
    
    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool):
        self._tool = tool # Atributo recebendo o objeto instanciado da classe "Tools"

class Tools:
    def __init__(self, name) -> None:
        self.name = name

    def write(self):
        return f'{self.name} is writing.'

w1 = Writer()
t1 = Tools('Pen Bic')
w1.tool = t1

print(w1.tool.write())