numeros = [3,1,5,True,5,12,67]
#una lista contiene varios elementos,datos de un mismo tipo o diferente
print(numeros)

print(numeros[4])#para acceder a un elemnto de una listta se ponene corchetes

objetos = [3,True,'hola',88]
#append()recibe un parametro
objetos.append(False)
print(objetos)
#borrar cosas con pop()
objetos.pop(1)
print(objetos)
objeto = [3,True,'hola',88,34]
for elemento in objeto:
    print(elemento)
