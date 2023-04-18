#gerador de cpfs.
import random

cpf = ''
i = i2 = 0
novo_digito = []

for c in range(9):
    cpf += str(random.randint(0, 9))

for indice in range(10, 1, -1):
    novo_digito.append(int(cpf[i]) * indice)
    i += 1

primeiro_digito = (sum(novo_digito) * 10) % 11
primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

cpf += str(primeiro_digito)
novo_digito = list(str(novo_digito))
novo_digito.clear()

for indice in range(11, 1, -1):
    novo_digito.append(int(cpf[i2]) * indice)
    indice += 1
    i2 += 1

segundo_digito = (sum(novo_digito) * 10) % 11
segundo_digito = 0 if segundo_digito > 9 else segundo_digito
cpf += str(segundo_digito)

print(cpf)