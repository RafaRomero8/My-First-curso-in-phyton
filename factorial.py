def run():
    """Calcula el factorial de n.

        n int > 0
        returns n!

    def factorial(n):
        if n == 1:
            return  1
        return  n * factorial(n-1)

    n = int(input('escribe un numero entero: '))
    print(factorial(n))
 """




    def multiplicar_por_dos(n):
        return n * 2


    def sumar_dos(n):
        return n + 2



    def aplicar_operacion(f,numeros):
        resultados = []
        for numero in numeros:
            resultado = f(numero)
            resultados.append(resultado)


    nums = [1,2,3]
    print(aplicar_operacion(multiplicar_por_dos,nums))
    print(aplicar_operacion(sumar_dos, nums))

    sumar = lambda x,y: x + y
    print(sumar(2,3))

    def aplicar_operaciones(num):
        operaciones = [abs,float]

        resultado =[]
        for operacion in operaciones:
            resultado.append(operacion(num))
        return resultado
    print(aplicar_operaciones(-2))

if __name__ == '__main__':
        run()

