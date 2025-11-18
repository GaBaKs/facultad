#Utilizando las funciones desarrolladas en los ejercicios 11 y 15, comprimir un mensaje
#mediante el algoritmo de Huffman y/o Shannon-Fano y almacenarlo en un archivo binario.
#Enviar el archivo a un compañero, quien tendrá que extraer y descomprimir el mensaje.
#Ambos deben calcular la tasa de compresión, el rendimiento y la redundancia.

def encoder(cadena, fuente, codigo):
    resultado = bytearray()
    buffer = ""  # acumulador de bits

    for car in cadena:
        # índice del símbolo en el alfabeto
        i = fuente.index(car)
        # código correspondiente
        buffer += codigo[i]

        # mientras haya 8 o más bits, empaquetamos un byte
        while len(buffer) >= 8:
            byte = buffer[:8]
            buffer = buffer[8:]
            resultado.append(int(byte, 2))  # convierte '10101100' → entero → byte

    # Si quedan bits sobrantes, rellenamos con ceros a la derecha
    if buffer:
        byte = buffer.ljust(8, '0')
        resultado.append(int(byte, 2))

    with open("persistencia.bin", "wb") as archivo:
        archivo.write(resultado)

    return resultado

def decoder(fuente, codigo):
     
    with open("persistencia.bin", "rb") as archivo:
        datos = archivo.read()  # No hace falta convertir a bytearray, bytes ya sirven

    # Convertir los bytes a una cadena de bits (8 bits por byte)
    bits = ''.join(f'{byte:08b}' for byte in datos)

    resultado = ""
    buffer = ""

    # Recorremos los bits reconstruyendo los símbolos originales
    for bit in bits:
        buffer += bit
        if buffer in codigo:
            i = codigo.index(buffer)
            resultado += fuente[i]
            buffer = ""

    return resultado

code = ['000', '111011', '111010', '11111111110', '111111101', '001', '111001', '11010', '10111', '010', '11111100', '1111011', '1111100', '1010', '11111101', '111111111110', '10110', '11011', '1001', '111111110', '0110', '111000', '111100', '1000', '0111', '11001', '11000', '1111010', '111111111111', '1111111110', '1111101', '111111100']

alfabeto = [
  " ", ",", ".", ":", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
  "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

probs = [
  0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
  0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
  0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
  0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199,
]

# Utilizando las funciones de compresion (Huffman y ShannoFanno) y lo guardo en un archivo