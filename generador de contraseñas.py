import random

def generar_contrasena():#definir una funcion con simbolos y caracteres
    mayusculas =['A','B','C','D','E','F','G']
    minusculas =['a','b','c','d','e','f','g']
    simbolos =['!','#','$','%','&','/']
    numeros =['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros #concatenamos o sumamos las listas

    contrasena = [] #lista vacia para guardar los carcateres para elegir al azar

    for i in range(15):#hacer un for para recorrer genera 15 caracteres
        caracter_random = random.choice(caracteres)#choice funcion para elegir caracter al azar de la listay se guarada en el caracter random
        contrasena.append(caracter_random)#append para agregar al caracter_radom

    contrasena = "".join(contrasena)#convertir la lista a string (se puede de esta forma)
    return contrasena #join para generar el string unidos con una solacadena
                      #La función join convierte una lista en una cadena formada por
                      #los elementos de la lista separados por comas
                      #juntar todos los caracteres en una sola cadena

def run():
    contrasena = generar_contrasena()
    print('Tu nuevo contraseña es: ' + contrasena)#





if __name__ == '__main__':
    run()