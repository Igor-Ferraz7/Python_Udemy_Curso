# desempacotamento de listas.
lista = [1, 2]
num1, num2 = lista
print(num1, num2)

str1, str2 = ['ola', 'opa']
print(str1, str2)

lista2 = [0, 1, 2, 3, 4, 5]
_, num1, *_ = lista2 # "_" é usado para guardar variavies que não serão utilizadas, como se fosse uma lixeira.
print(num1, _)