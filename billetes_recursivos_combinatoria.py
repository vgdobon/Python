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

def devolucion_billetes(peticion_cliente, billetes):
    combinacion={}
    for i in(-1,2,4):
        combinacion[i]=[]
        peticion_cliente = peticion_cliente
        billetes_copy = billetes.copy()
        longitud_billetes=len(billetes)
        while peticion_cliente > 0:    
            for j in range(i,longitud_billetes):
                if peticion_cliente > billetes[i+j]:
                    combinacion[i].append(billetes[i+j])
                    peticion_cliente-=billetes[i+j]
                    del billetes[i+j]
        billetes=billetes_copy.copy()
    return combinacion

print(devolucion_billetes(peticion_cliente,billetes))
        


