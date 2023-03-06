import unittest
from funciones import calcularMedia

class TestMedia(unittest.TestCase):
    
    def setUp(self):
        print("Entrando en setUp")
        
    def tearDown(self):
        print("Entrando en tearDown")
        
    def test1(self):
        print("Entrando en test1")
        resultado = calcularMedia([20,20,20])
        self.assertEqual(resultado, 20)
    
    def test2(self):
        print("Entrando en test2")
        resultado = calcularMedia([20,30,20])
        self.assertEqual(resultado, 20)
        