#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#N-esima
# A partir de la función que calcula la n-ésima potencia,
# modificarlo para que no sea recursivo (sino un simple
# bucle), y después adaptarlo para que sea un generador
# (es decir, que en cada llamada produzca el valor sig.
# que corresponda, y pueda usarse indefinidamente).
def potencia(base,exponente):
    i=1
    while i < exponente:
        yield base ** i
        i+=1
    return

g = potencia(2,6)

print(g)

for i in g:
    print(i)

############################################################################
############################################################################
