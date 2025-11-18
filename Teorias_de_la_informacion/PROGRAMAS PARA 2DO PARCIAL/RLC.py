import math

#-------------------------------- EJERCICIO 19 ---------------------------------
# Realizar una función en Python que reciba como parámetro una cadena de caracteres con
# un mensaje y devuelva una secuencia de bytes (bytearray) que contenga el mensaje
# comprimido con RLC, utilizando un byte para almacenar la representación en código ASCII
# del carácter y otro byte para el número.
#-------------------------------- EJERCICIO 19 ---------------------------------

def compresion_RLC(mensaje, fuente, codificacion): #Lo convierte en un ByteArray
    mensaje_codificado = []
    anterior = -1
    for c in mensaje:
        indice = fuente.index(c)
        if anterior!=-1 and indice == anterior :
            cont+=1
        else:
            if anterior != -1:
                mensaje_codificado.append(cont)
                mensaje_codificado.append(int(codificacion[anterior],2))
                anterior = indice
                cont = 1
            else:
                anterior = indice
                cont = 1
    mensaje_codificado.append(cont)
    mensaje_codificado.append(int(codificacion[anterior],2))
    return bytearray(mensaje_codificado)

fuente = ['A', 'E', 'I', 'O', 'U']
codificacion = ['00', '01', '10', '111', '110']

mensaje = "UUOOOOAAAIEUUUU"

print("El mensaje comprimido en RLC resulta: ",compresion_RLC(mensaje,fuente,codificacion))

# Comprimo un mensaje con el metodo de RLC el cual indica la cantidad de simbolos que se repiten de forma consecutiva
# por ejemplo: AAAAABBD = 5 A 2 B 1 D
# Estos valores los guardo en un byte array, utilizando un byte para el numero y otro para el simbolo