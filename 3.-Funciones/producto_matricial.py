m = [[1,2],[3,4],[5,6]]
n = [[5,10,15,0],[0,0,20,0]]


def producto_matricial(m,n):
    #filas y columnas del resultado
    a = len(m)  #filas de m
    filas = a
    d = len(n[0]) #columnas de n
    columnas = d

    b = len(m[0]) #columnas de m
    c = len(n) #filas de n

    #calcular r[0]
    if b != c:
        print("Error, no calculable")
        exit(1)
        
    r = []
    #calcular r[0][0] le llamo x
    for k in range(a):
        l = []
        for j in range(d):
            x = 0
            for i in range(b):
                sumando = m[k][i] * n[i][j]
                # print(f"Iteracion {i}: sumado vale {sumando}")
                x = x + sumando
            l.append(x)
        # l es una fila de resultados
        r.append(l)
    return r

print(producto_matricial(m,n))