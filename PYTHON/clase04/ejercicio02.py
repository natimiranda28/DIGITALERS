"""
Utilizar una lista con 10 elementos. Iterar con while True.
Mostrar un elemento y preguntar si es ese el que estoy buscando,
si se responde que "si", vamos a agregarlo a otra lista.
si se responde que "no", continuar con la iteración,
pero si no ser responde con "si" o "no", volver a hacer la pregunta.
Al final, cuando se termine de iterar, mostrar la lista nueva.
comidas_argentinas = [
    "Asado",
    "Empanadas",
    "Provoleta",
    "Humita",
    "Locro",
    "Milanesa",
    "Dulce de Leche",
    "Alfajores",
    "Choripán",
    "Provoleta",
]
"""
comidas = [
    "Asado",
    "Empanadas",
    "Provoleta",
    "Humita",
    "Locro",
    "Milanesa",
    "Dulce de Leche",
    "Alfajores",
    "Choripán",
    "Provoleta",
]

seleccionadas = []
i = 0
while True:
    if i <= len(comidas):
        print("Terminó la iteración.")
        break
    comida = comidas[i]
    respuesta = input(f"¿Es {comida} la comida que estás buscando? (si/no): ").strip().lower()
    
    if respuesta == "si":
        seleccionadas.append(comida)
        print(f"{comida} ha sido agregada a la lista de seleccionadas.")
        i += 1 
    elif respuesta == "no":
        print("Continuando con la siguiente comida...")
        i += 1  
    else:
        print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

print("Lista de comidas seleccionadas:", seleccionadas)


