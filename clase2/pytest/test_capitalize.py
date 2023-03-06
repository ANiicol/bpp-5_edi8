import pytest
#el nombre del script que contiene los test debe de empezar con test_<loquesea>.py
def capital(x):
    return x.capitalize()

#definir nuestro test
#el nombre de la funcion debe de comentar con el test_<loquese>

def test_capital1():
    assert capital ("hola") == "Hola"
    
def test_capital2():
    assert capital ("hola") == "hola"