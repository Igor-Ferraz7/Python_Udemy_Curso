condicao = ''
a = "-="

while not condicao:
    try:
        print('-='*30)
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
        print('-='*30)

        try:
            tipo_operacao = int(input(f"[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n{a*30}\nDigite o tipo de operação desejada: "))
            print('-='*30)
            if tipo_operacao == 1:
                print(f"A soma de {n1} e {n2} é {n1+n2}")

            elif tipo_operacao == 2:
                print(f"A subtração de {n1} e {n2} é {n1-n2}")

            elif tipo_operacao == 3:
                print(f"A multiplicação de {n1} e {n2} é {n1*n2}")

            elif tipo_operacao == 4:
                print(f"A divisão de {n1} e {n2} é {n1/n2:.2f}")

            else:
                print("Número inválido, digite apenas valores de 1 a 4.")
        except:
            print("Valor inserido não é válido, insira um número entre 1 e 4 apenas.")
            print('-='*30)
    except:
        print("Valor inserido não é válido, tente novamente.")
        print('-='*30)
    condicao = input("Deseja sair? [S]im: ").upper().startswith("S")