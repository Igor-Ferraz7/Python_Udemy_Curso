string = 'Igor'
method = 'upper'

if hasattr(string, method): # Verifica se o metodo existe.
    print(getattr(string, method)()) # executa o metodo (upper) na forma de variável (method)