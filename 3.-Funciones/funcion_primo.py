import math

def divisores(numero):
    
    divisores=[]
    i=2

    while i < numero:
        if(numero%i==0):
            divisores.append(i)
        i+=1
        
    return divisores

def factoriales_divisores(numero):
    divisores_factoriales=[]
    while numero > 1:
        for i in range(2,numero):
            if numero%i==0:
                divisores_factoriales.append(i)
                numero = numero/i
            


def primo(numero):
    raiz = math.sqrt(numero)
    i=2

    while i <= raiz:
        if(numero%i==0):
            print("El numero",numero,"no es primo")
            print(divisores(numero))
            return False #"NO"
        i+=1
    else: #else del while
        print("El numero",numero," es primo")
        return True #"SI"

numero = int(input("Dime un numero"))

print("Es primo?",primo(numero))
print()

print("Divisores de",numero,":",divisores(numero))
print()