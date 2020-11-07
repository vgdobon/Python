import random
import math

a = int(input("Dime el valor de a: "))
b = int(input("Dime el valor de b: "))
c = int(input("Dime el valor de c: "))

if ((pow(b,2)-4*a*c))<0:
    print("No mola")
else:
    xPositivo = (-b + math.sqrt(pow(b,2)-4*a*c))/(2*a)
    xNegativo = (-b - math.sqrt(pow(b,2)-4*a*c))/(2*a)
    print("Valor minimo: ",xNegativo,"\nValor maximo: " ,xPositivo)
