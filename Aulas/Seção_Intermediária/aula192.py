# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

to_do_list = []
remake = []

def lines():
    print('-='*30)

while True:
    lines()
    print('Comandos: listar, desfazer, refazer')
    action = input('Digite um comando para ser realizado: ').lower()

    if action == 'desfazer':
        if not to_do_list: #
            lines()
            print('Nada para desfazer.')
        
        else:
            remake.append(to_do_list.pop())

    elif action == 'refazer':
        if not remake: #
            lines()
            print('Nada para refazer.')

        else:
            to_do_list.append(remake[-1])
            remake.pop(-1)

    elif action == 'listar': #
        print('\nTAREFAS:\n')
        for tasks in to_do_list:
            print(tasks)
        print()

    elif action == 'cls': #
        os.system('cls')

    else:
        to_do_list.append(action)