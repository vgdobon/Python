import random
x = int(input("Dime un numero:"))
x = random.randrange(100)

#CONDICIONAL IF,ELIF,ELSE
if x>0:
    print(f"{x} es positivo")
elif x<0:
    print(f"{x} es negativo")
else:
    print(x, " es cero")

print(type(x))

for i in range(5):
    xRandom = random.randrange(101)
    if xRandom > 50:
        print(xRandom)4


