def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):#calcular las diviciones desde el uno
        if i == 1 or i == numero: #si la variable i es igual a 1 salta del ciclo(si alguna de las dos condiciones se cumple se salta el ciclo)
            continue
        if numero % i == 0:#si al dividir el numero por da resto 0 se suma valor al contador
            contador += 1  #
    if contador == 0:
        return True
    else:
        return  False


def run():
    numero = int(input('escribe un numero: '))#convertirlo a entero
    if es_primo(numero): #aveces se puede dejar el condicionaal sin comparar ago
        print('es primo')
    else:
        print('no es primo')







if __name__ =='__main__':
    run()