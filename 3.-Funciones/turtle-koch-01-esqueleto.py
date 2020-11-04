#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 5 "copo de nieve Koch" del Módulo 5 (esqueleto inicial)

import turtle


def koch(t, order, size):
    """
    Make turtle t draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """

    # MODIFICAR ESTA PARTE !!!
    

    if order==0:
        t.forward(size)
    else:
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)
        t.right(120)
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)

t = turtle.Turtle()

# Dibujar el fractal de Koch varias veces (con distinto 'orden')
for i in range(10):
    # Las tres líneas siguientes, simplemente para ubicar cada uno OK
    t.up()  # Pencil up
    t.goto(-150, 300 - i * 150)
    t.down()

    # Dibujar el fractal de orden i
    koch(t, i, 100)


# Pause at the end
turtle.mainloop()
