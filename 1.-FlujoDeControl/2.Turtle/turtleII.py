#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

# Inicialización: crear una "tortuga" t. Dejar tal cual
t = turtle.Turtle()
# t.hideturtle()  # opcional: no mostrar la tortuga (menos didáctico)

#numero de lados


# Posición inicial no centrada (opcional, se puede modif./eliminar)
t.up()  # lápiz "arriba" (no pintar)
t.goto(-100, 200)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()



    
SIDE_LENGTH = 1
angle = 20
i=1
while i<100:
    t.forward(SIDE_LENGTH)
    t.right(angle)
    SIDE_LENGTH+=1
    i+=1

t.up()  # lápiz "arriba" (no pintar)
t.goto(-100, -200)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()

#El dibujo en sí.
#=== INICIO PARTE A MODIFICAR ===

SIDE_LENGTH = 2
angle = 90
i=1
while i>100:
    t.forward(SIDE_LENGTH)
    t.right(angle)
    SIDE_LENGTH+=1
    i+=1
    
t.up()  # lápiz "arriba" (no pintar)
t.goto(100, 200)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()

SIDE_LENGTH = 2
angle = 360/6
i=1
while i>100:
    t.forward(SIDE_LENGTH)
    t.right(angle)
    SIDE_LENGTH+=1
    i+=1


# === FIN DE PARTE A MODIFICAR ===

# Esto es necesario para que la ventana no se cierre al final. Dejar tal cual
turtle.mainloop()