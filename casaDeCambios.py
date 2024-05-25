pesos = 0.0
dolares = 0.0
cambio = 0.0

print("Casa de cambios")

pesos = int(input('Introduzca el monto en pesos argentinos: '))
cambio = int(input('Introduzca a cuántos pesos argentinos equivale 1 dólar: '))

dolares = pesos / cambio

print("Los {} pesos argentinos equivalen a {} dolares, teniendo en cuenta el valor del dolar a {}".format(pesos, round(dolares, 2), cambio))