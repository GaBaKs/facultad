[]

import math

# CANALES PARA LA TRANSMISION DE LA INFORMACION - UNIDAD 5

"""
-------- GENERALES QUE NECESITO -----------------------------------------------------------------------------------------------------------
"""

'''
PARA USAR LAS FUNCIONES QUE HICE

# SI ME DAN CADENAS DE CARACTERES Y TENGO QUE GENERAR LA MATRIZ DEL CANAL
probsAi,alfEnt = AlfabetoProbabilidades(entrada) #probsAi son P(ai), probs a priori
probsaux,alfSal = AlfabetoProbabilidades(salida) # obtengo alfabeto de la salida

matCanal = MatrizDelCanal(entrada,salida,alfEnt,alfSal) # ALFABETOS NECESARIOS


# SI ME DAN LA MATRIZ
hacer alfabetos aleatorios para mostrar
# genera alfabetos automáticos
def AlfEnt(mat): return [str(i) for i in range(len(mat))]
def AlfSal(mat):  return [str(j) for j in range(len(mat[0]))]

alfEnt = AlfEnt(matCanal)
alfSal = AlfSal(matCanal)


# EXTRA
# Muestro P(ai)
print("P(ai) - Probabilidades A Priori:")
MuestraSimbolos(alfEnt,probsAi)
'''

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

# mandando probsAi,2 es la entropia a priori
# print(f"H(A): {hA: .4f}")
def Entropia(prob,r): # r = len(AlfabetoCodigo(codigo)) PARA CODIGOS COMPACTOS
    h=0 
    for p in prob:
        h += p * math.log(1/p,r)
    
    return h

# Muestra cada simbolo enlistado con su probabilidad
def MuestraSimbolos (simbolos,prob):
    for s,p in zip(simbolos,prob):
        print(f"{s}: {p: .4f}")

"""
-------------------------------------------------------------------------------------------------------------------------
"""



# ---------------------------------------------- MATRIZ DEL CANAL ---------------------------------------------- #

"""
----- USA - AlfabetoProbabilidades 

----- RECIBE - mensaje de entrada, mensaje de salida (cadenas de caracteres), alfabeto de entrada y alfabeto de salida

        ALFABETOS NECESARIOS XQ LOS USA PARA CALCULAR DIMENSION DE LA MATRIZ
"""

# P(bj/ai)
def MatrizDelCanal(entrada,salida,alfEnt,alfSal): # Obtiene y muestra la matriz del canal a partir de las cadenas de entrada y salida

    mat = [ [0] * len(alfSal) for _ in range(len(alfEnt)) ] # inicializo matriz

    # veo el simbolo de entrada y su correspondiente simbolo de salida
    for simbEnt, simbSal in zip(entrada,salida): # zip junta los elem de ambas cadenas por posicion
        mat[alfEnt.index(simbEnt)][alfSal.index(simbSal)] += 1 # en mat(i,j) sumo cant veces que entro ai y salio bj

    for i in range(len(mat)):
        cantAi= sum(mat[i]) # cuento cant apariciones del simbolo de entrada (ai)
        if cantAi != 0:
            mat[i] = [elem / cantAi for elem in mat[i]] # divido toda la fila por la cantidad de apariciones, para obtener prob condicional
        
    # Muestra matriz segun par (i,j)
    for i in range(len(mat)): # i es el índice de la fila
        for j in range(len(mat[i])): # j es el índice de la columna
            print(f"  ({alfEnt[i]}, {alfSal[j]}) = {mat[i][j]: .4f}", end=" ")
        print() # salto de línea para pasar a la siguiente fila

    #return mat

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- P(bj) - PROBABILIDAD SIMBOLOS DE SALIDA ---------------------------------------------- #

"""
----- RECIBE - Matriz del canal, probs a priori, alf salida
"""

# P(bj)
def ProbsBj(matCanal,probsAi,alfSal):
    probsBj = [0] * len(matCanal[0])

    for i in range(len(matCanal)):
        for j in range(len(matCanal[i])):
            probsBj[j] += matCanal[i][j] * probsAi[i]

    print(f"P(bj):")
    MuestraSimbolos(alfSal,probsBj)

    return probsBj

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- P(ai/bj) - PROBABILIDADES A POSTERIORI ---------------------------------------------- #

