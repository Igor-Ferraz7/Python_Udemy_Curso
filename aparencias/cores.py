#• Cores:       •Estilos:
#30 branco     |-0 None
#31 vermelho   |-1 Negrito
#32 verde      |-4 Com linha
#33 amarelo    |-7 Invertido (negative)
#34 azul        •Código:
#35 roxo         \033[estilo;cor;fundom(a string)\033[m
#36 ciano       ex: \033[0;33;44m'Olá mundo\033[m'
#37 cinza

branco = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
des = '\033[m'