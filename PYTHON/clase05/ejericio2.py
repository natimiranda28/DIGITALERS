"""
Crear una función que reciba una cadena y devolver la cadena convertida en mayúsculas
y mostrar el resultado fuera de la función.
Si el resultado es una cadena vacía, mostrar un mensaje indicando que la cadena está vacía.
De lo contrario, mostrar la cadena.
"""


def convertir_a_mayusculas(cadena):
    return cadena.upper()  

def principal():
    texto = input("Escribí una frase: ")
    resultado = convertir_a_mayusculas(texto)

    if resultado == "":
        print("La cadena está vacía.")
    else:
        print("La cadena en mayúsculas es:", resultado)

principal()
