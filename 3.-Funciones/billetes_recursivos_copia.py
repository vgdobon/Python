billetes = [5,5,10,10,10,10,10,20,20,20]

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def devolucion(peticion_cliente,billetes):
    combinaciones = potencia(billetes)
    combinacion=[]
    
    for i in combinaciones:
        if sum(i)==peticion_cliente:
            combinacion.append(i)
    

    mj2=[]
    for i in combinacion:
        if i not in mj2:
            mj2.append(i)
    combinacion_dict={}
    a=1
    for h in mj2:
        combinacion_dict[str(a)]=h
        a+=1
    return combinacion_dict


print(devolucion(100,billetes))