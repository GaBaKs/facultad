import math

#-------------------------------- EJERCICIO 20 ---------------------------------
# Volver a comprimir los mensajes del ejercicio 18 (utilizando la función desarrollada) y
# calcular la tasa de compresión de cada uno.
#-------------------------------- EJERCICIO 20 ---------------------------------


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

def calcula_tasa_compresion(mensaje,mensaje_codificado):
    return (len(mensaje))/len(mensaje_codificado) #Revisar!!! 

fuente = ['A', 'E', 'I', 'O', 'U']
codificacion = ['00', '01', '10', '111', '110']

mensaje = "UUOOOOAAAIEUUUU"

mensaje_comprimido = compresion_RLC(mensaje,fuente,codificacion)

print("El mensaje comprimido en RLC resulta: ",compresion_RLC(mensaje,fuente,codificacion))
print("La tasa de compresion resulta: ",calcula_tasa_compresion(mensaje,mensaje_comprimido))

# Comprimo con RLC y calculo la tasa de compresion comparando el tamaño antes y despues de comprimir
# Comprimo un mensaje con el metodo de RLC el cual indica la cantidad de simbolos que se repiten de forma consecutiva
# por ejemplo: AAAAABBD = 5 A 2 B 1 D
# Estos valores los guardo en un byte array, utilizando un byte para el numero y otro para el simbolo
