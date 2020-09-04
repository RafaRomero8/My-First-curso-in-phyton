def run():
    """
    def coordenadas():
        return (5,4)


    coordenada = coordenadas()
    coordenada
    print(coordenada)

    x,y = coordenadas() #desempaquetada
    print(x,y)

    my_tuple = (8,)
    print(my_tuple)

    # range(comienzo,fin,pasos)

    my_range = range(1, 5)
    my_ranges = range(0, 7, 2)

    print(type(my_range))#tipo de esta variable
    for i in my_range:
        print(i)  #es no inclusivo no esta incluyendo el final

    for h in my_ranges:
        print(h)

    for k in range(0,21,2):
        print('------------')
        print(k + 1)
#el contenido de las tuplas  pueden ser de tipo int,float y string
   """

    # lista
    a = [1,2,3]
    c =list(a) # para clonar la lista (sintaxis)
    print(c)
    d = a[::]
    print(d)# otra forma de clonar lista

    my_list = list(range(20))
    print(my_list)
    double = [i * 2 for i in my_list] #notacion de list comperhension  se define la peracion que queremos(i * 2)
    print(double)

    pares =[i for i in my_list if i % 2 == 0]# se aplica el filtro es decir if i % ...
    print(pares)












if __name__ == '__main__':
        run()