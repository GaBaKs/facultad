[]

import math

probsAi = [2/5,3/5]
matCanal = [[3/5,2/5],
            [1/3,2/3]]
alfEnt = ['0','1']
alfSal = ['0','1']

# Devuelve alfabeto y sus probabilidades
def  AlfabetoProbabilidades(mensaje):
    cuentas=[]
    simbolos=[]

    for car in mensaje:
        if car in simbolos:
            cuentas[simbolos.index(car)]+=1
        else:
            simbolos.append(car)
            cuentas.append(1)
    
    n=len(mensaje)
    prob = [c/len(mensaje) for c in cuentas]
    return prob,simbolos

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

    #return hPost

# Entropia A Priori
hA = Entropia(probsAi,2)
print(f"H(A): {hA: .4f}")
EntropiaAPosteriori(matCanal,probsAi,alfEnt,alfSal)