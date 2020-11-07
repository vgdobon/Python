import math



def primo(numero):
    raiz = math.sqrt(numero)
    i=2

    while i <= raiz:
        if(numero%i==0):
            print("El numero",numero,"no es primo")
            return False #"NO"
        i+=1
    else:
        print("El numero",numero," es primo")
        return True #"SI"

numero = int(input("Dime un numero"))

print("Es primo?",primo(numero))