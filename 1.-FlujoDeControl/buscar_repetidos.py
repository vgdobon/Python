cadena = input("Dime palabras(separadas por espacio)")
lista = cadena.split()



# subcadena = ""

# for i in lista:
    
#     if subcadena.find(i) >= 0:
#         print(i,"está repetida")

#     subcadena = subcadena + " " + i
i=0
j=0

longitud_lista= len(lista)

while i < longitud_lista:
    while j < longitud_lista:
        if not(i==j):
            if lista[i]==lista[j]:
            
                print(lista[i])
        j+=1
i+=1