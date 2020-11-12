#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
class Tablero:

    def __init__(self):
        self.tablero= self.rellenar_tablero_inicial()
    
    
    def cadena_aleatoria(self):
            cadena = ["A","B","C","D","E","F","G","H","I","J","K","L"," ","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            i=0

            while i in range(len(cadena)):
                numero_aleatorio = random.randrange(28)
                aux=cadena[i]
                cadena[i]=cadena[numero_aleatorio]
                cadena[numero_aleatorio]=aux
                i+=1
            
            return cadena

    def rellenar_tablero_inicial(self):
            abecedario = self.cadena_aleatoria()
            letra = iter(abecedario)
            tablero_inicial= [ ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""] ]
            for i in range(4):
                for j in range(7):
                    tablero_inicial[i][j]=letra.__next__()
                
            return tablero_inicial

    


        
    
    def dibujar_estado(self):
        for i in self.tablero:
            print(i,"\n")

    def mover(self,letra,direccion):
        posicion_letra = list(((x,  y) for x,  row in enumerate(self.tablero)
                        for y,  elemento in enumerate(row)  if elemento == letra))
        if direccion=="N":
            
            print(busqueda)
            # if (posicion[0]>3 or posicion[0]<0)  or (posicion[1]>6 or posicion[1]<0):
            pass
        elif direccion=="S":
            pass
        elif direccion=="E":
            pass
        elif direccion=="0":
            pass
        else:
            return "No has elegido una direccion correcta (N S E 0)"

    def comprobacion(self,tablero_comprobacion):
        tablero_acertado = [ ["A","B","C","D","E","F","G"],["H","I","J","K","L","M","N"],["Ñ","O","P","Q","R","S","T"],["U","V","W","X","Y","Z",""] ]
        i=0
        while i < len(tablero_comprobacion):
            j=0
            while j < len(tablero_comprobacion[0]):
                if not tablero_comprobacion[i][j] == tablero_acertado[i][j]:
                    return False
        return True


juego_tablero = Tablero()
while not juego_tablero.comprobacion(juego_tablero.tablero):
    print("Mueve ficha")
    letra= input("Letra a mover")
    direccion= input("En que dirreccion (N,S,E,O)")
    juego_tablero.mover(letra,direccion)
    juego_tablero.dibujar_estado()
    print(juego_tablero.dibujar_estado())


print("HAS GANADO")

