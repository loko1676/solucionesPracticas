"""
Desarrollar un programa secuencial que permita ingresar un precio
calcular el IVA y mostrar el precio final de lista de un producto
Ejemplo: Si un producto vale $100 y el IVA es 21, el precio de lista es $121
"""

precio = float(input("Ingrese el precio del producto: \n"))
iva = float(input("Ingrese el valor del iva: \n"))

precioFinal = precio + (precio * (iva/100))

print(f"El precio final del producto de valor {precio} con un iva de {iva}% es de {precioFinal}")
