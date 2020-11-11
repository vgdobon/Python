#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tablero:

    # def rellenar_tablero_inicial(self, abecedario):
    #         letra = iter(abecedario)
    #         tablero_inicial= [ ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""] ]
    #         for i in range(4):
    #             for j in range(7):
    #                 tablero_inicial[i][j]=letra.__next__()
                
    #         return tablero_inicial



    def __init__(self,tablero_inicial):
        # self.tablero_inicial= self.rellenar_tablero_inicial(tablero_inicial)
        self.tablero_inicial= tablero_inicial
    
    def dibujar_estado(self):
        print(self.tablero_inicial)

    
t=[["a", "h", "ñ", "u", "b", "i", "o"], ["v", "c", "j", "p", "w", "d", "k"], ["u", "x", "e", " ", "l", "r", "f"], ["m", "s", "y", "g", "n", "t", "z"]]

tablero = Tablero(t)

tablero.dibujar_estado()
