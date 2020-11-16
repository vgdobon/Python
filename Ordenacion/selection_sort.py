def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k
                 
        swap(aList, least, i)
    

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def linearSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found:
        if my_list[position] == item:
            found = True
        position = position + 1
    return found

lista = [1.4,1,4.1,4,7,2]
selectionSort(lista)
print(lista)

print("¿Esta el 1 en la lista?",linearSearch(2,lista))