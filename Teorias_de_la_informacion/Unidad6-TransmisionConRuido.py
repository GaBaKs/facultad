[]

import math
import itertools

# TRANSMISION DE LA INFORMACION EN CANALES CON RUIDO - UNIDAD 6

"""
-------- GENERALES QUE NECESITO -----------------------------------------------------------------------------------------------------------

ProbabilidadesAPosteriori esta cambiada con respecto a la que uso en la unidad 5 (verifica ceros)


PARA PROBABILIDADES EQUIPROBABLES
probsAi = [1/len(mat)] * len(mat)
"""

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

# P(ai,bj)
def ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal):
    
    matSS = [[0 for _ in alfSal] for _ in alfEnt] # matriz del mismo tamaño

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            matSS[i][j] = matCanal[i][j] * probsAi[i]

    return matSS

# Informacion Mutua I(A,B) ------------------- USA DE ACA PARA ARRIBA
def InfoMutua (matCanal,probsAi,alfEnt,alfSal):

    matSS = ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal)
    matPost = ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal)
    Iab = 0

    for i in range(len(matSS)):
        for j in range(len(matSS[i])):
            if (matPost[i][j] > 0):
                Iab += matSS[i][j] * math.log(matPost[i][j] / probsAi[i],2)

    print(f"I(A,B) - Informacion Mutua: {Iab: .4f}")

    #return Iab 


# mandando probsAi,2 es la entropia a priori
def Entropia(prob,r): # r = len(AlfabetoCodigo(codigo)) PARA CODIGOS COMPACTOS
    h=0 
    for p in prob:
        if (p != 0):
            h += p * math.log(1/p,r)
    
    return h

# H(A/bj)
def EntropiaAPosteriori (matCanal,probsAi,alfEnt,alfSal):
    hPost = []

    probsBj = ProbsBj(matCanal,probsAi,alfSal)
    matPost = ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal)

    for j in range(len(alfSal)): # por cada simbolo de salida
        col = [matPost[i][j] for i in range(len(alfEnt))] # P(ai/bj)
        h = Entropia(col,2) # entropia de la columna
        hPost.append(h) # agrego a mi lista

    return hPost

# H(A|B)
def Equivocacion (matCanal,probsAi,alfSal,alfEnt):

    probsBj = ProbsBj(matCanal,probsAi,alfSal)
    hPost = EntropiaAPosteriori(matCanal,probsAi,alfEnt,alfSal)
    hAB = 0

    for j in range((len(probsBj))):
        hAB += probsBj[j] * hPost[j]

    print(f"H(A|B) - Equivocacion: {hAB:.4f}")

    #return hAB

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

    #return Iab

"""
-------------------------------------------------------------------------------------------------------------------------
"""


# ---------------------------------------------- VERIFICA CANAL SIN RUIDO O DETERMINANTE ---------------------------------------------- #

"""
----- RECIBE - Matriz del canal
"""

# funcion booleana, devuelve si es un canal sin ruido
def CanalSinRuido(matCanal):
    sinRuido = True
    j = 0

    while(j in range(len(matCanal[0])) and sinRuido):
        sinRuido = (sum(1 for i in range(len(matCanal)) if matCanal[i][j] != 0)) == 1
        j += 1
    
    if (sinRuido): print("Canal SIN ruido")
    else: print("Canal CON ruido")

    #return sinRuido

# --------------- #

# funcion booleana, devuelve si es un canal determinante
def CanalDeterminante(matCanal):
    det = True
    i = 0

    while(i in range(len(matCanal)) and det):
        det = (sum(1 for j in range(len(matCanal[0])) if matCanal[i][j] != 0)) == 1
        i += 1
    
    if (det): print("Canal determinante")
    else: print("Canal NO determinante")

    #return det

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- MATRIZ DEL CANAL COMPUESTO ---------------------------------------------- #

"""
----- RECIBE - Matriz canal 1, matriz canal que se forma por la salida del 1, probs a priori del canal 1

CANAL EN SERIE, LA ENTRADA DEL SEGUNDO ES LA SALIDA DEL ANTERIOR 
"""

def MatrizCanalCompuesto(matAB,matBC,probsAiAB):

    r = len(matAB)
    s = len(matAB[0]) # len(matBC)
    t = len(matBC[0])

    matComp = [[0 for _ in range(t)] for _ in range(r)]

    for i in range(r):
        for k in range(t):
            suma = 0
            for j in range(s):
                suma += matAB[i][j] * matBC[j][k]
            matComp[i][k] = suma
    
    alfEnt= [str(i) for i in range(len(matAB))]
    alfSal = [str(j) for j in range(len(matBC[0]))]

    print("Matriz del Canal Compuesto:")
    for i in range(len(matComp)): # i es el índice de la fila
        for j in range(len(matComp[i])): # j es el índice de la columna
            print(f"  ({alfEnt[i]}, {alfSal[j]}) = {matComp[i][j]: .4f}", end=" ")
        print() # salto de línea para pasar a la siguiente fila

    print("Equivocacion e Informacion Mutua del Canal Compuesto")
    Equivocacion(matComp,probsAiAB,alfSal,alfEnt)
    InfoMutua(matComp,probsAiAB,alfEnt,alfSal)


    #return matComp

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- MATRIZ REDUCIDA - REDUCCION SUFICIENTE ---------------------------------------------- #

