#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 5 "copo de nieve Koch" del Módulo 5 (esqueleto inicial)

import turtle


t = turtle.Turtle()

# Dibujar el fractal de Koch varias veces (con distinto 'orden')
# for i in range(10):
    # Las tres líneas siguientes, simplemente para ubicar cada uno OK
t.up()  # Pencil up
t.goto(-200, 200)
t.down()

    
SIDE_LENGTH = 2
angle = 90
i=1

while i in range(50):
    t.forward(SIDE_LENGTH+i)
    t.right(angle)
    i+=1

t.up()  # Pencil up
t.goto(-200, -200)
t.down()

SIDE_LENGTH = 2
angle = 89


for k in range(50):
    t.forward(SIDE_LENGTH+k)
    t.right(angle)
    k+=1

t.up()  # Pencil up
t.goto(-100,-100)
t.down()

angle = 144
SIDE_LENGTH = 50

for j in range(5):
    for h in range(5):
        t.forward(SIDE_LENGTH)
        t.right(angle)
    t.up()  # Pencil up
    t.forward(SIDE_LENGTH*4)
    t.right(angle)
    t.down()
    
turtle.mainloop()