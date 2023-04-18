"""
-> É necessário tratar parâmetros com None como padrão.
-> Pois, caso seja definido um argumento como 0 ou não for definido, ele será tratado como false.
"""
def soma(x, y, z=None): 
    if z is not None: 
        print(x + y + z)
        
    else:
        print(x + y)

soma(1, 4)
soma(1, 3, 0)
soma(3, 2, 1)