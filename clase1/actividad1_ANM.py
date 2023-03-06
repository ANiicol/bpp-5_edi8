'''
1. Crea una funcion que pida por pantalla un número al usuario y que controle mediante excepciones lo siguiente:
    a. Solo se podrá introducir numeros enteros
    b. Si el numero es mayor de 10 lanza una excepción con raise la cual hayas creado previamente mediante ‘class Miexcepcion(Exception):’
'''

class Miexcepcion(Exception):
    pass

def pedir_numero():
    while True:
        try:
            num = int(input("Introduce un número entero: "))
            if num > 10:
                raise Miexcepcion("El número es mayor que 10.")
            return num
        except ValueError:
            print("Debes introducir un número entero.")
        except Miexcepcion as e:
            print(e)

pedir_numero()

'''2. Abre un fichero .txt y controla mediante excepciones las diferentes casuisticas para que el programa no termine de forma inesperada.
Utiliza el finally para cerrar el fichero.
'''

try:
    archivo = open("C:/Users/Alex/OneDrive/02.Formación/Master-PYTHON/05-BPPP/L1/datos.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
except PermissionError:
    print("No tienes permiso para acceder al archivo.")
except Exception as e:
    print("Se ha producido un error inesperado:", e)
finally:
    archivo.close()
