#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def palabra_larga(filename,enc="utf-8"):
    l=[]
    longitud=0
    palabra_larga=""
    try:
        with open(filename,'r') as file:
            for i in file:
                i = i.strip()
                i = i.split()
                l.append(i)
            for j in l:
                for item in j:
                    if longitud < len(item):
                        longitud= len(item)
                        palabra_larga = item
            return palabra_larga,longitud
    except FileNotFoundError:
        print("No ha encontrado el archivo")

filename = "7.-ManipulacionDeDatos/palabras.txt"

print(palabra_larga(filename))

def contar_lineas(filename,enc="utf-8"):
    a=0
    try:
        with open(filename,'r') as file:
            for lineas in file:
                a+=1
            return a
    except FileNotFoundError:
        print("No ha encontrado el archivo")

print("Lineas en el archivo",contar_lineas(filename))
