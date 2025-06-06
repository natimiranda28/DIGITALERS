"""Proyecto Integrador. Clase 3
Consigna:
========
Crea un programa que solicite el nombre de un alumno a
través de la consola y la cantidad de cursos, y luego
muestre por pantalla esa información.
Ejemplo:
=======
Salida:
Ingrese su nombre: Mateo
Ingrese la cantidad de cursos: 3
Mateo está inscripto en 3 cursos
"""

""" nombre = input ("Ingrese su nombre: ")
cursos = input ("Ingrese la cantidad de cursos en la que esta inscripto: ")

print(f"{nombre} está inscripto en {cursos} cursos") """


alumnos = []

# Lista para almacenar los alumnos
alumnos = []

# Validación de usuario y contraseña
usuario = input("Ingrese nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if usuario == "admin" and contrasena == "uni123":
    while True:
        print("\nIngrese el número de la operación que desea ejecutar:")
        print("1 - Añadir un alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Salir.")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            cursos = input("Ingrese la cantidad de cursos: ")

            if cursos.isdigit():
                alumnos.append((nombre, int(cursos)))
                print("¡El alumno fue añadido a la lista!")
            else:
                print("La cantidad de cursos debe ser un número entero.")
        elif opcion == "2":
            if not alumnos:
                print("La lista de alumnos está vacía.")
            else:
                print("\nLista de alumnos:")
                for alumno in alumnos:
                    print(f"{alumno[0]} - {alumno[1]} cursos")
        elif opcion == "3":
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("La opción ingresada no es correcta, vuelva a intentarlo.")
else:
    print("Usuario y/o contraseña incorrecta.")
