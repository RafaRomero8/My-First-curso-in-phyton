def run():
    poblacion_paises = {
        'Mexico': 12000000,
        'Brasil': 21098790,
        'colombia': 2340078,
    }
    print(poblacion_paises['Mexico'])

    for pais in poblacion_paises.keys(): #keys devuelve las llaves del diccionario
        print(pais)

    for poblacion in poblacion_paises.values():#devuelve los valores del diccionario
        print(poblacion)

              #items devuelve la llave y el valor del diccionario ambas cosas
    for ppais,poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])
#con diccionario se utiliza llaves sirve paar definir los diccionario
#es una esrtructura de datos de llaves y valores,se accede a travez de las llaves
#


if __name__ == '__main__':
    run()