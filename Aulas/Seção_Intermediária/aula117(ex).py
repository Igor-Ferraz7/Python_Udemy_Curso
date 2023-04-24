"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""
def duplication(arg):
    arg *= 2
    return arg

def triplication(arg):
    arg *= 3
    return arg

def quadrupling(arg):
    arg *= 4
    return arg

print(
    duplication(9),
    triplication(4),
    quadrupling(6)
)
