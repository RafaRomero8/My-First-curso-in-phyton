def run():
    objetivo = int(input('escoge un entero'))
    respuesta = 0
  #determina si un numero tiene la raiz cuadrada exacta
    while respuesta**2 < objetivo:
        print(respuesta) #
        respuesta +=1 # aumenta la respuesta en uno
    if respuesta**2 == objetivo:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')



if __name__ == '__main__':
    run()