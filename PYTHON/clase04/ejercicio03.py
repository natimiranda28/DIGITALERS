"""
A partir de la siguiente lista, aumentar el precio de cada producto un 10%
y mostrar el resultado en pantalla:
lista_sublistas_producto_precio = [
    ["vaso", 100],
    ["plato", 200],
    ["tenedor", 300],
    ["cuchara", 400],
    ["cuchillo", 500],
]
"""
lista_sublistas_producto_precio = [
    ["vaso", 100],
    ["plato", 200],
    ["tenedor", 300],
    ["cuchara", 400],
    ["cuchillo", 500],
]
for producto, precio in lista_sublistas_producto_precio:
    precio_aumento = precio * 10 / 100 + precio
    print(f"El nuevo precio de {producto} es: {precio_aumento:.2f}")  