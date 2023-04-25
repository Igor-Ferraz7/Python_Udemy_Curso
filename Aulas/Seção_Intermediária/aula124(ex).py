options = {}

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
    for key, value in question.items():

        if key == 'Opções':
            print(f"--> {key}: \n")
            tupla = enumerate(value)

            for item in tupla:
               print(f'-> ({item[0]}) {item[1]}')
               options[item[0]] = [int(item[1])]

            answer = int(input('Escolha uma opção: '))

            if answer >= len(value):
                answer = None

            for index, value2 in options.items():

                if answer == index and answer < len(value):
                    answer = int(*value2)
                    break

        elif key == 'Resposta':

           if int(value) == answer:
                print('** ACERTOU **')
                acertos += 1
           else:
               print('X-X ERROU X-X')

        else:
            print('-='*30)
            print(f'{key}: {value}')
            print('-='*30)

print(f'Você acertou {acertos} de 3 perguntas')