"""
----- USA - ProbsBj

----- RECIBE - matriz del canal, probs a priori, alfabetos

    ALFABETOS SOLO PARA MOSTRAR LA MATRIZ
"""

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

    #return matPost

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- P(ai,bj) - PROBABILIDAD DEL SUCESO SIMULTANEO ---------------------------------------------- #

"""
----- RECIBE - matriz del canal, probs a priori, alfabetos

    ALFABETOS SOLO PARA MOSTRAR LA MATRIZ
"""

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

    #return matSS

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- H(A/bj) - ENTROPIA A POSTERIORI ---------------------------------------------- #

"""
---- USA - ProbsBj, ProbabilidadesAPosteriori

----- RECIBE - matriz del canal, probs a priori, alfabetos

    ALFABETOS SOLO PARA LLAMAR A LOS DEMAS QUE MUESTRAN MATRIZ
"""
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

    #return hPost

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- H(A|B) - EQUIVOCACION O RUIDO - ENTROPIA MEDIA A POSTERIORI ---------------------------------------------- #

"""
---- USA - ProbsBj, EntropiaAPosteriori

----- RECIBE - matriz del canal, probs a priori, alfabetos

    ALFABETOS SOLO PARA LLAMAR A LOS DEMAS QUE MUESTRAN MATRIZ
"""

# H(A|B)
def Equivocacion (matCanal,probsAi,alfEnt,alfSal):

    probsBj = ProbsBj(matCanal,probsAi,alfSal)
    hPost = EntropiaAPosteriori(matCanal,probsAi,alfEnt,alfSal)
    hAB = 0

    for j in range((len(probsBj))):
        hAB += probsBj[j] * hPost[j]

    print(f"H(A|B) - Equivocacion: {hAB:.4f}")

    #return hAB

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- H(B/ai) - ENTROPIA SALIDA CONDICIONADA ---------------------------------------------- #

"""
---- USA - Entropia

----- RECIBE - matriz del canal, probs a priori
"""

# H(B/ai)
def EntropiaSalidaCondicionada (matCanal,probsAi):
    hCond = []

    for i in range(len(probsAi)):
        fila = matCanal[i]
        h = Entropia(fila,2)
        hCond.append(h)
    
    return hCond

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- H(B|A) - PERDIDA ---------------------------------------------- #

"""
---- USA - EntropiaSalidaCondicionada

----- RECIBE - matriz del canal, probs a priori
"""

# H(B|A) = sumatoria de P(ai) * H(B/ai)
def Perdida (matCanal,probsAi):

    hBA = 0
    hCond = EntropiaSalidaCondicionada(matCanal,probsAi)

    for i in range(len(probsAi)):
        hBA += probsAi[i] * hCond[i]

    print(f" H(B|A) - Perdida: {hBA: .4f}")

    #return hBA

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- H(A,B) - ENTROPIA A FIN ---------------------------------------------- #

"""
---- USA - ProbabilidadSucesoSimultaneo

----- RECIBE - matriz del canal, probs a priori, alfabetos

    ALFABETOS SOLO PARA LLAMAR AL QUE MUESTRA MATRIZ
"""

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

# --------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------------- I(A,B) - INFORMACION MUTUA ---------------------------------------------- #

"""
---- USA - ProbabilidadSucesoSimultaneo, ProbabilidadesAPosteriori

----- RECIBE - matriz del canal, probs a priori, alfabetos

    ALFABETOS SOLO PARA LLAMAR A LOS DEMAS QUE MUESTRAN MATRIZ
"""

# Informacion Mutua I(A,B)
def InfoMutua (matCanal,probsAi,alfEnt,alfSal):

    matSS = ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal)
    matPost = ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal)
    Iab = 0

    for i in range(len(matSS)):
        for j in range(len(matSS[i])):
            Iab += matSS[i][j] * math.log(matPost[i][j] / probsAi[i],2)

    print(f"I(A,B) - Informacion Mutua: {Iab: .4f}")

    #return Iab

# ------------------------------------------------------------------------------------------------------------------ #