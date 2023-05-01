# COMO MANIPULAR A PAUSA COM GENERATOR

def generator(n=0):
    yield 1
    print('Continuando....')
    yield 2

gen1 = generator()

print(next(gen1))
print(next(gen1))

# LINKANDO GENERATORS

def genrator2(gen):
    yield from gen
    yield 3
    yield 4

gen2 = genrator2(gen1)
for steps in gen2:
    print(steps)