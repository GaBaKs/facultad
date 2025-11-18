import math

#-------------------------------- EJERCICIO 15 ---------------------------------
# Implementar funciones en Python que reciban como parámetros: una cadena de
# caracteres que contenga un alfabeto fuente y una lista de cadenas de caracteres que
# almacena una codificación en el alfabeto binario, y resuelvan lo siguiente:
# a. Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente,
# devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado.
# b. Dada una secuencia de bytes, decodificar y retornar el mensaje original.
#-------------------------------- EJERCICIO 15 ---------------------------------

def comprime_mensaje(mensaje, fuente, codificacion): #Lo convierte en un ByteArray
    mensaje_codificado = bytearray()
    buffer = ''
    
    for c in mensaje:
        indice = fuente.index(c)
        buffer+= codificacion[indice]

    while len(buffer) >= 8:
        byte = buffer[:8]
        buffer = buffer[8:]
        mensaje_codificado.append(int(byte, 2))

    # Si quedan bits sobrantes, relleno con 0s
    bits_sobrantes = 0
    if buffer:
        bits_sobrantes = 8 - len(buffer)
        byte = buffer.ljust(8, '0')
        mensaje_codificado.append(int(byte, 2))
     
    return mensaje_codificado,bits_sobrantes

def descomprime_mensaje(mensaje, fuente, codificacion, bits_sobrantes): #Analiza un ByteArray
    
    bits = ''.join(f'{byte:08b}' for byte in mensaje)

    mensaje_decodificado = ""
    buffer = ""

    # Recorremos los bits reconstruyendo los símbolos originales

    if bits_sobrantes > 0:
        bits = bits[:-(bits_sobrantes)]

    for bit in bits:
        buffer += bit
        if buffer in codificacion:
            indice = codificacion.index(buffer)
            mensaje_decodificado += fuente[indice]
            buffer = ""
    return mensaje_decodificado

fuente = ['A', 'B', 'C', 'D']
codificacion = ['00', '01', '10', '11']

mensaje = "AAAACAABDABDAA"
mensaje_comprimido, bits_sobrantes = comprime_mensaje(mensaje,fuente,codificacion) #ByteArray
print("El mensaje codificado resulta: ",mensaje_comprimido)

mensaje = mensaje_comprimido #ByteArray
mensaje_descomprimido = descomprime_mensaje(mensaje,fuente,codificacion,bits_sobrantes)
print("El mensaje decodificado resulta: ",mensaje_descomprimido)

# Comprimo un mensaje cambiando su representacion y guardandola en un bytearray
# para esto cargo un byte con el codigo de cada simbolo, entonces si por ejemplo tengo una A y su representacion en el codigo es 00
# se comprime, ya que la letra A ocupa 1 byte(8bits) y 00 2 bits. AAAA = 4 bytes /// AAAA = 1 byte

# Para descomprimir se hace algo similar, primero se toma un byte del ByteArray y se van extrayendo los bits y comparandolos con la codificacion de la fuente
# 00000000 = 00 00 00 00 = AAAA

# Si la compresion no llega a llenar un byte a este lo relleno con 0s y cuento la cantidad de bits de relleno, para que a la hora de descomprimirlos
# no sean tenidos en cuenta