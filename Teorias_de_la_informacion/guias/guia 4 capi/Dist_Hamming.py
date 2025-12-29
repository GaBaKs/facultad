def distancia_hamming(cad1,cad2):
    """Calcula la distancia de Hamming entre dos cadenas de igual longitud.
    Si las cadenas no tienen la misma longitud, devuelve -1."""
    if len(cad1) != len(cad2):
        return -1
    distancia = 0
    for a, b in zip(cad1, cad2):
        if a != b:
            distancia += 1
    return distancia

def distancia_minima(cod):
    """Calcula la distancia mínima entre todas las parejas de códigos en una lista.
    Si la lista tiene menos de dos códigos, devuelve -1."""
    if len(cod) < 2:
        return -1
    min_distancia = float('inf')
    for i in range(len(cod)):
        for j in range(i + 1, len(cod)):
            dist = distancia_hamming(cod[i], cod[j])
            if dist != -1 and dist < min_distancia:
                min_distancia = dist
    return min_distancia if min_distancia != float('inf') else -1

def cant_errores_posibles(distancia):
    """Calcula la cantidad de errores que se pueden detectar y corregir
    con un código de Hamming de una distancia dada.
    Devuelve una tupla (errores_detectables, errores_corregibles)."""
    errores_detectables = distancia - 1
    errores_corregibles = (distancia - 1) // 2 # División entera
    return errores_detectables, errores_corregibles
def hamming_completo(cod):
    if not cod:
        return -1,-1,-1
    dist_min = distancia_minima(cod)
    errores_detectables, errores_corregibles = cant_errores_posibles(dist_min)
    return dist_min, errores_detectables, errores_corregibles

"""cod1=["00","01","10","11"]
cod2=["000","100","101","111"]
cod3=["0000","0011","1010","0101"]
dist,errores_detectables,errores_corregibles=hamming_completo(cod1)
print("La distancia mininima del cod 1 es:",dist)
print("Cantidad de errores detectables y corregibles del cod 1:",errores_detectables,errores_corregibles)
dist,errores_detectables,errores_corregibles=hamming_completo(cod2)
print("La distancia mininima del cod 2 es:",dist)
print("Cantidad de errores detectables y corregibles del cod 2:",errores_detectables,errores_corregibles)
dist,errores_detectables,errores_corregibles=hamming_completo(cod3)
print("La distancia mininima del cod 3 es:",dist)
print("Cantidad de errores detectables y corregibles del cod 3:",errores_detectables,errores_corregibles)"""