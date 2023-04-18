from aparencias import travessao_igual

travessao_igual.titulo("Primeiro Exercício")
st_1 = travessao_igual.seta(1)
st_2 = travessao_igual.seta(2)

primeiro_valor = input(f"{st_2}Digite o primeiro valor: ")
segundo_valor = input(f"{st_2}Digite o segundo valor: ")


if primeiro_valor > segundo_valor:
    print(f'{st_1}{primeiro_valor=} é maior que {segundo_valor=}')
else:
    print(f'{st_1}{segundo_valor=} é maior que {primeiro_valor=}')

travessao_igual.linha()