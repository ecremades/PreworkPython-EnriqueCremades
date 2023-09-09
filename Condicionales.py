"""
1. Ejercicio: Dado un número, imprime si es positivo o negativo.  
"""
numero = -1

if numero < 0:
  print('El número es negativo')
else:
  print('El número es positivo')

"""
2. Ejercicio: Dado un número, imprime si es par o impar.
"""
num = 3

if num % 2 == 0:
  print('El número es par')
else:
  print('El número es impar')
  
"""
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
"""

num1 = 200
num2 = 30
num3 = 7

if (num1 > num2) and (num1 > num3):
  print('El número mayor es el primero')
elif (num2 > num1) and (num2 > num3):
  print('El número mayor es el segundo')
else:
  print('El número mayor es el tercero')

