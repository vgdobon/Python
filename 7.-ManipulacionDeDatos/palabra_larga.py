#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def palabra_larga(filename,enc="utf-8"):
    try:
        with open(filename,'r') as file:
            l= [line.split("") for line in file]
            print(l)
                
    except FileNotFoundError as fileNotFound:
        print(fileNotFound)

filename = "7.-ManipulacionDeDatos/palabras.txt"

palabra_larga(di)