"""
VERIFICAN QUE HAYA COLUMNAS COMBINABLES, GENERA LA MATRIZ DETERMINANTE Y REDUCE TODO LO QUE PUEDE, OBTENIENDO
UNA MATRIZ EN CADA PASO E INFORMANDO TMB LA INFO MUTUA EN CADA PASO(para ver que no cambie)

PARA HACER LA REDUCCION SUFICIENTE, NECESITO TODAS LAS FUNCIONES DE ESTA SECCION

---- USA - SOLO SI HACE PASO POR PASO DE LA RED SUF. --> ProbsBj, Probs Suceso Simultaneo, Probs a Posteriori, Info Mutua

---- RECIBEN - Matriz del canal - Para generar matriz det tmb necesito los indices de las dos columnas combinables

"""

# ------ BUSCA COLUMNAS COMBINABLES ------ #

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

# devuelve los indices de las columnas combinables, o -1 si no las hay
def VerificaCombinables(matCanal):
    comb = False
    j = 0
    b1 = b2 = -1 # si no son combinables va a devolver -1

    while (j < len(matCanal[0]) and not comb):
        col1 = [fila[j] for fila in matCanal] # me quedo con la columna
        k = j + 1
        while(k < len(matCanal[0]) and not comb): # recorro las demas columnas
            col2 = [fila[k] for fila in matCanal] # separo la columna en la que estoy parada
            comb = EsCombLineal(col1,col2) # verifico combinacion lineal
            if (comb):
                b1 = j
                b2 = k
            k += 1
        j += 1

    return b1,b2 # devuelvo los indices de las columnas combinables


# ------ GENERA MATRIZ DETERMINANTE PARA PODER MULTIPLICAR ------ #

def GeneraMatrizDeterminante(matCanal,b1,b2):
    
    # NxM * MxK = NxK donde K=M-1 (matDet tiene que ser de M x M-1)
    filasM = len(matCanal[0]) # cantFilas == cant columnas de mat original
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


# ------ REDUCCIONES SUFICIENTES INFORMANDO INFO MUTUA EN CADA PASO ------ #

def MatrizReducida (matCanal):
    
    matRed = [fila[:] for fila in matCanal]

    # PARA PASO A PASO --------- SACARLO SI NO LO PIDEN
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

        # PARA PASO A PASO ------- SACARLO SI NO LO PIDEN
        for fila in matRed: print(fila)
        probsAi = [1/len(matRed)] * len(matRed) #asumo equiprob
        InfoMutua(matRed,probsAi,AlfEnt(matRed),AlfSal(matRed)) # calculo info mutua cada paso

    #for fila in matRed: print(fila) # SI NO PONGO EL PASO A PASO, ASI ME MUESTRA RESULT
    #CanalDeterminante(matRed) # Comprueba si se obtiene un canal determinante

    # return matRed

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- VERIFICA CANAL UNIFORME ---------------------------------------------- #

"""
---- RECIBE - Matriz del canal
"""

def VerificaCanalUniforme(matCanal):

    u = True # asumo uniformidad
    i = 1 # empiezo desde la segunda fila
    primera = matCanal[0]
    tol=1e-9 # establezco una tolerancia

    while (i < len(matCanal) and u):
        fila = matCanal[i]
        primera = matCanal[0]

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

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- CAPACIDAD DE UN CANAL ---------------------------------------------- #

"""
---- RECIBE - Matriz del canal
"""

# ------ CASOS ESPECIALES ------ #

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

# ------ GENERAL ------ #

''' USA - Info mutua y todo lo que esa necesita '''

# paso = 0.0001 
# import iteltools
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

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- PROBABILIDAD DE ERROR ---------------------------------------------- #

"""
---- USA - TAL CUAL ESTA ACA, COPIAR Y PEGAR

---- RECIBE - Matriz del canal, probsAi
"""

def ReglaDeDecisionMax (matCanal):

    d = []

    for j in range(len(matCanal[0])): # para cada columna
        maxProb = -1
         
        for i in range(len(matCanal)): # busco maximo elemento (mayor prob)
            if (matCanal[i][j] > maxProb):
                maxProb = matCanal[i][j]
                iMax = i
        d.append(iMax) # armo lista con los indices
    
    return d


def ProbabilidadDeError (matCanal, probsAi):
    
    pE = 0
    d = ReglaDeDecisionMax(matCanal)

    for j in range(len(matCanal[0])): # recorro por columnas
        iMax = d[j]
        for i in range(len(matCanal)): # recorro cada elemento de la columna
            if (i != iMax): # si es un error
                pE += probsAi[i] * matCanal[i][j]

    print(f"Pe - Probabilidad de Error: {pE: .4f}")

    #returnpE

# --------------------------------------------------------------------------------------------------------------------- #
