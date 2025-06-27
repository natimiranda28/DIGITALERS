"""Crea un programa que realice una suma, una resta,
multiplicación y división,
a partir de dos números ingresados por el usuario,
y luego mostrar el resultado por pantalla"""


numero1 = int(input("Ingresá el primer número: "))
numero2 = int(input("Ingresá el segundo número: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2


if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"


print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
