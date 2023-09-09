"""
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
"""
for x in range(1,11):
  print(x, end=" ")
print()
"""
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
"""
count = 2
while count < 21:
  print(count, end=" ")
  count = count + 2
print()
"""
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
"""
suma = 0
for numero in range(1,101):
  suma = suma + numero
print(suma)