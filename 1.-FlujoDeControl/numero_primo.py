import math

numero = int(input("Dime un numero"))
raiz = math.sqrt(numero)

i=2

while i <= raiz:
    if(numero%i==0):
        print("El numero",numero,"no es primo")
        break
    i+=1
else:
    print("El numero",numero," es primo")