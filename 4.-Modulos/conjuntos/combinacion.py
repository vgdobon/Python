#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para abstraerse de las combinaciones v1
______________________________________________________________________________
- combinaciones(l):      Calcula y devuelve el conjunto potencia del conjunto c.
                    Devuelve todas las combinaciones en una lista(l)
______________________________________________________________________________
-combinacionesN(c, n):
                    Calcula y devuelve una lista con todas las
                    combinaciones posibles que se pueden hacer
                    con los elementos contenidos en c tomando n
                    elementos a la vez.
______________________________________________________________________________
-numero_combinaciones(l, n):   
                    Calcula y devuelve el número de combinaciones
                    posibles que se pueden hacer con elementos de una lista(l)
                    tomando n elementos a la vez.
_______________________________________________________________________________ 

"""

import math

def combinaciones(l):
    """ Acepta una lista como argumento, y devuelve todas
        las combinaciones en otra lista de listas"""
    
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
       Devuelve todas las combinaciones en una lista
    """
    if len(l) == 0:
        return [[]]
    r = combinaciones(l[:-1])
    return r + [s + [l[-1]] for s in r]

def combinacionesN(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in combinaciones(c) if len(s) == n]

def numero_combinaciones(l, n):
    """Calcula y devuelve el número de combinaciones
       posibles que se pueden hacer con elementos de una lista(l)
       tomando n elementos a la vez.
    """
    m=len(l)
    return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))

if __name__ == "__main__":
    print(__doc__)