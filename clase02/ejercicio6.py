"""
A partir del siguiente código, tratar de que, al ingresar una edad como
número negativo, dar el mensaje: "edad no válida"
edad = int(input("Ingresa la edad: "))
if edad >= 18:
    mensaje = "eres mayor de edad"
else:
    mensaje = "eres menor de edad"
print(mensaje)
"""

edad = int(input("Ingresa la edad: "))

if edad < 0:
    mensaje = "edad no válida"
else:
    if edad >= 18:
        mensaje = "eres mayor de edad"
    else:
        mensaje = "eres menor de edad"

print(mensaje)
