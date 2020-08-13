"""contador = 2
print('2 elevado a '+ str(contador) + ' es igual a: ' + str(2**contador))"""


def run():
   """ LIMITE = 1000  #si ponemos una variable en mayuscula se convierte en una constante

    contador = 0
    potencia_2 = 2 **contador #dos elevado a contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1 #aumenta el contador  se puede --> contador += 1
        potencia_2 = 2**contador

   for contador in range(1, 1001): #para la variable contador en  el rango que va de 1 a 1001 range(que va desde 0 al 999)
       print(contador) #se va a imprimir contador del 1 a 1001"""

   for i in range(10):print(11 * i)

if __name__ == '__main__':
    run()