#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dispones de los siguentes billetes:
# 3 x 20€, 5 x 10€, 2 x 5€.
# Calcula todas las posibles formas de cambiar
# un billete de 100€ con ellos.
# combinaciones:
#
# Pistas: son combinaciones; no dar resultados
# repetidos; salen tres resultados con esos datos.

#  20,20,20,10,10,10,10
#  20,20,20,10,10,10,5,5
#  20,20,10,10,10,10,5,5

billetes = [20,20,20,10,10,10,10,10,5,5]

peticion_cliente = 100

def devolucion(peticion_cliente,billetes,combinacion=None):
    global i
    if combinacion is None:
        combinacion={"1":[],"2":[],"3":[]}
        i=1
        copia_peticion = peticion_cliente
        copia_billetes=billetes.copy()

    print(combinacion)
    if peticion_cliente > 0 :
        print(billetes)

        posible_billete=(billetes[int(len(billetes)/i-1)])
        if peticion_cliente >= posible_billete:
            billete_sacado = posible_billete
            billetes.remove(billete_sacado)
            peticion_cliente-=billete_sacado
            combinacion.update({"{str(i)})":combinacion.get(str(i)).append(billete_sacado)})
            combinacion[str(i)]=combinacion[str(i)].append(billete_sacado)
            return devolucion(peticion_cliente,billetes,combinacion)

        elif peticion_cliente >= min(billetes):
            billete_sacado = min(billetes)
            billetes.remove(billete_sacado)
            peticion_cliente-=billete_sacado
            combinacion.append(billete_sacado)
            return devolucion(peticion_cliente,billetes,combinacion) 
    elif(i<3):
        peticion_cliente = copia_peticion
        billetes = copia_billetes.copy()
        i+=1

    else:
            return combinacion

print(devolucion(100,billetes))
