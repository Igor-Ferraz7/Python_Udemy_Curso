# impresição dos números de ponto fluuante:
import decimal

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
n3 = n1 + n2
print(n3) #retorna 0.79999... ao invés de 0.8 (sem o modulo 'decimal') / retorna 0.8 com o modulo decimal
print(round(n3, 1)) #corrige o erro sem modulos
