[]

import math
import random

"""
    [[0.4,0.6,0,0],
    [0,0,0.5,0.5],
    [0,0,0.7,0.3]]

    [[0.2,0.3,0.5],
    [0,0,1],
    [0,0,1]]

    [[0.4,0,0.2,0.4],
       [0.4,0.3,0.2,0.1],
       [0,0.3,0,0.7]]

    [[0,0.5,0,0.5],
    [0.8,0,0.2,0],
    [0,0.5,0,0.5],
    [0.8,0,0.2,0]]
"""

mat = [[0.4,0.6,0,0],
    [0,0,0.5,0.5],
    [0,0,0.7,0.3]]

# genera alfabetos automáticos
def AlfEnt(mat): return [str(i) for i in range(len(mat))]
def AlfSal(mat):  return [str(j) for j in range(len(mat[0]))]

# P(bj)
def ProbsBj(matCanal,probsAi,alfSal):
    probsBj = [0] * len(matCanal[0])

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            probsBj[j] += matCanal[i][j] * probsAi[i]

    return probsBj

# P(ai,bj)
def ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal):
    
    matSS = [[0 for _ in alfSal] for _ in alfEnt] # matriz del mismo tamaño

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            matSS[i][j] = matCanal[i][j] * probsAi[i]

    return matSS

# P(ai/bj)
def ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal):

    matPost = [[0 for _ in alfSal] for _ in alfEnt] # matriz del mismo tamaño
    probsBj = ProbsBj(matCanal,probsAi,alfSal)

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            if probsBj[j] != 0:
              matPost[i][j] = (matCanal[i][j] * probsAi[i]) / probsBj[j]
            else: matPost[i][j] = 0
    return matPost

# Informacion Mutua I(A,B)
def InfoMutua (matCanal,probsAi,alfEnt,alfSal):

    matSS = ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal)
    matPost = ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal)
    Iab = 0

    for i in range(len(matSS)):
        for j in range(len(matSS[i])):
            if (matPost[i][j] > 0):
                Iab += matSS[i][j] * math.log(matPost[i][j] / probsAi[i],2)

    print(f"I(A,B) - Informacion Mutua: {Iab: .4f}")

    return Iab

# booleana
def CanalDeterminante(mat):
    det = True
    i = 0

    while(i in range(len(mat)) and det):
        det = (sum(1 for j in range(len(mat[0])) if mat[i][j] != 0)) == 1
        i += 1
    
    if (det): print("Canal determinante")
    else: print("Canal NO determinante")

    #return det


def EsCombLineal(col1, col2):
    tol=1e-9
    i = 0
    comb = True # asumo combinable

    while (i < len(col2) and abs(col2[i]) < tol):
        i += 1

    if (i < len(col2)):  # encontro un elemento distinto de cero
        cte = col1[i] / col2[i]
        k = 0

        while (k < len(col1) and comb):
            a = col1[k]
            b = col2[k]

            if abs(b) < tol:
                if abs(a) >= tol:  # col2 tiene 0 pero col1 no, no pueden ser proporcionales
                    comb = False
            else:
                if abs((a / b) - cte) >= tol:  # si el cociente no coincide con la constante
                    comb = False

            k += 1

    else:
        comb = all(abs(a) < tol for a in col1) # si col2 es toda 0, tiene que verificar que col1 tambien

    return comb

def VerificaCombinables(mat):
    comb = False
    j = 0
    b1 = b2 = -1 # si no son combinables va a devolver -1

    while (j < len(mat[0]) and not comb):
        col1 = [fila[j] for fila in mat] # me quedo con la columna
        k = j + 1
        while(k < len(mat[0]) and not comb): # recorro las demas columnas
            col2 = [fila[k] for fila in mat] # separo la columna en la que estoy parada
            comb = EsCombLineal(col1,col2) # verifico combinacion lineal
            if (comb):
                b1 = j
                b2 = k
            k += 1
        j += 1

    return b1,b2 # devuelvo los indices de las columnas combinables

def GeneraMatrizDeterminante(mat,b1,b2):
    
    # NxM * MxK = NxK donde K=M-1 (matDet tiene que ser de M x M-1)
    filasM = len(mat[0]) # cantFilas == cant columnas de mat original
    colK = filasM - 1 # cantCol es == a la cantidad de columnas originales - 1

    matDet = [[0 for _ in range(colK)] for _ in range(filasM)] # inicializo matriz con 0

    cant = 0
    for i in range(0, filasM):

        if(i == b2):
            matDet[b2] = matDet[b1].copy()
        else:
            matDet[i][cant] = 1    
            cant+=1

    return matDet


def MatrizReducida (matCanal):
    
    matRed = [fila[:] for fila in matCanal]
    # PARA PASO A PASO
    # Matriz original:
    for fila in matRed: print(fila)
    probsAi = [1/len(matRed)] * len(matRed) #asumo equiprob
    InfoMutua(matRed,probsAi,AlfEnt(matRed),AlfSal(matRed)) # calculo info mutua cada paso

    b1,b2 = VerificaCombinables(matRed)

    while (b1 != -1):
        matDet = GeneraMatrizDeterminante(matRed,b1,b2)

        N = len(matRed)
        M = len(matRed[0])
        K = len(matDet[0])

        # obtengo matriz NxK donde N es filas de mat1 y K columnas de mat2
        matAux = [[0 for _ in range(K)] for _ in range(N)]

        for i in range(N):
            for t in range(K):
                suma = 0
                for j in range(M):
                    suma += matRed[i][j] * matDet[j][t]
                matAux[i][t] = suma

        matRed = [fila[:] for fila in matAux]

        b1,b2 = VerificaCombinables(matRed)

        # PARA PASO A PASO
        for fila in matRed: print(fila)
        probsAi = [1/len(matRed)] * len(matRed) #asumo equiprob
        InfoMutua(matRed,probsAi,AlfEnt(matRed),AlfSal(matRed)) # calculo info mutua cada paso

    # for fila in matRed: print(fila) # SI NO PONGO EL PASO A PASO, ASI ME MUESTRA RESULT
    CanalDeterminante(matRed)

    # return matRed

MatrizReducida(mat)