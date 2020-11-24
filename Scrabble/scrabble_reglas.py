#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrabble_fich as ss

def calcular_puntuacion_palabra(palabra):
    """Devuelve el valor (numérico) de la puntuación según scrabble de la palabra (cadena) indicada"""
    VALORES_LETRAS = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                        "x": 8, "z": 10}

    puntuacion=0
    for char in palabra:
        puntuacion += VALORES_LETRAS[str(char)]
    return puntuacion


def palabra_es_valida(palabra, lista):
    """Devuelve True si la palabra se encuentra dentro de la lista recibida"""
    
    if palabra in lista:
        return True

    return False

print(calcular_puntuacion_palabra("hola"))




flashcard_filename = "Scrabble/sowpods.txt" 

print(palabra_es_valida("ZZZ",ss.leer_fichero_palabras(flashcard_filename)))
