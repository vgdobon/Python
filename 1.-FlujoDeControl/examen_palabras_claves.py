palabras_clave = "False await else import pass None break except in raise True class finally is return \
                 and continue for lambda try as def from nonlocal while assert del global not with \
                 async elif if or yield"



lista_palabras_clave =  palabras_clave.split()

longitud_lista_palabras_clave = len(lista_palabras_clave)

lista_palabras_respuesta = []
palabra_respuesta=" "

while palabra_respuesta != "":
    palabra_respuesta = input("Palabra:")
    if palabra_respuesta!="":
        lista_palabras_respuesta.append(palabra_respuesta)


for item in lista_palabras_respuesta:
    if item in lista_palabras_clave:
        lista_palabras_clave.remove(item)


longitud_lista_palabras_clave_final = len(lista_palabras_clave)

print()
if not longitud_lista_palabras_clave_final==0:
    print("Palabras no recordadas:")
    for item in lista_palabras_clave:
        print(item)
print()       

nota = ((longitud_lista_palabras_clave - longitud_lista_palabras_clave_final) / longitud_lista_palabras_clave) *10

print("Nota:",round(nota,2),"/ 10")