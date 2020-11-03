def palabra_larga(l):
    palabra_larga=""
    for palabra in l:
        if(len(palabra_larga)<len(palabra)):
            palabra_larga=palabra
    return palabra_larga


def longitud_caracteres_lista(l):
    longitud = 0
    for palabra in l:
        longitud += len(palabra)
    return longitud

lista_palabra = input("Dime una frase").split()

print(palabra_larga(lista_palabra))

print(longitud_caracteres_lista(lista_palabra))