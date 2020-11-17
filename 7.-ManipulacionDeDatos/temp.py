#!/usr/bin/env python3
# -*- coding: utf-8 -*-


FICH_TABL = "7.-ManipulacionDeDatos/juego-vida.txt"

def leer_tablero_fich(nombre_fich):
    """Lee un fichero de texto con un contenido adecuado (...) y lo convierte
    en una matriz que representa el tablero de juego (0's y 1's numéricos)"""
    # Recordar que se debe cumplir que:
    # - Comprobar que todas tengan la misma logitud
    # - Permitir cualquier número de líneas de entrada
    # - Ignorar las líneas completamente vacías
    # La matriz resultado
    m = []
    with open(nombre_fich, 'r') as file_read:
        
        longitud = 0

        # for linea in file_read:
        #     if longitud==0:
        #         longitud = len(linea)
        #     elif len(linea)!=longitud:
        #         return "La siguiente linea no tiene la longitud correcta:",linea

        i=0
        for linea in file_read:  # NOTA: mejor que file_read.readlines():

            # j=0
            # for char in linea:
            #     m[i][j]==char
            #     j+=1
            # i+=1
            linea_lista = list(linea.strip())
            m.append(linea_lista)
    return m

m = leer_tablero_fich(FICH_TABL)

for i in m:
    linea=""
    for j in i:
        linea = linea + j
    print(linea)