import statistics as stats

lista=input("Lista de numeros:")
lista=lista.split()
print(lista)

lista_numericos=[]
for i in lista:
    lista_numericos.append(int(i))
print(lista_numericos)



suma=0
for i in lista_numericos:
    suma+=i

print("Suma:",suma)
print("Media:",suma/len(lista_numericos))


print("Suma con metodos:",sum(lista_numericos))
print("Media con metodos",round(stats.mean(lista_numericos)))