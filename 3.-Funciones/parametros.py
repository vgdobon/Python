def irpf(base, porcentaje=12.5,prorrateado=False):
    """
        irpf (sueldo,porcentaje, prorrateado=boolean)
    """
    if prorrateado:
        cantidad_prorateada = base/6
    if type(base)==float and type(porcentaje)==float:
        return (base/100) * porcentaje
    else:
        return None
    

print(irpf(1000,10))
print(irpf(10000,porcentaje=20))
print(irpf(1000))