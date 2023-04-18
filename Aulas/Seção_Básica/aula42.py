from aparencias import travessao_igual
from aparencias import cores

travessao_igual.titulo('Valor booleano NOT') # o opoerdor NOT, funciona invertendo valores, seja True ou False.
senha = input(f'{travessao_igual.seta(1)}Digite a senha: ')
# Nesse caso, uma str só será false se não conter nada dentro dela
if not senha: # qualquer coisa seguida de um not será avaliada como True ou False. E ela será definida de modo variado.
    print(f'{travessao_igual.seta(1)}Você não digitou nada.') 
travessao_igual.linha()
"""
if not senha -> senha é True?
    se sim: return false e break (não continua a condição)
    senão: return true e pass (continua a condição)
"""
