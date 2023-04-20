# O "*" emopacota ou desempacota iteraveis

numeros = 1, 2, 3, 4, 5, 6, 7

def soma(*args):
    somatoria = 0

    for c in args:
        somatoria += c
    
    return somatoria

soma2 = sum(numeros)

soma3 = soma(*numeros)

print(f'{soma2=}, {soma3=}')

