"""
 --> As variáveis com as quais trabalhamos com o .format podem ser usdas de maneira mais documentada. Possuindo um controle maior sobre parâmetros e argumentos.
"""

a = 'a' # criando variável
b = 'b' # criando variável
c = 2.568 # criando variável
string = 'b={1} - a={0} - b={1} - c={float_2:.2f}' # criando variável que possuirá formatação
strf = string.format(   # formatando as variáveis criadas
    a, b, float_2=c     # atribuindo um parâmetro-nomeado (float_c) para o último argumento (c)
)
print(strf)