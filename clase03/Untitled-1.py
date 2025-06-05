"""
Crear un programa que muestre 3 postres como menú.
El usuario debe escribir uno.
Si el nombre coincide con el menú, imprimir "Pedido recibido: <tal cosa>",
de lo contrario, imprimir "<tal cosa> no está en el menú"
1. Poner precio a cada producto y que se muestre en el menú.
2. Crear una billetera con saldo inicial (se puede usar input).
3. Al finalizar, mostrar el saldo final de la billetera.
4. Si el usuario elige un producto, restar el precio del producto al saldo inicial.
5. Si no tengo dinero suficiente, imprimir un mensaje.
6. Si se pudo realizar la compra, también, otro mensaje.
print("Menú de postres:")
print("1. Flan")
print("2. Helado")
print("3. Tarta de manzana")
postre = input("¿Qué postre quieres pedir? ")
if postre == "1":
    print("Pedido recibido: Flan")
elif postre == "2":
    print("Pedido recibido: Helado")
elif postre == "3":
    print("Pedido recibido: Tarta de manzana")
else:
    print(f"{postre} no está en el menú")

"""


menu = ["helado, $1000", "flan, $1200", "tarta, $2000"]


print("Menú de postres:")
print(menu[0])
print(menu[1])
print(menu[2])


pedido = input("Escribí el nombre de un postre del menú: ")
billetera = input ("Ingrese el saldo que posee: ")

if pedido == menu[0]:
    billetera = billetera - 1000
    print(f"Pedido recibido: {pedido} , saldo en billetera: {billetera}")
elif pedido == menu[1]:
    billetera = billetera - 1200
    print(f"Pedido recibido: {pedido} , saldo en billetera: {billetera}")
elif pedido == menu[2]:
    billetera = billetera - 2000
    print(f"Pedido recibido: {pedido} , , saldo en billetera: {billetera}")
else:
    print(f"{pedido} no está en el menú")
