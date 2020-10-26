l = [1, 2, 3]
print(l)
print(type(l))

l1= [4, 5, 6]
l_final = l +l1
print(l_final)

print("hola"[2])
print(type(l_final[2]))

l_final+=["hola"]
print(l_final)
print(l_final[6][0])

print("hola" in l_final)

#Metodos de la lista
lista = ["hola"]

#Eliminar un elemento
lista.remove("hola")
print(lista)

#Añadir un elemento
lista.append("hola")

#Añadir un elemento iterable
lista_nombre=["Jaime","adios","Pepe","hola"]
lista.extend(lista_nombre)
print(lista)

#Revertir el orden de los elementos(No devuelde una lista)
lista.reverse()
print(lista)

#Tamaño de una lista
print(len(lista))
print("Count:",lista.count("hola"))
print("Index:",lista.index("hola"))


lista_numeros =[]

i=10
while i<20:
    lista_numeros.append(i)
    i+=1

print("Suma:",sum(lista_numeros))
print("Minimo:",min(lista_numeros))
print("Maximo:",max(lista_numeros))
print("Longitud:",len(lista_numeros))

