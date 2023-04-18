lista_cpf = []
lista_cpf_mult = []
i = i2 = soma_mult = soma_mult2 = 0

CPF = input("Digite seu CPF: ")
CPF = CPF.replace('.', '') #formatando a string
CPF = CPF.replace('-', '') #formatando a string

try:
    for num in CPF:
        lista_cpf.append(int(num)) #adicionando cada índice da string transformada em inteiro.

    if len(lista_cpf) != 11: # tratamento de erros (CPF maior ou menor que 11 numeros)
        raise NameError('CPF inválido, não exceder (ou inserir menos de) 11 números.')

except ValueError:
    print('CPF inválido, por favor, insira somente números, pontos e um travessão.')
except NameError as error:
    print(error)

else:
    lista_cpf_mult_copy = lista_cpf.copy()

    for c in range(10, 1, -1):
        lista_cpf_mult.append(c * lista_cpf[i]) # multiplicando cada numero do cpf
        soma_mult += lista_cpf_mult[i] # somando cada multiplicação
        i += 1

    primeiro_digito = (soma_mult * 10) % 11
    primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

    for c in range(11, 1, -1):
        lista_cpf_mult_copy.append(c * lista_cpf[i2]) # multiplicando cada numero do cpf
        soma_mult2 += lista_cpf_mult_copy[i2] # somando cada multiplicação
        i2 += 1

    segundo_digito = (soma_mult2 * 10) % 11
    segundo_digito = 0 if segundo_digito > 9 else segundo_digito

    dois_digitos = str(primeiro_digito) + str(segundo_digito)

    if CPF[-2:] == dois_digitos and CPF != CPF[0] * len(CPF):
        print('CPF válido.')
    
    else:
        print('CPF inválido.')