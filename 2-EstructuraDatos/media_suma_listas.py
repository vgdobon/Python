import statistics as stats

lista_numeros=[2, 4, 6, 7, 8, 10]

suma=0
for i in lista_numeros:
    suma+=i

print("Suma:",suma)
print("Media:",suma/len(lista_numeros))


print("Suma con metodos:",sum(lista_numeros))
print("Media con metodos",stats.mean(lista_numeros))