import math

#-------------------------------- EJERCICIO 24 ---------------------------------
# Desarrollar funciones en Python que resuelvan lo siguiente:
# a. Dado un carácter, devolver un byte que represente su código ASCII (7 bits) y utilice
# el bit menos significativo para almacenar la paridad del código.
# b. Dado un byte que se obtuvo como resultado de la función anterior, verificar si es
# correcto o tiene errores.
#-------------------------------- EJERCICIO 24 ---------------------------------

def paridad_caracter(caracter):
    byte = []
    val = bin(ord(caracter))
    for x in val[2:]: #Se saltea el '0b' inicial
        byte.append(x)
    if val.count('1') % 2 == 0:
        byte.append('0') #Bit de paridad par
    else:
        byte.append('1') #Bit de paridad impar
    return byte
    
def verifica_paridad(byte):
    x = byte.copy()
    paridad = x.pop()
    cantidad_unos = x.count('1')
    flag = False
    if cantidad_unos % 2 == 0 and paridad == '0': #Cantidad de 1s par -> bit de paridad = 0
        flag = True
    else:
        if cantidad_unos % 2 != 0 and paridad == '1': #Cantidad de 1s impar -> bit de paridad = 1
            flag = True
    return flag

caracter = 'F'
byte = paridad_caracter(caracter)

print("El byte es correcto? -> ",verifica_paridad(byte))

# Dado un caracter (7 bits) cuento la cantidad de 1s en su representacion binaria (ascci) y le agrego un octavo bit de paridad
# Luego para verificarlo unicamente cuento la cantidad de 1s y compruebo si coincide con el bit de paridad
