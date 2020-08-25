"""numeros = [3,1,5,True,5,12,67]
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
    print(elemento)"""
numero_1 = [1,2,3,4]
numero_2 = [5,6,7]
print(numero_1 + numero_2)

#tuplas no se pueden borrar con la funco pp(),son estaticos a diferrencia de lsitas quee son dinamicas
#se ejecutan mas rapidos con el for haciendo el recorrido
#no se pueden agrega elemntos ni quitar,no se pueden modificar
mi_tupla = (1,2,3,4,5)
for numero in mi_tupla:
    print(numero)
