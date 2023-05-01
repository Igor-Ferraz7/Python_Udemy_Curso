# ITERATOR e GENERATOR:
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import sys

iterable = [1, 2, 3, '__iter__']
iterator = iter(iterable) # Um iterator trabalha com iteráveis, sempre visando o PRÓXIMO elemento.

# Você pode criar um iterador que começa a iteração a partir de um determinado elemento, ignorando os elementos anteriores da coleção.

for element in iterable:
    print(element, next(iterator)) # Ele usa apenas o metodo iter e next.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

lista = [number for number in range(1000000)]
generator = (number for number in range(1000000)) # É um iterator que sabe pausar.

#  É possível pausar e continuar a iteração em um gerador, mas a lógica interna do gerador é menos flexível e pode ser mais difícil de controlar em alguns casos.

print(sys.getsizeof(lista))
print(sys.getsizeof(generator)) # ele 
print(next(generator))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-