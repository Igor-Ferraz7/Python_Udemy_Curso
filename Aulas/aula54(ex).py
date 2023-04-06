print("-="*30)

try:
    numero = int(input("Insira um número inteiro: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

except:
    print("Valor inserido não é válido, pois não é um número inteiro.")

print("-="*30)

try:
    hora = int(input("Que horas são? "))
    
    if hora >= 0 and hora <= 11:
        print("Bom dia então!")

    elif hora >= 12 and hora <= 17:
        print("Boa tarde então!")

    elif hora >= 18 and hora <= 23:
        print("Boa noite então!")

    else:
        print("Não conheço essa hora.")

except:
    print("Valor inávalido. Por favor digite apenas números inteiros.")

print("-="*30)

nome = input("Qual seu primeiro nome? ")

if len(nome) <= 4:
    print("Seu nome é curto!")

elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome tem tamanho normal!")

else:
    print("Seu nome é grande!")

print("-="*30)