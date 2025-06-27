"""
=========
EJERCICIO
=========
Solicitar al usuario datos sobre un producto:
    - nombre
    - precio
    - cantidad
Guardar en un diccionario y mostrar en la consola:
"El producto < > cuesta $< > y su stock es < >."
"""



nombre = input("¿Cuál es el nombre del producto? ")
precio = float(input("¿Cuál es el precio del producto? "))
cantidad = int(input("¿Cuál es la cantidad en stock? "))

# Guardamos los datos en un diccionario
producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
}


print(f"El producto {producto['nombre']} cuesta ${producto['precio']} y su stock es {producto['cantidad']}.")
