"""Realizar una función en Python que reciba como parámetro una cadena de caracteres con
un mensaje y devuelva una secuencia de bytes (bytearray) que contenga el mensaje
comprimido con RLC, utilizando un byte para almacenar la representación en código ASCII
del carácter y otro byte para el número.
"""

def codificaRLC(mensaje):
    ba=bytearray()
    cont=1
    car_actual=mensaje[0]
    for x in range(1,len(mensaje)):
        if mensaje[x]==car_actual:
            cont+=1
        else:
           ba.append(ord(car_actual))
           ba.append(cont)  #si el caracter se repite mas de 255 veces, solo cuenta 255
           cont=1
           car_actual=mensaje[x]
    ba.append(ord(car_actual)) #agrego el ultimo caracter
    ba.append(cont)
    for b in ba:
        print(format(b, '08b'))
    return ba

def tasa_de_compresion(mensaje: str, mensaje_codificado:bytearray):
    tam_original = len(mensaje.encode('utf-8'))
    tam_codificado = len(mensaje_codificado)
    tasa = tam_original / tam_codificado if tam_codificado != 0 else 0
    return tasa

mensaje="UUOOOOAAAIEUUUU"
mensaje_codificado=codificaRLC(mensaje)
print("la tasa de compresion es:",tasa_de_compresion(mensaje,mensaje_codificado))