# Ejemplos con ficheros de texto:
with open('7.-ManipulacionDeDatos/foo.txt', 'r') as file_read:
    
    for line in file_read:  # NOTA: mejor que file_read.readlines():
        print(line, end='')  # cada cadena "line" ya termina con "\n"
with open('7.-ManipulacionDeDatos/foo.txt', 'r') as file_read:
    # De una vez leer todo (sólo si fichero "pequeño"!)
    lista = file_read.readlines()
    # Alternativa: de una vez leer todo (fichero "pequeño"!)
    cad = file_read.read()  # cadena con todo "junto", no lista
    print(cad)
# with open('7.-ManipulacionDeDatos/foo.txt', 'r') as file_read:
#     while ...:  # podemos hacerlo a mano también, con (o sin) bucles
#         line = file_read.readline()

# with open('7.-ManipulacionDeDatos/foo.txt', 'a') as f_write:
#     f_write.write('hola\n')
#     f_write.writelines(['algo\n', 'mas', 'adios\n'])