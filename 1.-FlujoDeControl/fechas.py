year = int(input("Año: "))
month = int(input("Mes: "))
day = int(input("Dia: "))

while not (1900 < year < 2021 and 0<month<13 and 0 < day < 32) :
    print("Escribe un año correcto")
    year = int(input("Año: "))
    month = int(input("Mes: "))
    day = int(input("Dia: "))


print(year,"-",month,"-",day,sep="")