import math

#-------------------------------- EJERCICIO 15 ---------------------------------
# Implementar funciones en Python que reciban como parámetros: una cadena de
# caracteres que contenga un alfabeto fuente y una lista de cadenas de caracteres que
# almacena una codificación en el alfabeto binario, y resuelvan lo siguiente:
# a. Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente,
# devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado.
# b. Dada una secuencia de bytes, decodificar y retornar el mensaje original.
#-------------------------------- EJERCICIO 15 ---------------------------------

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
    bits_sobrantes = 0
    if buffer:
        bits_sobrantes = 8 - len(buffer)
        byte = buffer.ljust(8, '0')
        mensaje_codificado.append(int(byte, 2))
     
    return mensaje_codificado,bits_sobrantes

def decodificar_mensaje(mensaje, fuente, codificacion, bits_sobrantes): #Analiza un ByteArray
    
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
mensaje_codificado, bits_sobrantes = codificar_mensaje(mensaje,fuente,codificacion) #ByteArray
print("El mensaje codificado resulta: ",mensaje_codificado)

mensaje = mensaje_codificado #ByteArray
mensaje_decodificado = decodificar_mensaje(mensaje,fuente,codificacion,bits_sobrantes)
print("El mensaje decodificado resulta: ",mensaje_decodificado)
