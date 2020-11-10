import conjuntos.combinacion as cc
import conjuntos.permutacion as cp



print("Combinaciones de[1, 2, 3]\n",cc.combinaciones([1,2,3]),end="\n")
print("Combinaciones de[1, 2, 3] de 2 elementos\n",cc.combinacionesN([1,2,3],2))


print()
print()
print()
print()
print()
print("Permutaciones de[1, 2, 3]\n",cp.permutaciones([1,2,3]))
print("Permutaciones de[1, 2, 3] de 2 elementos\n",cp.permutacionesN([1,2,3],2))