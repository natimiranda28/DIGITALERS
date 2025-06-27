"""
Solicitar al usuario la cantidad de stock que comprará.
Mostrar en la terminal el nombre del artículo, el precio unitario, y el precio final.
"""

# Entrada
nombre_articulo = "perfume"
precio_unitario = 100
stock = 10
print(f"Va a comprar: {nombre_articulo}")
print(f"Precio unitario: {precio_unitario}")
print(f"Stock: {stock}")
cantidad_a_comprar = int(input("¿Cuántas unidades desea comprar? "))
# Operaciones
precio_final = precio_unitario * cantidad_a_comprar
stock = stock - cantidad_a_comprar
# Salida
print("*********************")
print(f"Compra: '{nombre_articulo}'")
print(f"Precio final: ${precio_final}")
print(f"Stock disponible del {nombre_articulo}: {stock}")