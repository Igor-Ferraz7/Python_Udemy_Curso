# desempacotamento em chamadas de méodos e funções:
string = 'ABCD'
lista = ['Igor',
        'Rogi',
        1, 2, 4,
        'Sousa',
        'Ferraz'
        ]

dict = {"Nome": 'Igor',
        "Idade": 18
        }

print(lista)
print(*lista)

print(dict)
print(*dict)

primeiro, *_, penultimo, ultimo = lista
print(primeiro, penultimo, ultimo)