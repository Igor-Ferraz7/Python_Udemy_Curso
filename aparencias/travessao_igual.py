"""
--> Formatação de strings:

-> s - string
-> d - int
-> f - float
-> x ou X - Hexadecimal

-> > - Joga pra direita
-> < - Joga pra esquerda
-> cite exemplos de temas relacionado à área de tecnologia para artigos cientificos
"""
class cores():
    def __init__(self):
        self.branco = '\033[30m'
        self.vermelho = '\033[31m'
        self.verde = '\033[32m'
        self.amarelo = '\033[33m'
        self.azul = '\033[34m'
        self.roxo = '\033[35m'
        self.ciano = '\033[36m'
        self.des = '\033[m'

cores = cores()
def titulo(nome):
    print(f'{cores.roxo}' + '-='*30, end=f'-{cores.des}\n')
    print(f'{nome:^61}')
    print(f'{cores.roxo}' + '-='*30, end=f'-{cores.des}\n\n')

def linha():
    print('\n', f'{cores.roxo}', '\b' + '-='*30, end=f'-{cores.des}\n\n')

def seta(n):
    travessao = "-"
    st = f'{travessao*n}> '
    return st
# linha()
# print(f"{seta(1)}Ola")
# titulo('Olaa')