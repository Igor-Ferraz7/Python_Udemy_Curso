# while que faça algo do tipo: *I*g*o*r*

nome = input("Digite seu nome: ")
contador = 0
nome_tamanho = len(nome)
nome_formatado = '*'

while contador < nome_tamanho:
    nome_formatado += nome[contador]
    nome_formatado += '*'
    contador += 1
    if contador == nome_tamanho:
        print(nome_formatado)

# while contador < nome_tamanho:
#     if "**" in nome_formatado:
#         print('-='*30)
#         print(f"Antes: {nome_formatado}")
#         print(f"Depois: {nome_formatado_novo}")
#         print('-='*30)
#     nome_formatado += f'*{nome[contador]}*'
#     contador += 1
#     if contador == nome_tamanho:
#         print(nome_formatado)