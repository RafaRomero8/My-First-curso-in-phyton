#conversión de pesos mexicanos a dolaes

"""pesos = input("¿Cuantos pesos tienes?: ")
pesos = float(pesos)
valor_dollar = 22.38
dollars = pesos / valor_dollar
dollars = round(dollars,2)
dollars = str(dollars)
print("Tienes $" + dollars + " dollars ")

#conversión de dolares a pesos mexicanos

dolar = input("¿Cuantos dollars tienes?: ")
dolar = float(dolar)
valor_dollar = 22.38
pesos = dolar * valor_dollar
pesos = round(pesos,2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos mexicanos ")

edad = int(input("Escribe tu edad"))
if edad > 17:
    print("eres mayor de edad")
else:
    print("eres menor de edad")"""

def conversor(tipo_pesos, valor_dollar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dollars = pesos / valor_dollar
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " dollars ")


#conversion con condicional


menu = """
Bienvenido al conversor de monedas 💲

1- Pesos mexicanos
2- Pesos argentino
3- Pesos colombiano

Elige una opción:  """

opcion = int (input(menu))

if opcion == 1:
    conversor("mexicanso",24)

elif opcion == 2:
    conversor("argentinos", 65)

elif opcion == 3:
    conversor("colombianos",3875)

else:
    print("Ingresa una opcion valida")




"""numero = int(input("escribe un número: "))

if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")"""

