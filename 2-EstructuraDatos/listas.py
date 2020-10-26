import copy

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

###########Metodos de la lista##############
lista = ["hola","adios"]

#Eliminar un elemento
lista.remove("hola")
del l[0]
print(lista)

#Eliminar un elemento(return elemento)
a = [1,2,3]
b = a.pop()
print("Pop:",b)

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

#Cuantas veces está en la lista
print("Count:",lista.count("hola"))

#Cual es el indice del elemento en la lista
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

#Ordenar lista
x = [1,9,7,4,3,2]
x.sort(reverse=True)
print(x)

#Hacer una copia nueva de una lista
x1 = x.copy()
x2 = x[:]
x3 = list(x)

#Copia profunda
x4 = copy.deepcopy(x)


#############SUBCONJUNTOS###################Rodajas

#Todos
print(x[:])

#Ultimo
print(x[-1])

#Con salto
print(x[::2])

#Saber la direccion de memoria
print(id(x))
