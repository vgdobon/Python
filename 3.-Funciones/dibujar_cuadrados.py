#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

# Inicialización: crear una "tortuga" t. Dejar tal cual
t = turtle.Turtle()
# t.hideturtle()  # opcional: no mostrar la tortuga (menos didáctico)

#numero de lados


# Posición inicial no centrada (opcional, se puede modif./eliminar)
t.up()  # lápiz "arriba" (no pintar)
t.goto(-100, 300)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()


def dibujar_cuadrados(n_poligonos,n_lados):
    angle = 360/n_lados
    SIDE_LENGTH = 90/n_lados
    for i in range(n_poligonos):
        t.down()
        for j in range(n_lados):
            
            t.forward(SIDE_LENGTH)
            t.right(angle)
        t.up()
        t.forward(SIDE_LENGTH*n_lados/2)


dibujar_cuadrados(4,4)
dibujar_cuadrados(4,20)