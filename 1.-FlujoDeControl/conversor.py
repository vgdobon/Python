seguir_operando = True

while seguir_operando:
    numero_convertir = input("Numero en base 10:")
    numero_decimal = int(numero_convertir)
    base_salida = int(input("A que base quieres convertir el numero: "))
    numero_base=""
    while numero_decimal >= 1:
        digito_base = numero_decimal%base_salida
        numero_decimal = numero_decimal//base_salida
        numero_base= str(digito_base) + numero_base
    
    
    print("\nEl numero decimal",numero_convertir,"en base",base_salida,"es:",numero_base,"\n")
    
    
    seguir_operando = bool(int(input("¿Quieres seguir haciendo operaciones?\n\
(Pulsa 0 para terminar el programa o 1 para continuar haciendo operaciones)")))

