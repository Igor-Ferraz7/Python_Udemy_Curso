"""
--> Funções de primeira classe
"""
def salutation(msg, name):
    return f'{msg}, {name}!'

def execution(function, *args): # Empacoando parâmetros.
    return function(*args) # Desempacotando argumentos.

print(
    execution(salutation, 'Good Morning', 'Igor')
)