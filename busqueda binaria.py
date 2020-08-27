def run():
    #solo funciona cuando el conjunto esta ordenado
    objetivo = int(input('escoge un numero'))
    epsilon = 0.01
    bajo = 0.0#limite inferior
    alto = max(1.0,objetivo)#max()regresa el valor mas alto entre dos valores
    respuesta = (alto + bajo) / 2#se divide el alto y bajo siempre

    while abs(respuesta**2 - objetivo) >= epsilon: #
        print(f'bajo={bajo},alto={alto},respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'la raiz de {objetivo} es {respuesta}')





if __name__ == '__main__':
    run()