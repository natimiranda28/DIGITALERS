palabra_secreta = "azul"
entrada_usuario = input("Adivina la palabra secreta: ")
if entrada_usuario == palabra_secreta:
    print("✨ Has adivinado")
else:
    entrada_usuario = input("Adivina la palabra secreta: ")
    if entrada_usuario == palabra_secreta:
        print("✨ Has adivinado")
    else:
        entrada_usuario = input("Adivina la palabra secreta: ")
        if entrada_usuario == palabra_secreta:
            print("✨ Has adivinado")
        else:
            print("😔 Has perdido")