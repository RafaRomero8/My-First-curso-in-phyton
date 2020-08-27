def run():
    objetivo = int(input('escoge un numero'))
    epsilon = 0.0001 #presicion que queremos
    paso = epsilon**2 #mas pequeño que epsilon
    respuesta = 0.0 #variable para guardar la respuesta

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:  # conforme el valor absoluto sde acerca a epsilon se va a llegar mas cerca
        #abs()regresa el valor absoluto
        print(abs(respuesta**2 - objetivo),respuesta)
        respuesta += paso #respuesta aumenta el paso en cada iteracion sube
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'no se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
"""objetivo = int(input('escoge un entero'))
    respuesta = 0
  #determina si un numero tiene la raiz cuadrada exacta
    while respuesta**2 < objetivo:
        print(respuesta) #
        respuesta +=1 # aumenta la respuesta en uno
    if respuesta**2 == objetivo:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')"""



if __name__ == '__main__':
    run()