"""
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
"""
def fibonacci(n):
    # Inicializar los primeros dos números de la serie
    a, b = 0, 1

    # Verificar si el valor de n es válido
    if n <= 0:
        print("Por favor, ingresa un número positivo.")
    elif n == 1:
        print(a)
    else:
        # Imprimir los primeros n números de la serie de Fibonacci
        print(a, end=" ")
        print(b, end=" ")
        for x in range(2, n):
            # Calcular el siguiente número de la serie y actualizar a y b
            next_number = a + b
            print(next_number, end=" ")
            a, b = b, next_number
        print(" ")

# Ejemplo de uso: Imprimir los primeros 10 números de Fibonacci
fibonacci(10)

"""
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.
"""
def obtener_divisores(numero):
    # Inicializar una lista para almacenar los divisores
    divisores = []
    
    # Iterar desde 1 hasta el número
    for i in range(1, numero + 1):
        # Comprobar si i es divisor de numero
        if numero % i == 0:
            # Si es divisor, agregarlo a la lista de divisores
            divisores.append(i)
    
    return divisores

# Ejemplo de uso: Obtener los divisores de un número
numero = 12
lista_de_divisores = obtener_divisores(numero)
print(f"Los divisores de {numero} son: {lista_de_divisores}")

"""
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
"""
def retorno_lista(lista):
    lista_unicos = list(set(lista))
    return lista_unicos

resultado = retorno_lista([1,2,3,4,5,1,3,4,7,9])
print(resultado)

"""
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
"""
def suma_digitos(numero):
    suma = 0
    # Convierte el número a su representación de cadena (string) para iterar sobre sus dígitos.
    numero_str = str(numero)
    
    # Itera sobre cada dígito en la cadena y suma su valor entero a 'suma'.
    for digito in numero_str:
        suma += int(digito)
    
    return suma

resultado = suma_digitos(15)
print(resultado)

"""
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
"""
def contar_vocales(cadena):
    # Inicializamos un contador de vocales a 0
    contador = 0
    
    # Definimos un conjunto de vocales en minúsculas y mayúsculas
    vocales = set("aeiouAEIOU")
    
    # Iteramos sobre cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter está en el conjunto de vocales, incrementamos el contador
        if caracter in vocales:
            contador += 1
    
    return contador

cadena = "Hola, ¿cómo estás?"
resultado = contar_vocales(cadena)
print(resultado)

"""
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
"""
def primeros_n_elementos(lista, n):
    if n <= 0:
        return []  # Si n es menor o igual a cero, retornamos una lista vacía
    
    if n >= len(lista):
        return lista  # Si n es mayor o igual al tamaño de la lista, retornamos la lista completa
    
    return lista[:n]  # Usamos la rebanada (slice) para obtener los primeros n elementos

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
n = 3
resultado = primeros_n_elementos(mi_lista, n)
print(resultado)

"""
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
"""
def contar_letras_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0
    
    # Iteramos sobre cada carácter en la cadena
    for caracter in cadena:
        # Verificamos si el carácter es una letra mayúscula
        if caracter.isupper():
            mayusculas += 1
        # Verificamos si el carácter es una letra minúscula
        elif caracter.islower():
            minusculas += 1
    
    return mayusculas, minusculas

# Ejemplo de uso:
cadena = "Hola Mundo"
mayusculas, minusculas = contar_letras_mayusculas_minusculas(cadena)
print(f"Mayusculas: {mayusculas}")
print(f"Minusculas: {minusculas}")

