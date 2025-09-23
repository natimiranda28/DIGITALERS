
"""Crear una función en Python que tome como argumento 
un entero que indique la cantidad de términos y retorne 
una lista como la anterior. Por ejemplo:
>>> fib(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
La función debe, además, chequear que el argumento 
pasado sea mayor a 2. En caso de ser menor, debe 
mostrar un mensaje en pantalla y no retornar nada."""
def fib(n):
    if n <= 2:
        print("La cantidad debe ser mayor a 2")
        return

    # Lista de los primeros dos términos de la secuencia Fibonacci
    numeros_fibonacci = [0, 1]

    # Generamos los términos de la secuencia hasta n
    for i in range(2, n):
        a = numeros_fibonacci[-1] + numeros_fibonacci[-2]
        numeros_fibonacci.append(a)

    return numeros_fibonacci

# Solicitamos el número al usuario
n = int(input("Ingrese un número mayor a 2: "))


resultado = fib(n)
if resultado:
    print(resultado)
