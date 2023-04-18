"""
--> Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a
letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
- Faça a contagem de tentativas do seu usuário.

"""
import os

palavra_secreta = "testes"
letras_acertadas = ''
tentativas = 0

while True:
    letra_solicitada = str(input("Digite uma letra: "))

    if bool(letra_solicitada.isnumeric()):
        print("Valor inválido. è permitido apenas a inserção de letras: ")
        continue
    if len(letra_solicitada) > 1:
        print("Digite apenas uma letra por favor.")
        continue
    else:
        tentativas += 1

    if letra_solicitada in palavra_secreta:
        letras_acertadas += letra_solicitada

    palavra_formada = ''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
           palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')

    if '*' not in palavra_formada:
        os.system('cls')
        print(f"Parabéns! Você completou a palavra secreta com um total de {tentativas} tentativas.")
        break