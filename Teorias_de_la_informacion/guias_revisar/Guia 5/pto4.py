[]

entrada = "010101"
salida = "010101"
#matCanal = [[0.4, 0.4, 0.2],
 #           [0.3, 0.2, 0.5],
  #          [0.3, 0.4, 0.3]]

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

# Obtiene y muestra la matriz del canal a partir de las cadenas de entrada y salida
# P(bj/ai)
def MatrizDelCanal(entrada,salida,alfEnt,alfSal):

    matCanal = [ [0] * len(alfSal) for _ in range(len(alfEnt)) ] # inicializo matriz

    # veo el simbolo de entrada y su correspondiente simbolo de salida
    for simbEnt, simbSal in zip(entrada,salida): # zip junta los elem de ambas cadenas por posicion
        matCanal[alfEnt.index(simbEnt)][alfSal.index(simbSal)] += 1 # en mat(i,j) sumo cant veces que entro ai y salio bj

    for i in range(len(matCanal)):
        cantAi= sum(matCanal[i]) # cuento cant apariciones del simbolo de entrada (ai)
        if cantAi != 0:
            matCanal[i] = [elem / cantAi for elem in matCanal[i]] # divido toda la fila por la cantidad de apariciones, para obtener prob condicional

    # Muestra matriz segun par (i,j)
    print("P(bj/ai) - Matriz del canal:")
    for i in range(len(matCanal)): # i es el índice de la fila
        for j in range(len(matCanal[i])): # j es el índice de la columna
            print(f"  ({alfEnt[i]}, {alfSal[j]}) = {matCanal[i][j]: .4f}", end=" ")
        print() # salto de línea para pasar a la siguiente fila

    return matCanal

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

    #return matPost

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

# TENGO QUE TENER ESTO SI O SI PARA PODER MOSTRAR BIEN LAS MATRICES

probsAi,alfEnt = AlfabetoProbabilidades(entrada) #probsAi son P(ai), probs a priori
probsaux,alfSal = AlfabetoProbabilidades(salida) # obtengo alfabeto de la salida

# Muestro
print("P(ai) - Probabilidades A Priori:")
MuestraSimbolos(alfEnt,probsAi)

# SACAR ESTA LINEA SI YA ME DAN LA MATRIZ
matCanal = MatrizDelCanal(entrada,salida,alfEnt,alfSal) # ALFABETOS NECESARIOS

# Llamo probs, P(bj) se llama en Posteriori
ProbabilidadesAPosteriori(matCanal,probsAi,alfEnt,alfSal) # los alfabetos son solo para mostrar bien la matriz
ProbabilidadSucesoSimultaneo(matCanal,probsAi,alfEnt,alfSal) # los alfabetos son solo para mostrar bien la matriz