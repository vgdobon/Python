l = [123,432,52,543,544,1,0,2345]

def bubble_sort(l):

    i=1
    while i < len(l):
        j=0
        while j < len(l)-i:
            if l[j] > l[j+1]:
                aux=l[j]
                l[j]=l[j+1]
                l[j+1]=aux
            j+=1
        i+=1

    return l

