def run():
    """Calcula el factorial de n.

        n int > 0
        returns n!
        """
    def factorial(n):
        if n == 1:
            return  1
        return  n * factorial(n-1)

    n = int(input('escribe un numero entero: '))
    print(factorial(n))

if __name__ == '__main__':
        run()

