#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para abstraerse de las permutaciones v1
_________________________________________________________________________________
inserta_multiple(x, lst):
        Devuelve una lista con el resultado de
        insertar x en todas las posiciones de lst.  
_________________________________________________________________________________
inserta(x, lst, i):
        Devuelve una nueva lista resultado de insertar
        x dentro de lst en la posición i.
_________________________________________________________________________________
permutaciones(l):
       Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos de una lista(l).
    
_________________________________________________________________________________
permutacionesN(c, n):
        Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n elementos
_________________________________________________________________________________
-numero_permutaciones(l, n):   
                    Calcula y devuelve el número de permutaciones
                    posibles que se pueden hacer con elementos de una lista(l)
                    tomando n elementos a la vez.
_________________________________________________________________________________    

"""
import math
import conjuntos.combinacion

def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]

def permutaciones(l):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos de una lista(l).
    """
    if len(l) == 0:
        return [[]]
    return sum([inserta_multiple(l[0], s)
                for s in permutaciones(l[1:])],
               [])

def permutacionesN(c, n):
    """ Acepta una lista como argumento, y devuelve todas
        las permutaciones en otra lista de listas"""
    
    
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permutaciones(s)
                for s in combinacion.combinaciones(c, n)],
               [])


def numero_permutaciones(l, n):
    """Calcula y devuelve el número de permutaciones
       posibles que se pueden hacer con elementos de una lista(l)
       tomando n elementos a la vez.
    """
    m = len(l)
    return math.factorial(m) // math.factorial(m - n)

if __name__ == "__main__":
    print(__doc__)