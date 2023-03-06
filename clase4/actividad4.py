'''PARTE 1'''

import pdb

lista_de_listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
pdb.set_trace()
maximos = [max(lista) for lista in lista_de_listas]
print(maximos)

'''
Al ejecutar este código, veremos que se detiene en la línea donde se llama a pdb.set_trace(). 
Podemos inspeccionar las variables en ese punto, como la lista_de_listas, 
que tendrá el valor [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]. 
Luego, podemos continuar la ejecución línea a línea presionando la tecla n en cada paso.
'''

'''PARTE 2'''

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo, numeros))
print(primos)
