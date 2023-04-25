
"""
Aqui fiz uma mesclagem do que analisei no codigo feito pelo professor, do que quis aproveitar do meu codigo anterior feito e de outro codigo analisado, porem de um aluno.
"""
acertos = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for question in perguntas:
    ask = question['Pergunta']
    options = question['Opções']
    answer = question['Resposta']

    print('-='*30)
    print(f'Pergunta: {ask}')
    print('-='*30)

    for index, option in enumerate(options):
        print(f'{index}) {option}')

    choice = input('Escolha uma opção: ')

    if choice.isdigit():
        choice = int(choice)

        if choice < len(options):
            if options[choice] == answer:
                print('ACERTOU')
                acertos += 1
        else:
            print('ERROU')

    else:
        print('ERROU')

print(f'Acertou {acertos} de {len(perguntas)} perguntas.')
