#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "recorrer diccionarios" del Módulo 4

dicc1 = {
    "Naranjas": 25,
    "Manzanas": 0,
    "Fresas": 240,
    "Kiwis": 15.33333,
    "Plátanos": 5.5,
}

dicc2 = {
    "Naranjas": None,
    "Manzanas": 55,
    "Fresas": 0.0,
    "Kiwis": "tres bandejas",
    "Plátanos": 5.5,
}

# frutas = dicc1
# print(frutas)
# print(frutas.keys())
# print(frutas.values())
# print(frutas.items())
# print(frutas.get("Naranjas","no esta esa fruta"))
# fruta =dict( frutas.items() )
# print(fruta.items())
# print(fruta)
# print(type(frutas))

# for fruta in frutas:  # si no indico nada, es como keys()
#     # MODIFICAR para que cumpla lo que se pide:
#     if frutas[fruta] > 0:
#         print("La cantidad de:", fruta, "es", frutas[fruta])

# print()


# # Alternativa: recorrer los items (tuplas clave-valor)

# for fruta, cantidad in frutas.items():
#     # MODIFICAR para que cumpla lo que se pide:
#     if cantidad > 0:
#         print("La cantidad de:", fruta, "es", cantidad)

# print()


# # Alternativa 2, no recomendable para este caso: sacar los elementos con popitem()
# # No es recomendable simplemente por eficiencia, tenemos que hacer primero una copia
# # porque no sabemos si luego haría falta la lista original de nuevo (probable...)

# copia_frutas = dict(frutas)  # copia
# # copia_frutas = frutas.copy()  # alternativa (mejor) para copia
# while len(copia_frutas) > 0:
#     fruta, cantidad = copia_frutas.popitem()
#     # MODIFICAR para que cumpla lo que se pide:
#     if cantidad > 0:
#         print("La cantidad de:", fruta, "es", cantidad)

proveedores = {
    1 :{'Nombre':"Fruta Manolo",'telefono': 976704567,'direccion':'Calle Zaragoza'},
    2 :{ 'Nombre':"Frutas María",'telefono':976102030},'direccion':'Avenida Teruel',
    3 :{'Nombre':"Frutas Aragon",'telefono':977456789},'direccion':'Plaza Huesca',
}




dicc1 = {
    "Naranjas":{'cantidad': 25, 'proveedor':proveedores[1]},
    "Manzanas": {'cantidad': 40, 'proveedor':proveedores[2]},
    "Fresas": {'cantidad': 45, 'proveedor':proveedores[3]},
    "Kiwis": {'cantidad': 15.3, 'proveedor':proveedores[1]},
    "Plátanos":{'cantidad':  5.5, 'proveedor':proveedores[2]},
}


frutas = dicc1.copy()


cantidad_frutas_proveedor={}

for clave , valor in frutas.items():
    prov = valor['proveedor']['Nombre']
    
    if not prov in cantidad_frutas_proveedor.keys():
        cantidad_frutas_proveedor[prov]=valor["cantidad"]
    else:
        cantidad_frutas_proveedor[prov]=valor["cantidad"]+cantidad_frutas_proveedor[prov]
        
    # if(valor['proveedor'])==proveedores[1]:
    #     frutas_Manolo+=valor['cantidad']

    
    # if(valor['proveedor'])==proveedores[2]:
    #     frutas_Maria+=valor['cantidad']
    
    
    # if(valor['proveedor'])==proveedores[3]:
    #     frutas_Aragon+=valor['cantidad']
    
print(cantidad_frutas_proveedor)   
# print("Frutas Manolo:",frutas_Manolo)
# print("Frutas Maria:",frutas_Maria)
# print("Frutas Aragon:",frutas_Aragon)



# # for fruta,valor in frutas.items():
# #     print(fruta)
# #     print(valor[])
        
#     # if fruta['proveedor']=="Fruta Manolo":
#     #     frutas_Manolo+=fruta['cantidad']
    
#     # if fruta['proveedor']==2:
#     #     frutas_Maria+=fruta['cantidad']
    
#     # if fruta['proveedor']==3:
#     #     frutas_Aragon+=fruta['cantidad']





