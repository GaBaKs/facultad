[]

import math

mat1 = [[0.7,0,0.3,0],
             [0.2,0.6,0,0.2]]

mat2 = [[0.9,0,0.1],
       [0,1,0],
       [0.1,0.1,0.8],
       [0,0.5,0.5]]

# HACER FUNCION PARA QUE HAGA LOS ALFABETOS Y
# LAS PROBS AI SI NO ME LO DAN
alfEnt2 = ["1","2","3","4"]
alfSal2 = ["1","2","3"]
probsAi1 = [1/len(mat1)] * len(mat1)
alfSal1 = ["1","2","3","4"]


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

# P(ai,bj)
def ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal):
    
    matSS = [[0 for _ in alfSal] for _ in alfEnt] # matriz del mismo tamaño

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            matSS[i][j] = matCanal[i][j] * probsAi[i]

    return matSS

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

def MatrizCanalCompuesto(matAB,matBC,probsAiAB):

    r = len(mat1)
    s = len(mat1[0]) # len(matBC)
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



# PARA CANALES EN SERIE LAS ENTRADAS SON LA SALIDA DEL ANTERIOR
probsAi2 = ProbsBj(mat1,probsAi1,alfSal1)
Equivocacion(mat2,probsAi2,alfSal2,alfEnt2)
InfoMutua(mat2,probsAi2,alfEnt2,alfSal2)
MatrizCanalCompuesto(mat1,mat2,probsAi1)