
def run():
    i = 0
    testo = input("Escibe un texto: ")
    while i < len(testo):
        letra = testo[i]
        print(letra, end = ' ')
        i+=1







   # texto = input("Escribe un texto: ")
    #for letra in texto:
     #   if letra == 'o':#cuando se encuntre con la letra o se corta
      #      break
       # print(letra)





   # for i in range(10000):
    #    print(i)
     #   if i == 5678:
      #      break #se para el ciclo en el momento que nosotros queranmos en este caso en el numero 5678



   # frase = input('escribe una frase')
    #for palabra in frase:
     #   print(palabra.strip())
    #nombre = input('escribe tu nombre')
    #for letra in nombre:
     #   print(letra[::-1])  # para cada letra en nonmbre va a imprimir la letra en el ciclo


# for contador in range(1000): #se ejecuta un ciclo pero cada vez que se encuentre un numero impar se salta el numero y no ko imprime
 #         if contador % 2 != 0:
  #            continue #apartir de continue lo que esta despues  no se va a ejecutar
   #       print(contador)

#ejemplo de ciclo con break y continue

if __name__ == '__main__':
    run()
