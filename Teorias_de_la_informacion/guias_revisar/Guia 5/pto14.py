[]

import math

probsAi = [0.70,0.30]
matCanal = [[0.7,0.3],
            [0.4,0.6]]

alfEnt = ['0','1']
alfSal = ['0','1']

def MuestraSimbolos (simbolos,prob):
    for s,p in zip(simbolos,prob):
        print(f"{s}: {p: .4f}")

# P(bj)
def ProbsBj(matCanal,probsAi,alfSal):
    probsBj = [0] * len(matCanal[0])

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            probsBj[j] += matCanal[i][j] * probsAi[i]
    
    print(f"P(bj):")
    MuestraSimbolos(alfSal,probsBj)

    return probsBj

# P(ai/bj)
def ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal):

    matPost = [[0 for _ in alfSal] for _ in alfEnt] # matriz del mismo tamaño
    probsBj = ProbsBj(matCanal,probsAi,alfSal)

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            matPost[i][j] = (matCanal[i][j] * probsAi[i]) / probsBj[j]
    
    # Muestra matriz segun par (i,j)
    print("P(ai/bj) - Matriz de Probs A Posteriori:")
    for i in range(len(matPost)): # i es el índice de la fila
        for j in range(len(matPost[i])): # j es el índice de la columna
            print(f"  ({alfEnt[i]}, {alfSal[j]}) = {matPost[i][j]: .4f}", end=" ")
        print() # salto de línea para pasar a la siguiente fila

    return matPost

# mandando probsAi,2 es la entropia a priori
def Entropia(prob,r): # r = len(AlfabetoCodigo(codigo)) PARA CODIGOS COMPACTOS
    h=0 
    for p in prob:
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

    print("Entropia A Posteriori")
    print([f"{elem: .4f}" for elem in hPost])

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

# H(B/ai)
def EntropiaSalidaCondicionada (matCanal,probsAi):
    hCond = []

    for i in range(len(probsAi)):
        fila = matCanal[i]
        h = Entropia(fila,2)
        hCond.append(h)
    
    return hCond


# H(B|A) = sumatoria de P(ai) * H(B/ai)
def Perdida (matCanal,probsAi):

    hBA = 0
    hCond = EntropiaSalidaCondicionada(matCanal,probsAi)

    for i in range(len(probsAi)):
        hBA += probsAi[i] * hCond[i]

    print(f" H(B|A) - Perdida: {hBA: .4f}")

    #return hBA

# P(ai,bj)
def ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal):
    
    matSS = [[0 for _ in alfSal] for _ in alfEnt] # matriz del mismo tamaño

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            matSS[i][j] = matCanal[i][j] * probsAi[i]

    print("P(ai,bj) - Matriz de Probs de Suceso Simultaneo:")
    for i in range(len(matSS)): # i es el índice de la fila
        for j in range(len(matSS[i])): # j es el índice de la columna
            print(f"  ({alfEnt[i]}, {alfSal[j]}) = {matSS[i][j]: .4f}", end=" ")
        print() # salto de línea para pasar a la siguiente fila

    return matSS

# H(A,B)
def EntropiaAFin (matCanal,probsAi,alfEnt,alfSal):

    matSS = ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal)
    hAFin = 0

    for i in range(len(matSS)):
        for j in range(len(matSS[i])):
            p = matSS[i][j]
            hAFin += p * math.log(1/p,2)

    print(f" H(A,B) - Entropia A Fin: {hAFin: .4f}")

    #return hAFin


# Informacion Mutua I(A,B)
def InfoMutua (matCanal,probsAPriori,alfEnt,alfSal):

    matSS = ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal)
    matPost = ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal)
    Iab = 0

    for i in range(len(matSS)):
        for j in range(len(matSS[i])):
            Iab += matSS[i][j] * math.log(matPost[i][j] / probsAi[i],2)

    print(f"I(A,B) - Informacion Mutua: {Iab: .4f}")

    #return Iab

Equivocacion(matCanal,probsAi,alfSal,alfEnt)
Perdida(matCanal,probsAi)
EntropiaAFin(matCanal,probsAi,alfEnt,alfSal)
InfoMutua(matCanal,probsAi,alfEnt,alfSal)