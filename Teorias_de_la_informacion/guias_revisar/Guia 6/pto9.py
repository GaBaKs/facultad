[]

import math
import itertools

"""

[[0.60,0.40],
[0.20,0.80]]

[[0.25,0.75],
[0.90,0.10]]

[[0.51,0.49],
[0.72,0.28]]

[[0.77,0.23],
[0.20,0.80]]

"""
mat = [[0.77,0.23],
[0.20,0.80]]

# genera alfabetos automáticos
def AlfEnt(mat): return [str(i) for i in range(len(mat))]
def AlfSal(mat):  return [str(j) for j in range(len(mat[0]))]

def VerificaCanalUniforme(mat):

    u = True # asumo uniformidad
    i = 1 # empiezo desde la segunda fila
    primera = mat[0]
    tol=1e-9 # establezco una tolerancia

    while (i < len(mat) and u):
        fila = mat[i]
        primera = mat[0]

        # ordeno las filas que voy a comparar
        fila = sorted(fila)
        primera = sorted(primera)

        j = 0
        while (j < len(fila) and u):
            if (abs(fila[j] - primera[j]) >= tol):
                u = False
            j += 1
        i += 1

    return u

def CapacidadDeterminante(mat):
    return math.log(len(mat[0]))

def CapacidadSinRuido(mat):
    return math.log(len(mat))

def Entropia(prob,r): # r = len(AlfabetoCodigo(codigo)) PARA CODIGOS COMPACTOS
    h=0 
    for p in prob:
        h += p * math.log(1/p,r)
    
    return h

def CapacidadUniforme (mat):

    h = 0
    for fila in mat:
        h += Entropia(fila,2)

    return math.log(len(mat[0])) - h

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

    return Iab

def CapacidadCanal(matCanal, paso):
    alfEnt = AlfEnt(matCanal) # genero los alfabetos
    alfSal = AlfSal(matCanal)
    
    n = len(matCanal) # num entradas
    
    cantPasos = int(round(1.0 / paso)) # numero de pasos discretos en [0,1]
    valores = [round(i * paso, 10) for i in range(cantPasos + 1)] # lista de valores permitidos segun el paso

    maxI = -1 # inicializo mi info mutua
    maxProbs = [] # inicializo las mejores probabilidades
    tol = 1e-9

    for comb in itertools.product(valores, repeat= n - 1): # para cada tupla
        sumaParcial = sum(comb) # calculo suma parcial de las primeras n-1 probs
        ult = round(1.0 - sumaParcial, 10) # deduzco ultima prob

        if (-tol <= ult and ult <= 1 + tol): 
            rem = ult / paso # compruebo q ult entra

            if (abs(rem - round(rem)) <= 1e-8): # compruebo que rem sea entero
                probsAi = list(comb) + [round(ult,10)] # construyo posible probsAi

                if(not (abs(sum(probsAi) - 1.0) > 1e-6)): # verifico que la posibilidad es coherente (que sume aprox 1)
                    Iab = InfoMutua(matCanal,probsAi,alfEnt,alfSal) # si cumple, calculo la info mutua de la matriz con estas probs
                    
                    if (Iab > maxI): # si es mayor, guardo los valores
                        maxI = Iab
                        maxProbs = probsAi

    print(f"Capacidad: {maxI: .4f}")
    print("p optima: ",min(maxProbs))
    #return maxI, maxProbs

CapacidadCanal(mat,0.0001)