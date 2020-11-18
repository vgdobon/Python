#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def potencias(base):
    exponente = 0
    while exponente <= 49:
        yield base**exponente
        exponente +=1

def escribir(filename,enc="utf-8"):
    
    try:
        with open(filename,'w') as file:
            for a in potencias(2): 
                file.writelines (str(a)+"\n")
    except FileNotFoundError:
        print("No ha encontrado el archivo")

filename = "7.-ManipulacionDeDatos/potencias.txt"

escribir(filename)
