#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para abstraerse de las combinaciones v1

- combinar(l):

       Calcula y devuelve el conjunto potencia del 
       conjunto c.
       Devuelve todas las combinaciones en una lista
    

"""
def combinar(l):
    """ Acepta una lista como argumento, y devuelve todas
        las combinaciones en otra lista de listas"""
    
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
       Devuelve todas las combinaciones en una lista
    """
    if len(l) == 0:
        return [[]]
    r = combinar(l[:-1])
    return r + [s + [l[-1]] for s in r]

if __name__ == "__main__":
    print(__doc__)