i = 1 #2 numero de factoriales
sumatorio = 1 #2 Sumatorio de e
factorial = 1 #calculo del factorial

while i < 20:
    
    factorial = factorial * i
    sumatorio += 1/factorial
    
    print(i,":",sumatorio)
    i+=1

print("\nAproximacion del numero e: ",sumatorio)
