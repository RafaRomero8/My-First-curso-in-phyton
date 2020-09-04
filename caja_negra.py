#def run():
import  unittest
def suma(num1,num2):
    return num1 + num2
class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num1 = 10
        num2 = 5
        resulatdo = suma(num1,num2)

        self.assertEqual(resulatdo,15)
    def test_negativo(self):
        num1 = -10
        num2 = -7
        resulatdo = suma(num1, num2)

        self.assertEqual(resulatdo, -17)

#es un test te dice el comportamiento de tu codigo

if __name__ == '__main__':
       # run()
    unittest.main()
