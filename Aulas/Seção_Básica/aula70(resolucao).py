frase = "Python é uma linguagem de programação multiparadigma. Python foi criado por guido van Rossum."
frase.lower()
contador = 0
maior_qtd_letra = 0

while contador < len(frase):
    letra_atual = frase[contador]
    qtd_letra = frase.count(letra_atual)
    # print(f"{letra_atual}: {qtd_letra}")

    if ' ' in letra_atual:
        contador += 1
        continue

    if qtd_letra > maior_qtd_letra:
        maior_qtd_letra = qtd_letra
        letra_mais_repetida = frase[contador]
    
    contador += 1

print(f'A letra mais repetida foi: "{letra_mais_repetida}", com uma quantidade de {maior_qtd_letra}x')
    