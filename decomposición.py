def run():

    menu = """programa para buscar la raiz cuadrada
1.Enumeración exhaustiva
2.Aproximación de soluciones
3.Busqueda binaria
--elije una opcion: """

    opcion = int(input(menu))

    if opcion == 1:
        objetivo = int(input('escoge un numero'))
        respuesta = 0

        while respuesta ** 2 < objetivo:
            print(respuesta)
            respuesta += 1
        if respuesta ** 2 == objetivo:
            print(f'la raiz cuadrada de {objetivo} es {respuesta}')
        else:
            print(f'{objetivo} no tiene una raiz cuadrada exacta')

    if opcion == 2:
        objetivo = int(input('escoge un numero'))
        epsilon = 0.001
        paso = epsilon ** 2
        respuesta = 0.0
        while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
            print(abs(respuesta ** 2 - objetivo), respuesta)
            respuesta += paso
        if abs(respuesta ** 2 - objetivo) >= epsilon:
            print(f'no se encontro la raiz cuadrada de {objetivo}')
        else:
            print(f'la raiz cuadrada de {objetivo} es {respuesta}')

    elif opcion == 3:
        objetivo = int(input('escoge un numero'))
        epsilon = 0.01
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo) / 2

        while abs(respuesta ** 2 - objetivo) >= epsilon:
            print(f'bajo={bajo},alto={alto},respuesta={respuesta}')
            if respuesta ** 2 < objetivo:
                bajo = respuesta
            else:
                alto = respuesta
            respuesta = (alto + bajo) / 2
        print(f'la raiz de {objetivo} es {respuesta}')
    else:
        print('ingrese una opcion correcta')
if __name__ == '__main__':
        run()