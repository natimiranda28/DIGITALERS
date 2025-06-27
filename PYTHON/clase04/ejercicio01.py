"""
Usando while, recorrer la frase, y cuando en cuentre la letra 'P' salir del bucle:
frase = (
    "La creciente popularidad del aprendizaje "
    "automático probablemente hará que Python sea el lenguaje líder en el futuro."
)
print(frase)
"""
frase = ("La creciente popularidad del aprendizaje automático probablemente hará que Python sea el lenguaje líder en el futuro.")

i = 0
while i < len(frase):
    if frase[i] == 'P':
        break
    print(frase[i])
    i += 1