#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def leer_fichero_palabras(filename):
    """Devuelve una LISTA de cadenas con las palabras que contiene el fichero indicado.
    Todas están en MINÚSCULAS"""
    wordlist = []
    try:
        with open(filename,'r') as file_r:
            for linea in file_r:
                linea = linea.strip()
                wordlist.append(linea)

        pass

    except:
        print("Error leyendo fichero:", filename)
        wordlist = []  # por si acaso, no devolver nada

    return wordlist

# flashcard_filename = "Scrabble/sowpods.txt" 
# print(leer_fichero_palabras(flashcard_filename))