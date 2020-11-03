lista = [1, 2, 3, 4, 5, 6]
lista2 = lista.copy()

def print_all_after_delete_first(l):
    del l[0]  #l.pop(0)
    print(l)

def print_delete_first(l):
    a = l.copy() #a=l[:]
    del a[0]
    print (a)

print_all_after_delete_first(lista)
print(lista)

print_delete_first(lista2)
print(lista2)