# Exercício - Adiando execução de funções

def soma(x=0, y=0):
    x = yield from criar_funcao
    # y = next(criar_funcao)
    return x + y

def multiplica(x=0, y=0):
    return x * y

def criar_funcao(funcao, *args):
    yield args
    return funcao

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))

# -----------------> NAO CONSEGUI RESOLVER <-----------------