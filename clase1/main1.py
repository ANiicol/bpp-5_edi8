'''
#Errores de sintaxis

if(5>2) print("Es mayor")

#Errores lógicos
resultado = 2+8/2
print(f"La media es {resultado}")
'''
#Excepciones
'''
try:
    numero = 10
    divisor = int(input("introduce un valor"))
    resultado = numero/divisor

except ZeroDivisionError:
    print("Error, división entre 0")
except ValueError:
    print("Error por el valor pasado")
except Exception as e:
    print("Ha ocurrido un error: ", e)
    
else:
    print(resultado)
    print("Se ejecuta siempre que no se ejecute el except")
finally:
    print("Se ejecutra siempre")
'''   
#raise --> nos permite lanzar exceptiones

'''
raise ZeroDivisionError
raise NameError("Información de la excepción")
'''
#assert -> podemos realizar comprobaciones
#si la expresión es falsa, se lanza una excepcion de tipo AssertionError

#assert(4==5)

'''
if condicion:
    raise AssertionError()
'''
#assert False, "El mensaje personalizado"
#assert (False, "El mensaje personalizado") INCORRECTO!!
#despues de un assert, no se ejecuta el codigo. Tiene que estar dentro de un try, except
'''
def suma(a,b):
    return a+b

assert(suma(2,3) == 5)
assert(suma(4,3) == 5)
'''
'''
def suma(a,b):
    assert(type(a) == int)
    assert(type(b) == int)
    
    return a+b

assert(suma(2,2.0) == 5)
'''

'''
class Clase1:
    pass
class Clase2:
    pass

m1 = Clase1()
m2 = Clase2()

assert(isinstance(m1,Clase1))
'''

#Creando nuestras propias exceptiones

class Miexcepcion2(Exception):
    pass
    '''def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2'''
        
try:
    raise Miexcepcion2({"m1":"Mensaje 1","m2":"Mensaje 2"})
except Miexcepcion2 as e:
    aux = e.args[0]
    print(aux["m1"])
    print(aux["m2"])