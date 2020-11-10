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
#     """
#     if len(c) == 0:
#         return [[]]
#     r = potencia(c[:-1])
#     return r + [s + [c[-1]] for s in r]

import conjuntos.combinacion as cc
import conjuntos.permutacion as cp



print("Combinaciones de[1, 2, 3]\n",cc.combinar([1,2,3]),end="\n")
print("Combinaciones de[1, 2, 3] de 2 elementos\n",cc.combinaciones([1,2,3],2))


print()
print()
print()
print()
print()
print("Permutaciones de[1, 2, 3]\n",cp.permuta([1,2,3]))
print("Permutaciones de[1, 2, 3] de 2 elementos\n",cp.permutar([1,2,3],2))