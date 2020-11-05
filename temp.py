# Dispones de los siguentes billetes:
# 3 x 20€, 5 x 10€, 2 x 5€.
# Calcula todas las posibles formas de cambiar
# un billete de 100€ con ellos.
# combinaciones:
#
# Pistas: son combinaciones; no dar resultados
# repetidos; salen tres resultados con esos datos.

#  20,20,20,10,10,10,10
#  20,20,20,10,10,10,5,5
#  20,20,10,10,10,10,5,5

billetes = [5,5,10,10,10,10,10,20,20,20]



def devolucion(peticion_cliente,billetes,combinacion=None):

    aux = []
    for i in ...:
        
        if combinacion is None:
            combinacion=[]

        if peticion_cliente > 0 :
            print(billetes)

            posible_billete=(billetes[int(len(billetes)/2)])
            if peticion_cliente >= posible_billete:
                billete_sacado = posible_billete
                billetes.remove(billete_sacado)
                peticion_cliente-=billete_sacado
                combinacion.append(billete_sacado)
                return devolucion(peticion_cliente,billetes,combinacion)

            elif peticion_cliente >= min(billetes):
                billete_sacado = min(billetes)
                billetes.remove(billete_sacado)
                peticion_cliente-=billete_sacado
                combinacion.append(billete_sacado)
                return devolucion(peticion_cliente,billetes,combinacion)

        else:
            aux.append()




lista_devolucion = devolucion(95,billetes)
print(lista_devolucion)

suma=0
for i in lista_devolucion:
    suma+=i

print(suma)
