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


# El dibujo en sí.
# === INICIO PARTE A MODIFICAR ===
SIDE_LENGTH = 10
angle = 10
i=1
while i>0:
    t.forward(SIDE_LENGTH)
    t.right(angle)
    angle+=10
    



# === FIN DE PARTE A MODIFICAR ===

# Esto es necesario para que la ventana no se cierre al final. Dejar tal cual
turtle.mainloop()