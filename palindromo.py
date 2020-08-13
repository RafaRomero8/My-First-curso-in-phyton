#cuando se escriba una funcion se deja dos espacios apartir de la función
"""def palindromo(palabra):#recibe una palabra
    palabra = palabra.replace(' ','')#elimina espacios
    palabra = palabra.lower() #la convierte a minuscula
    palabra_invertida = palabra[::-1] #la invierte
    if palabra == palabra_invertida: #si se cumple devuelve un true si no false
        return True
    else:
        return False
  """

def main():
    """palabra = input('escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('es palindromo')
    else:
        print('no es palindromo')"""
    palabra = str( input('escribe una palabra: ')).replace(' ','').lower()
    if palabra[::] == palabra[::-1]:
        print('es palindromo')
    else:
        print('no es palindromo')

if __name__ == '__main__':    #es el punto de entrada en phyton al poner doble guion bajo,cuando se ejecuta un archivo
    main()

