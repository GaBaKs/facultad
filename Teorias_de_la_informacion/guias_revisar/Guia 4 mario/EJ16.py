import math

#-------------------------------- EJERCICIO 16 ---------------------------------
# Codificar una función en Python que reciba como parámetros: una cadena de caracteres
# con un mensaje y una secuencia de bytes (bytearray) con ese mensaje codificado y calcule
# la tasa de compresión
#-------------------------------- EJERCICIO 16 ---------------------------------

def calcula_tasa_compresion(mensaje,mensaje_codificado):
    return (len(mensaje))/len(mensaje_codificado) #Revisar!!!   

def codificar_mensaje(mensaje, fuente, codificacion): #Lo convierte en un ByteArray
    mensaje_codificado = bytearray()
    buffer = ''
    
    for c in mensaje:
        indice = fuente.index(c)
        buffer+= codificacion[indice]

    while len(buffer) >= 8:
        byte = buffer[:8]
        buffer = buffer[8:]
        mensaje_codificado.append(int(byte, 2))  # convierte '10101100' → entero → byte

    # Si quedan bits sobrantes, rellenamos con ceros a la derecha
    if buffer:
        byte = buffer.ljust(8, '0')
        mensaje_codificado.append(int(byte, 2))

    return mensaje_codificado


fuente = ['A', 'B', 'C', 'D']
codificacion = ['00', '01', '10', '11']
mensaje = "ABACBAACABABAACBABAD"
mensaje_codificado = codificar_mensaje(mensaje,fuente,codificacion) #ByteArray

tasa_compresion = calcula_tasa_compresion(mensaje,mensaje_codificado)

print("La tasa de compresion es de: ",tasa_compresion)