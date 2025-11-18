import math
#-------------------------------- EJERCICIO 22 ---------------------------------
# Implementar una función en Python que reciba una lista de cadenas de caracteres que
# representa una codificación binaria y devuelva: la distancia de Hamming, la cantidad de
# errores que se pueden detectar y la cantidad de errores que se pueden corregir.
#-------------------------------- EJERCICIO 22 ---------------------------------

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

cod = ['0000', '0011', '1010', '0101']

hamming = distancia_hamming(cod)
print("Distancia de Hamming del codigo: ",hamming)

errores_detectables = errores_detectables(distancia_hamming(cod))
print("Cantidad de errores detectables en el codigo: ",errores_detectables)

errores_corregibles = errores_corregibles(distancia_hamming(cod))
print("Cantidad de errores corregibles en el codigo: ",errores_corregibles)

# La distancia de Hamming representa la diferencia entre 2 codigos de igual longitud, ya que analiza bit a bit
# Para calcularla comparo 2 codigos de igual longitud y si el bit difiere sumo 1
# Gracias a esto calculo los errores y con esto puedo analizar si el codigo es corregible o no
