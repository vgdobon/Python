import random
r = random.randint(1, 100)


print("Debes adivinar un número entre 1 y 100 que he elegido al azar.")
print("Tienes un número ilimitado de intentos (cuantos menos uses, mejor!).")
print("En el primer intento, te diré 'WARM!' si estás cerca (dist. < 10)")
print("Si te acercas más que con el intento anterior, te diré 'WARMER!'")
print("Si te alejas respecto al intento anterior, te diré 'COLDER!'")
print("Cuando aciertes, te diré el número de intentos que te ha costado")


lista_intentos=[]

numero_usuario=-5
distancia_anterior=0

while numero_usuario!=r:
    intento_incorrecto = True
    
    while intento_incorrecto:
        numero_usuario = int(input("Adivina el número:"))
        if 100<numero_usuario<0:
            print("No has escrito un numero correcto")
        else:
            intento_incorrecto=False
            lista_intentos.append(numero_usuario)
    
    distancia_nueva = abs(r-numero_usuario)
    print("Número de aciertos:",len(lista_intentos))

    if len(lista_intentos)==1:
            if  distancia_nueva<10:
                print("WARM!")
            else:
                print("Mal empiezas!!")
    else:
        if distancia_nueva < distancia_anterior:
            print("WARMER!!")
        else:
            print("COLDER!!")

    distancia_anterior=distancia_nueva

print("Has acertado el numero era el",r)
print(len(lista_intentos))