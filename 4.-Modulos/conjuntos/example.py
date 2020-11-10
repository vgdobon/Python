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