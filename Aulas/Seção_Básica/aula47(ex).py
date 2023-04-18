nome = input("Insira seu nome: ")
idade = input("Diga sua idade: ")
lst = [nome, idade]
contador = 0
for c in lst:
    if not c:
        locals_vars = dict(locals())
        for name, value in locals_vars.items():
            if value == c and name != 'c' and contador != len(lst):
                contador += 1
                print(f"O campo '{name}' não foi digitado.")
if nome:
    print(f"O nome ao contrário é: {nome[::-1]}")
    if " " in nome:
        print(f"Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")
    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A última letra do seu nome é {nome[-1]}")
