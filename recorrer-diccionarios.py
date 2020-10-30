#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "recorrer diccionarios" del Módulo 4

dicc1 = {
    "Naranjas": 25,
    "Manzanas": True,
    "Fresas": 240,
    "Kiwis": 15.33333,
    "Plátanos": 5.5,
}

dicc2 = {
    "Naranjas": None,
    "Manzanas": "55",
    "ZZZ": (0, 998, 'hola'),
    "Fresas": "0.0",
    "Peras": True,
    "Kiwis": "3",
    "Plátanos": 5.5,
}

frutas = dicc2


# for fruta in frutas:  # si no indico nada, es como keys()
#     if (type(frutas[fruta]) == int) or (type(frutas[fruta]) == float):
#         print("La cantidad de:", fruta, "es", frutas[fruta])
#     # NOTA: opcionalmente permitimos cadenas con "pinta" de números
#     # pero esto tiene un peligro: falla con cadenas que no la tienen!
#     elif type(frutas[fruta]) == str:
#         x = float(frutas[fruta])
#         print("La cantidad de:", fruta, "es", x)

# print()


# Alternativa: recorrer los items (tuplas clave-valor)

for fruta, cantidad in frutas.items():
    if (type(cantidad) == int) or (type(cantidad) == float):
        print("La cantidad de:", fruta, "es", frutas[fruta])
    # NOTA: opcionalmente permitimos cadenas con "pinta" de números
    # pero esto tiene un peligro: falla con cadenas que no la tienen!
    elif type(cantidad) == str:
        x = float(cantidad)
        print("La cantidad de:", fruta, "es", x)

print()


# Alternativa 2, no recomendable para este caso: sacar los elementos con popitem()
# No es recomendable simplemente por eficiencia, tenemos que hacer primero una copia
# porque no sabemos si luego haría falta la lista original de nuevo (probable...)

# # copia_frutas = dict(frutas)  # copia
# copia_frutas = frutas.copy()  # alternativa (mejor) para copia
# while len(copia_frutas) > 0:
#     fruta, cantidad = copia_frutas.popitem()
#     if (type(cantidad) == int) or (type(cantidad) == float):
#         print("La cantidad de:", fruta, "es", frutas[fruta])
#     # NOTA: opcionalmente permitimos cadenas con "pinta" de números
#     # pero esto tiene un peligro: falla con cadenas que no la tienen!
#     elif type(cantidad) == str:
#         x = float(cantidad)
#         print("La cantidad de:", fruta, "es", x)
