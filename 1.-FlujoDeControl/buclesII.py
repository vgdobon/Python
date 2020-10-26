#Del 1 al 10
print("Del 1 al 10")
for i in range(10):
    print(i+1)

#De i a x(inclusive)
i=0
x=20
print("De",i,"a",x)
while i<=x:
    print(i)
    i+=1

#Números impares
i=0
x=20
print("Numeros impares del",i,"a",x)
for i in range(x+1):
    if(i%2!=0):
        print(i)

#Recorrer una cadena
s = "Hola don pepito"
print("Recorrer una cadena")
for i in s:
    print(i)