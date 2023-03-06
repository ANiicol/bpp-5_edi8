# Script con funciones para sumar y multiplicar dos números

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b


# Pruebas utilizando unittest

import unittest

class TestFunciones(unittest.TestCase):
    
    def setUp(self):
        print("Entrando en setUp")
        
    def tearDown(self):
        print("Entrando en tearDown")

    def test_sumar(self):
        print("Entrando en test sumar")
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(-2, 5), 3)

    def test_multiplicar(self):
        print("Entrando en test multiplicar")
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(0, 0), 0)
        self.assertEqual(multiplicar(-2, 5), -10)
        self.assertEqual(multiplicar(4, 0.5), 2)
    
    def test_sumar_entero_y_flotante(self):
        print("Entrando en test sumar entero y flotante")
        self.assertEqual(sumar(2, 3.5), 5.5)
        self.assertEqual(sumar(0, 2.5), 2.5)
        self.assertEqual(sumar(-2, 5.8), 3.8)

    def test_sumar_negativo(self):
        print("Entrando en test sumar negativo")
        self.assertEqual(sumar(-5, -3), -8)
        self.assertEqual(sumar(-2, -2), -4)

    def test_multiplicar_entero_y_flotante(self):
        print("Entrando en test multiplicar entero y flotante")
        self.assertEqual(multiplicar(2, 3.5), 7)
        self.assertEqual(multiplicar(0, 2.5), 0)
        self.assertEqual(multiplicar(-2, 5.8), -11.6)

    def test_multiplicar_negativo(self):
        print("Entrando en test multiplicar negativo")
        self.assertEqual(multiplicar(-5, 3), -15)
        self.assertEqual(multiplicar(-2, -2), 4)


# Pruebas utilizando pytest

import pytest

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(0, 0) == 0
    assert sumar(-2, 5) == 3

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(0, 0) == 0
    assert multiplicar(-2, 5) == -10
    assert multiplicar(4, 0.5) == 2

def test_sumar_entero_y_flotante():
    assert sumar(2, 3.5) == 5.5
    assert sumar(0, 2.5) == 2.5
    assert sumar(-2, 5.8) == 3.8

def test_sumar_negativo():
    assert sumar(-5, -3) == -8
    assert sumar(-2, -2) == -4

def test_multiplicar_entero_y_flotante():
    assert multiplicar(2, 3.5) == 7
    assert multiplicar(0, 2.5) == 0
    assert multiplicar(-2, 5.8) == -11.6

def test_multiplicar_negativo():
    assert multiplicar(-5, 3) == -15
    assert multiplicar(-2, -2) == 4


# Ejecución de las pruebas

if __name__ == '__main2__':
    unittest.main()
    pytest.main()
