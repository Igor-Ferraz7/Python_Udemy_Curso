# Associação
class Writer:
    def __init__(self) -> None:
        self._tool = None
    
    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool):
        self._tool = tool

class Tools:
    def __init__(self, name) -> None:
        self.name = name

    def write(self):
        return f'{self.name} are writing.'

w1 = Writer()
t1 = Tools('Pen Bic')
w1.tool = t1

print(w1.tool.write())