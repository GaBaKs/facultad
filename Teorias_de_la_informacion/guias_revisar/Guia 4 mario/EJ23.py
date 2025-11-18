import math

#-------------------------------- EJERCICIO 23 ---------------------------------
# Dados los siguientes códigos que representan colores:
#        [Rojo, Amarillo, Verde, Azul] 
# cod1 = ['0100100','0101000','0010010','0100000']
# cod2 = ['0100100','0010010','0101000','0100001']
# cod3 = ['0110000','0000011','0101101','0100110']
# a. Obtener sus distancias de Hamming
# b. Especificar cúantos errores se pueden detectar y corregir en cada caso
#-------------------------------- EJERCICIO 23 ---------------------------------

def distancia_hamming(cod):
    hamming = -1
    N = len(cod)
    for i in range(N):
        for j in range(i+1,N):
            cont = 0
            for s1,s2 in zip(cod[i],cod[j]):
                if(s1 != s2):
                    cont += 1
            if cont < hamming or hamming == -1:
                hamming = cont
    return hamming
    
def errores_detectables(hamming):
    cant = 0
    if hamming >= 2: #Si no se cumple se devuelve 0
        cant = hamming-1
    return cant

def errores_corregibles(hamming):
    cant = 0
    if hamming >= 2: #Si no se cumple se devuelve 0
        cant = (hamming-1) / 2 
    return math.floor(cant) #Aplica piso a la division para devolver un entero

cod1 = ['0100100','0101000','0010010','0100000']
cod2 = ['0100100','0010010','0101000','0100001']
cod3 = ['0110000','0000011','0101101','0100110']


hamming = distancia_hamming(cod3)
print("Distancia de Hamming del codigo: ",hamming)

errores_detectables = errores_detectables(distancia_hamming(cod3))
print("Cantidad de errores detectables en el codigo: ",errores_detectables)

errores_corregibles = errores_corregibles(distancia_hamming(cod3))
print("Cantidad de errores corregibles en el codigo: ",errores_corregibles)