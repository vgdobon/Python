def range(min,max,step):
    lista=[]

    while min<max:
        lista.append(min)
        min+=step

    return lista

print(range(2,10,2))

print(range(100,1000,100))