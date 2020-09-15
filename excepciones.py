def divide_elemenos_de_lista(lista,divisor):
    try:
        return[i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista
lista = list(range(10))
divisor = 0

print(divide_elemenos_de_lista(lista,divisor))
"""usa asserts hace parte de la programación defensiva, debes usarlos siempre que sepas que algodebe cumplirse,
 se usa mucho con parametros de las funciones.por ejemplo una función que divide dos números 
 a y b uno sabe que b o el divisor no puede ser 
 cero entonces uno puede usar un assert"""