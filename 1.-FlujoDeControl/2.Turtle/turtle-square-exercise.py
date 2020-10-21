#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

# Inicialización: crear una "tortuga" t. Dejar tal cual
t = turtle.Turtle()
# t.hideturtle()  # opcional: no mostrar la tortuga (menos didáctico)

#numero de lados
numero_lados= int(input("Dime el numeros de lados"))

# Posición inicial no centrada (opcional, se puede modif./eliminar)
t.up()  # lápiz "arriba" (no pintar)
t.goto(-100, 100)  # movimiento directo a coordenadas, por sencillez (no es lo habitual)
t.down()


# El dibujo en sí.
# === INICIO PARTE A MODIFICAR ===
SIDE_LENGTH = 200
angle = 360/numero_lados
i=0
while i<numero_lados:
    t.forward(SIDE_LENGTH)
    t.right(angle)
    i+=1

t.up() 
t.goto(-150, 150)



# === FIN DE PARTE A MODIFICAR ===

# Esto es necesario para que la ventana no se cierre al final. Dejar tal cual
turtle.mainloop()
