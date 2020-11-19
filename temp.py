# print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))

# lista = [1, 2, 3, 4, 5, 6, 7, 8,8, 9]
# print(lista[:-1])
# print(set(lista))


# lista1 = []

# for i in range(10):
#     lista1.append(i)

# set_lista=set(lista1)
# print(set_lista)

# def potencia(c):
#     """Calcula y devuelve el conjunto potencia del 
#        conjunto c.
#        Devuelve todas las combinaciones en una lista
# #     """
# #     if len(c) == 0:
# #         return [[]]
# #     r = potencia(c[:-1])
# #     return r + [s + [c[-1]] for s in r]
# import random

# def cadena_aleatoria():
#     cadena = "ABCDEFGHIJKLMN ÑOPQRSTUVWXYZ"
#     print(cadena)
#     print(len(cadena))
#     i=0
#     while i < len(cadena):
#         numero_aleatorio = random.randrange(28)
#         aux = cadena[i]
#         print()
#         cadena[i].cadena[numero_aleatorio] )
#         cadena[numero_aleatorio].replace( aux )
#         i+=1
        

#     return cadena

# print(cadena_aleatoria())

# tablero_acertado = [ ["A","B","C","D","E","F","G"],["H","I","J","K","L","M","N"],["Ñ","O","P","Q","R","S","T"],["U","V","W","X","Y","Z",""] ]


# print(tablero_acertado.index("A"))    

# np.where(tablero_acertado =="A")


# n = lambda x: x**2
# print(n(5))

cad = "hola, Javier , estamos en Zaragoza , adios\n udghbisuf"
print(cad.strip())
print(cad.split())