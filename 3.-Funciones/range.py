def range(minimo,maximo,step):
    lista=[]

    while minimo<maximo:
        lista+=[minimo] #lista.append(minimo)
        minimo+=step

    return lista

print(range(2,10,2))

print(range(100,1000,100))