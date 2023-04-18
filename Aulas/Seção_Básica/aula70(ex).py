frase = "Python é uma linguagem de programação multiparadigma. Python foi criado por guido van Rossum."
frase = frase.lower()
alfabeto = "abcdefghijklmnopqrstuvwxyzçáéíóúãõ"
dicionario = {}
lista = []
last_value = 0
contador = 0

for letra in alfabeto:
    dicionario[letra] = frase.count(letra)

for key, value in dicionario.items():
    contador += 1
    if contador == 1:
        if value > last_value:
            biggest_value = value
            letra_moda = key 

        elif value < last_value:
            biggest_value = last_value
            letra_moda = key

    else:
        if value > biggest_value:
            biggest_value = value
            letra_moda = key

        elif last_value > biggest_value:
            biggest_value = last_value
            letra_moda = key

    last_value = value

print(f'Letra: {letra_moda} Qtd: {biggest_value}')


