suma = 0
i=0
n=0

while(n !="" and n != "fin"):

    n = input("Dime un numero")

    if(n != "fin" and n != ""):
        numero = int(n)
        suma+=numero
        i+=1

print("La suma es: ",suma)
print("La media es: ",suma/i)