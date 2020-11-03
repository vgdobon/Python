diccionario = {
                "a":"n",
                "b":"o",
                "c":"p",
                "d":"q",
                "e":"r",
                "f":"s",
                "g":"t",
                "h":"u",
                "i":"v",
                "j":"w",
                "k":"x",
                "l":"y",
                "m":"z",
}

def print_rot13(palabra):
    palabra_encriptada=""

    for i in palabra:
        if i != (" "):
            if i in diccionario.keys():
                palabra_encriptada = palabra_encriptada + diccionario[i]
            else:
                palabra_encriptada =palabra_encriptada + list(diccionario.keys())[list(diccionario.values()).index(i)] 
        else:
            palabra_encriptada += " "
    print(palabra_encriptada)

palabra = input("Mensaje a escriptar:")
print(palabra,":")
print()

print_rot13(palabra)