


# Diccionario para almacenar los alumnos (antes era una lista)
alumnos = {}

# Validación de usuario y contraseña
usuario = input("Ingrese nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if usuario == "admin" and contrasena == "uni123":
    while True:
        print("\nSeleccione una opción:")
        print("1 - Añadir un alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Ver cantidad de cursos de un alumno.")
        print("4 - Salir.")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            cursos = input("Ingrese la cantidad de cursos: ")
            if cursos.isdigit():
                alumnos[nombre] = int(cursos)
                print("El alumno fue añadido a la lista.")
            else:
                print("La cantidad de cursos debe ser un número entero.")

        elif opcion == "2":
            if not alumnos:
                print("La lista de alumnos está vacía.")
            else:
                print("\nLista de alumnos:")
                for nombre, cursos in alumnos.items():
                    print(f"{nombre} - {cursos} cursos")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del alumno: ")
            if nombre in alumnos:
                print(f"{nombre} tiene {alumnos[nombre]} cursos.")
            else:
                print("El alumno no se encuentra en la lista.")

        elif opcion == "4":
            print("¡Gracias por utilizar el programa!")
            break

        else:
            print("La opción ingresada no es correcta, vuelva a intentarlo.")
else:
    print("Usuario y/o contraseña incorrecta.")
