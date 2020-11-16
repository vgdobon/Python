def gnomeSort (a): 
    pos = 0 
    while pos < len(a): 
        if (pos == 0 or a[pos]>= a[pos-1]): 
            pos = pos + 1 
        else: 
            aux = a[pos]
            a[pos] = a[pos-1]
            a[pos-1] = aux
            pos= pos - 1
    return a

lista = [2,1,4,5,1,7,6,9,8]
gnomeSort(lista)
print(lista)