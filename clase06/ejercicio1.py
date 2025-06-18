def saludar(nombre):
    print(f"¡Bienvenido {nombre}!")  

def pedir_cantidad_invitados():
    return int(input("¿Cuántos invitados vendrán a la fiesta? "))

def obtener_lista_de_invitados(cantidad):
    lista = []
    for i in range(cantidad):
        nombre = input(f"¿Cuál es el nombre del invitado {i+1}? ")
        lista.append(nombre)
    lista.sort()
    return tuple(lista)

def main():
    cantidad = pedir_cantidad_invitados()
    lista_de_invitados = obtener_lista_de_invitados(cantidad)
    for invitado in lista_de_invitados:
        saludar(invitado)

main()  
