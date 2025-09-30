[]

import random

n = 20
alf = ['a','c','h','u','s']
codigo = ["BC","A","C","BA","BB"]
probs = [0.13,0.34,0.37,0.12,0.04]

# generar posible mensaje de N simbolos codificados
#             emitidos por la fuente

'''
Usamos random.choices para generar el texto aleatorio. Lo devuelve en una lista
El primer argumento es la lista de caracteres posibles
El segundo argumento, weights, es para definir la probabilidad de cada carácter en el texto generado
k es la longitud del texto generado
join se utiliza para concatenar la lista de caracteres generados en una sola cadena
Dentro de '' se especifica con que queremos separar los elementos de la lista (en este caso, no se separa con nada)
Si escribiera '-' quedaria: 'a-b-c-d' por ejemplo
'''

def Mensaje (codigo,probs,n):
    return "".join(random.choices(codigo,weights = probs,k = n))

print(Mensaje(codigo,probs,n))





