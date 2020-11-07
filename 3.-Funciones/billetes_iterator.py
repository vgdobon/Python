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
import itertools as it

bills = [5,5,10,10,10,10,10,20,20,20]


print(bills)
makes_100 = []

list(it.combinations(bills, 3))
def devolucion(peticion_cliente,bills):

    makes_100 = []
    for n in range(1, len(bills) + 1):
        for combination in it.combinations(bills, n):
            if sum(combination) == peticion_cliente:
                makes_100.append(combination)
    return set(makes_100)

print(devolucion(100,bills))

        