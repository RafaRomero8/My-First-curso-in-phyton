
import random
   #es el paquete que tiene funciones aleatorios
                #se pone punto al final punto y accedemos a la funcion o modulo
def run():
    numero_aleatorio = random.randint(1,100)#randint genera un umero entero que va de A  a un numero b
    numero_elegido = int(input('elige un numero entre el 1 y 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un numero mas grande')
        else:
            print('busca un numero mas pequeño')
        numero_elegido =int(input('elige otro numero: '))
    print('!Ganaste')

#




if __name__ == '__main__':
        run()