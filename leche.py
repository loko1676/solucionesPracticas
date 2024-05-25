"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
"""
precio = 1000
monto = 0
cant = int(input("Ingrese la cantidad de leches que va a comprar: \n"))
jubilado = input("¿Es jubilado? (SI/NO): \n").lower()
jubilado = True if jubilado == "si" else False

if 12 < cant < 24:
    monto = cant * precio
    monto = monto - (monto * 0.1)
elif cant > 24:
    monto = cant * precio
    monto = monto - (monto * 0.15)
else:
    monto = cant * precio

monto = monto - (monto * 0.1) if jubilado == True else monto
# if jubilado == True:
#     monto = monto - (monto * 0.1)
    
print (monto)
