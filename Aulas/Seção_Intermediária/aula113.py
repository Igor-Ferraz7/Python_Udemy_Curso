"""
-> Exercícios com funções Pt.1

 Crie uma função que multiplica todos os argumentos
 não nomeados recebidos
 Retorne o total para uma variável e mostre o valor
 da variável.

"""
def mult(*args):
    result = 1
    for c in args:
        result *= c
    return result

print(mult(2, 3, 3))

"""
-> Exercícios com funções Pt.2
 Crie uma função que fala se o número é par ou ímpar.
 Retorne se é par ou ímpar.
"""

def even_odd(number):
    if number % 2 == 0:
        return f'The number {number} is even.'
    return f'The number {number} is odd.'
    
print(even_odd(12323))