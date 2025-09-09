"""
A partir del siguiente código, crear un bloque
try-except para que muestre "el archivo no existe"
archivo = open("17_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()
archivo = open("17_test.tx", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
"""
try:
    archivo = open("17_test.txt", "w")
    archivo.write("Python\n")
    archivo.write("Django\n")
    archivo.close()
    archivo = open("17_test.tx", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)    
except FileNotFoundError:
    print("el archivo no existe")
except Exception as e:
    print("Ocurrió un error:", e)   
finally:
    print("Ejecución del bloque try-except finalizada.")    

    