"""
1. Ejercicio: Define una función que tome dos números y retorne su suma.
"""
def suma(n1,n2):
  return n1 + n2
print(suma(3,5))
"""
2. Ejercicio: Define una función que tome un número y retorne su factorial.  
"""
def factorial(n):
  if n == 0 or n == 1:
    resultado = 1
  elif n > 1:
    resultado = n * factorial(n - 1)
  return resultado
  
resultado = factorial(5)
print(resultado)
"""
3. Ejercicio: Define una función que tome un número y determine si es primo.
"""
def primo(n):
  for i in range(2,n):
    if n % i == 0:
      return "No es primo"
  return "Es primo"
    
resultado = primo(5)
print(resultado)
  

"""
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
"""
def suma_lista(lista):
  total = 0
  for n in lista:
    total = total + n
  return total

resultado = suma_lista([5,3,2])
print(resultado)
  

"""
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
"""
def cadena_reversa(cadena):
  reversa = cadena[::-1]
  return reversa

nueva_cadena = cadena_reversa("Hola")
print(nueva_cadena)