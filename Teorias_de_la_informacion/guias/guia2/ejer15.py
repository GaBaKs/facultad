import math
from libreria import *
import random


cad = "CAAACCAABAACBBCABACCAAABCBBACCDEFG"


simbolos,cant=cuentasimbolos(cad)

prob=probabilidadlista(simbolos,cant)

def MatrizDeTransicion (simbolos,cad):
    matT = [ [0 for _ in range(len(simbolos))] for _ in range(len(simbolos))]
    cadL = list(cad) #a la cadena la hago lista
    for i in range(len(simbolos)):
        for j in range(len(simbolos)):
            canti = 0
            for k in range(len(cadL) - 1): #cuento apariciones de la dupla
                if cadL[k] == simbolos[i] and cadL[k+1] == simbolos[j]:
                    canti += 1
            matT[i][j] = canti # pongo cant de la dupla en la ubicacion de la matriz

    for j in range(len(matT)):
        tot = 0
        for i in range(len(matT)):
            tot += matT[i][j] #sumo cantidades de esa letra por columna
        
        for i in range(len(matT)):
            matT[i][j] = matT[i][j] / tot
    
    return matT

matT=MatrizDeTransicion (simbolos,cad)

for fila in matT:
    print([f"{val: .2f}" for val in fila])


#b

def getcolumna(matriz,alfabeto,caracter):
    aux=[]
    for i in matriz:
        aux.append(i[alfabeto.index(caracter)])
    
    return aux

def simularMensaje(simbolos,matriz,longitud1,simbolo_inicial):
    mensaje = []
    if simbolo_inicial == '':
        simbolo_inicial = random.choice(simbolos)[0]
    mensaje.append(simbolo_inicial)
    longitud1 -= 1
    for x in range(longitud1):
        simbolo_actual = mensaje[-1]
        columna=getcolumna(matriz,simbolos,simbolo_actual)
        siguiente_simbolo=random.choices(simbolos,weights=columna,k=1)[0]
        mensaje.append(siguiente_simbolo)

    return mensaje

print(simularMensaje(simbolos,matT,10,''))

#c

tipofuente (matT, 0.1)
