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

def print_rot13(frase):
    """Pasa una cadena como argumento para codificar ese mensaje,
       la convierte a mensaje encriptado e imprime el mensaje codificado
    """
    palabra_encriptada=""

    for i in frase.lower():
        if i != (" "):
            if i in diccionario.keys():
                palabra_encriptada = palabra_encriptada + diccionario[i]
            else:
                palabra_encriptada =palabra_encriptada + list(diccionario.keys())[list(diccionario.values()).index(i)] 
        else:
            palabra_encriptada += " "
    print(palabra_encriptada)