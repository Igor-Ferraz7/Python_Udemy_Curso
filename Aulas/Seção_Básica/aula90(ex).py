"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.

- nada para listar (impossibilitar mostrar listas que não contém nada)
- impossiblitar apagar indices não existentes

- quando for inserir algo: limpar o terminal
- o indice a ser apagado deverá ser solicitado

- vai printar indice e o item juntos e sempre deverão ser atualizados 
"""
import os

lista = []

while True:
    print('-='*30)
    resposta = input("Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ").lower()
    print('-='*30)

    if resposta == 'i':
        os.system('cls')
        inserir_valor = input("Digite um valor para ser inserido: ")
        lista.append(inserir_valor)
    
    elif resposta == 'a':
        try:
            apagar_valor = int(input("Digite um índice a ser apagado: "))
            lista.pop(apagar_valor)
        except ValueError:
            print("Índice inválido. Insira apenas um número inteiro.")
        except IndexError:
            print("Índice inválido. Insira apenas um índice existente.")
    
    elif resposta == 'l':
        os.system('cls')
        if not lista:
            print("Nada para listar.")
        else:
            for item in range(len(lista)):
                print(f'{item} {lista[item]}')
    
    else:
        print("Opção inexistente.")
    
    
