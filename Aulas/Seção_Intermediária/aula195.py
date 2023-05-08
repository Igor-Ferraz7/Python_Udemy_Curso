import os, json

def execut(function, *args):
    def internal():
        return function(*args)
    return internal

def lines():
    print('-='*30)

def listar(tasks):
    print('\nTAREFAS:\n')
    if not tasks:
        print("Nada para listar")
    else:
        for task in tasks:
            print(f'-> {task}')
    print()
    lines()

def desfazer(tasks, remake_tasks):
    if not tasks: #
        print('Nada para desfazer.')
        lines()
    
    else:
        remake_tasks.append(tasks.pop())

def refazer(tasks, remake_tasks):
    if not remake_tasks: #
        print('Nada para refazer.')
        lines()

    else:
        tasks.append(remake_tasks[-1])
        remake_tasks.pop(-1)

def adicionar(tasks, task):
    tasks.append(task)

def clear():
    os.system('cls')

def write_in_doc(arquive, tasks):
    for task in tasks:
        arquive.write(task)

to_do_list = []
remake = []
CAMINHO_ARQUIVO = 'Aulas\\Seção_Intermediária\\aula195.json'



while True:
    print('Comandos: listar, desfazer, refazer')
    action = input('Digite um comando para ser realizado: ').lower()
    lines()

    actions_dict = {
        'listar': execut(listar, to_do_list),
        'desfazer': execut(desfazer, to_do_list, remake),
        'refazer': execut(refazer, to_do_list, remake),
        'adicionar': execut(adicionar, to_do_list, action),
        'cls': execut(clear)
    }

    command = actions_dict.get(action) if actions_dict.get(action) is not None \
    else actions_dict['adicionar']

    command()

    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(to_do_list, arquivo, ensure_ascii=False, indent=2)