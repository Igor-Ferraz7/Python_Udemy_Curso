"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
lista_cpf = []
lista_cpf_mult = []
i = soma_mult = resultado = 0

CPF = input("Digite seu CPF: ")

CPF = CPF.replace('.', '') #formatando a string
CPF = CPF.replace('-', '') #formatando a string
try:
    for num in CPF:
        lista_cpf.append(int(num)) #adicionando cada índice da string transformada em inteiro.
    if len(lista_cpf) > 11 or len(lista_cpf) < 11:
        print(int(adqwda))

except ValueError:
    print('CPF inválido, por favor, insira somente números (), pontos e um travessão.')
except NameError:
    print('CPF inválido, não exceder (ou inserir menos de) 11 números.')

else:
    for c in range(10, 1, -1):
        lista_cpf_mult.append(c * lista_cpf[i])
        soma_mult += lista_cpf_mult[i]
        i += 1

    resultado = (soma_mult * 10) % 11
    resultado = 0 if resultado > 9 else resultado

    print(f"O primeiro dígito é {resultado}")