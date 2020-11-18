#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
# import sys



# dia = sys.argv[1]
# mes = sys.argv[2]
# año = sys.argv[3]

dia = 17
mes = 11
año = 2020

now = datetime.date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A of %B.")


fecha = datetime.date(año,mes,dia)
fecha.strftime("%m-%d-%y. %d %b %Y is a %A of %B.")
diferencia = now - fecha
print(f"{diferencia.days*24} horas")