"""
8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
"""
def es_numero_perfecto(numero):
    if numero <= 0:
        return False  # Los números negativos y cero no pueden ser perfectos
    
    suma_divisores = 0
    
    # Iteramos desde 1 hasta (numero // 2) + 1 para encontrar los divisores propios
    for divisor in range(1, (numero // 2) + 1):
        if numero % divisor == 0:
            suma_divisores += divisor
    
    return suma_divisores == numero

# Ejemplo de uso:
numero = 6
resultado = es_numero_perfecto(numero)
print(resultado)

"""
9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.
"""
def numero_a_binario(numero):
    binario = bin(numero)
    return binario
resultado = numero_a_binario(9)
print(resultado)

"""
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
"""
def interseccion_listas(lista1, lista2):
    # Utiliza conjuntos para encontrar la intersección
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    interseccion = conjunto1.intersection(conjunto2)
    
    # Convierte la intersección de conjunto a lista
    lista_interseccion = list(interseccion)
    
    return lista_interseccion

# Ejemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = interseccion_listas(lista1, lista2)
print(resultado)

"""
11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
def palindromo(cadena):
    if cadena[:] == cadena[::-1]:
        return "Es palindromo"
    return "No es palindromo"
print(palindromo("ana"))

"""
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.
"""
for numero in range(1, 51):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
        
"""
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.
"""
def ordenar_lista_ascendente(lista):
    return sorted(lista)  # Devuelve una nueva lista ordenada sin modificar la original

# Ejemplo de uso:
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada = ordenar_lista_ascendente(mi_lista)
print(lista_ordenada)


"""
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
"""
def palabras(lista,n):
    nueva_lista = []
    for palabra in lista:
        if len(palabra) > n:
            nueva_lista.append(palabra)
    return nueva_lista
lista = ["Hola", "adios", "Enrique", "motocicleta", "arbol"]
numero = 4
resultado = palabras(lista, numero)
print(resultado)

"""
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.
"""
def fibonacci_iterativo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Inicializamos una lista con los primeros dos números de Fibonacci
    fibonacci = [0, 1]
    
    # Calculamos los siguientes números de Fibonacci iterativamente
    while len(fibonacci) < n:
        siguiente_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente_numero)
    
    return fibonacci

# Ejemplo de uso:
n = 10  # Cambia n según la cantidad de números de Fibonacci que desees calcular
serie_fibonacci = fibonacci_iterativo(n)
print(serie_fibonacci)

"""
16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
"""
def maximo(lista):
    return max(lista)
lista = [1,5,6,8,9]
resultado = maximo(lista)
print(resultado)

"""
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.
"""
def suma_cubos_digitos(numero):
    suma_cubos = 0
    
    # Convierte el número a su representación de cadena (string) para iterar sobre sus dígitos.
    numero_str = str(numero)
    
    # Itera sobre cada dígito en la cadena y suma el cubo de su valor entero a 'suma_cubos'.
    for digito in numero_str:
        valor = int(digito)
        cubo = valor ** 3
        suma_cubos += cubo
    
    return suma_cubos
resultado = suma_cubos_digitos(123)
print(resultado)

"""
18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
"""
def segundo_numero_mas_grande(lista):
    if len(lista) < 2:
        return None  # Si la lista no tiene al menos dos elementos, no hay segundo número más grande
    
    # Eliminamos duplicados y ordenamos la lista en orden descendente
    lista_ordenada = sorted(set(lista), reverse=True)
    
    # El segundo número más grande es el segundo elemento en la lista ordenada
    segundo_mas_grande = lista_ordenada[1]
    
    return segundo_mas_grande

# Ejemplo de uso:
mi_lista = [3, 7, 1, 9, 12, 5]
resultado = segundo_numero_mas_grande(mi_lista)
print(resultado)

"""
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
"""
def tienen_miembro_en_comun(lista1, lista2):
    # Convierte ambas listas en conjuntos (sets)
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Verifica si la intersección de los conjuntos no es vacía
    if conjunto1.intersection(conjunto2):
        return True
    else:
        return False

# Ejemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = tienen_miembro_en_comun(lista1, lista2)
print(resultado)

"""
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
"""
def lista_en_orden_inverso(lista):
    return lista[::-1]

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
lista_inversa = lista_en_orden_inverso(mi_lista)
print(lista_inversa)

"""
21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
"""
def contar_digitos_letras(cadena):
    num_digitos = 0
    num_letras = 0
    
    for caracter in cadena:
        if caracter.isdigit():
            num_digitos += 1
        elif caracter.isalpha():
            num_letras += 1
    
    return num_digitos, num_letras

# Ejemplo de uso:
cadena = "H3ll0 W0rld"
digitos, letras = contar_digitos_letras(cadena)
print(f"Número de digitos: {digitos}")
print(f"Número de letras: {letras}")

"""
 22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números
"""
def suma_numeros(lista):
    acumulada = 0
    for numero in lista:
        acumulada += numero
    return acumulada
lista = [1,2,3,4,5]
resultado = suma_numeros(lista)
print(resultado)

"""
23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.
"""
def elemento_mas_comun(lista):    
    frecuencias = {}  # Diccionario para mantener las frecuencias de cada elemento
    
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    
    elemento_mas_comun = max(frecuencias, key=frecuencias.get)
    
    return elemento_mas_comun

# Ejemplo de uso:
mi_lista = [1, 2, 2, 3, 4, 2, 4, 5, 2]
resultado = elemento_mas_comun(mi_lista)
print(resultado)

"""
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
"""
def tabla_de_multiplicar(numero):
    if numero <= 0:
        return None  # Manejo de casos especiales, como números negativos o cero
    
    tabla = {}
    
    for i in range(1, 11):
        producto = numero * i
        tabla[i] = producto
    
    return tabla

# Ejemplo de uso:
numero = 3  # Cambia este número según el que desees
tabla = tabla_de_multiplicar(numero)
print(tabla)

"""
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
"""
def contar_apariciones_caracteres(cadena):
    apariciones = {}
    
    for caracter in cadena:
        if caracter in apariciones:
            apariciones[caracter] += 1
        else:
            apariciones[caracter] = 1
    
    return apariciones

# Ejemplo de uso:
cadena = "Hola, mundo"
resultado = contar_apariciones_caracteres(cadena)
print(resultado)

"""
26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
"""
def elementos_no_comunes(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    elementos_no_comunes_lista1 = conjunto1.difference(conjunto2)
    elementos_no_comunes_lista2 = conjunto2.difference(conjunto1)
    
    elementos_no_comunes = list(elementos_no_comunes_lista1.union(elementos_no_comunes_lista2))
    
    return elementos_no_comunes

# Ejemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = elementos_no_comunes(lista1, lista2)
print(resultado)

"""
27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.
"""
def eliminar_duplicados(lista):     
    return list(set(lista))


mi_lista = [1, 2, 2, 3, 4, 4, 5, 5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print(lista_sin_duplicados)

"""
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.
"""
def suma_cuadrados_numeros_pares(n):
    suma = 0
    
    for i in range(2, n + 1, 2):
        suma += i ** 2
    
    return suma


numero = 10
resultado = suma_cuadrados_numeros_pares(numero)
print(resultado)

"""
29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
"""
def promedio (lista):
    contador = 0
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
lista = [1,3,5]
resultado = promedio(lista)
print(resultado)

"""
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
"""
def cadena_maslarga(lista):
    cadena_mas_larga = " "
    for cadena in lista:
        if len(cadena) > len(cadena_mas_larga):
            cadena_mas_larga = cadena
    return cadena_mas_larga
lista = ["hola", "motocicleta", "arbol"]
resultado = cadena_maslarga(lista)
print(resultado)

"""
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.
"""
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def n_primeros_primos(n):
    primos = []
    numero = 2  # Comenzamos con el primer número primo, que es 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Ejemplo de uso:
n = 10  # Cambia este valor para obtener los primeros n números primos
primeros_primos = n_primeros_primos(n)
print(primeros_primos)

"""
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
"""
def invertir_palabras(cadena):
    # Dividir la cadena en palabras utilizando el espacio como separador
    palabras = cadena.split()
    
    # Revertir el orden de las palabras
    palabras_revertidas = palabras[::-1]
    
    # Unir las palabras revertidas para formar la cadena resultante
    cadena_resultante = ' '.join(palabras_revertidas)
    
    return cadena_resultante

# Ejemplo de uso:
mi_cadena = "Hola, mundo"
cadena_invertida = invertir_palabras(mi_cadena)
print(cadena_invertida)

"""
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
"""
def ordenar_por_ultimo_elemento(lista_de_tuplas):
    lista_ordenada = []
    for tupla in lista_de_tuplas:
        lista_ordenada.append(tupla[-1])
    lista_ordenada = sorted(lista_ordenada)               
    return lista_ordenada


lista_tuplas = [(1, 5), (2, 3), (3, 8), (4, 1)]
lista_ordenada = ordenar_por_ultimo_elemento(lista_tuplas)
print(lista_ordenada)

"""
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
"""
def contar_vocales(cadena):
    # Inicializamos un contador para las vocales
    contador = 0
    
    # Definimos una lista de letras vocales en minúsculas
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # Convertimos la cadena a minúsculas para hacer la comparación
    cadena = cadena.lower()
    
    # Iteramos sobre cada carácter de la cadena
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    
    return contador

# Ejemplo de uso:
mi_cadena = "Hola, mundo"
cantidad_vocales = contar_vocales(mi_cadena)
print(cantidad_vocales)

"""
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.
"""
def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    
    if numero <= 3:
        return True  # 2 y 3 son primos
    
    if numero % 2 == 0 or numero % 3 == 0:
        return False  # Los números divisibles por 2 o 3 no son primos
    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False  # Si es divisible por algún número entre i y i + 2, no es primo
        i += 6
    
    return True  # Si no se encontraron divisores, es primo

# Ejemplo de uso:
numero = 17  # Cambia este número según el que desees verificar
resultado = es_primo(numero)
print(resultado)


































