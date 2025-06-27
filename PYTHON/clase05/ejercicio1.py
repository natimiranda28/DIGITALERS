"""
Dado el siguiente el siguiente código, hacer que preguntar_nombre,
devuelva un string (y no None). Voy a tener que crear una variable
desde donde llamo la función
"""

def saludar_con_nombre(nombre):
    print(f"¡Hola {nombre}!")

def preguntar_nombre():
    nombre = input("Dime tu nombre: ")
    # saludar_con_nombre(nombre)

def principal():
    # nombre = "Python"
    preguntar_nombre()
    # saludar_con_nombre(nombre)

principal()

"""codigo corregido""" 


def saludar_con_nombre(nombre):
    print(f"¡Hola {nombre}!")

def preguntar_nombre():
    nombre = input("Dime tu nombre: ")
    return nombre  #Ahora devuelve el nombre

def principal():
    nombre = preguntar_nombre()  
    saludar_con_nombre(nombre)  

principal()
