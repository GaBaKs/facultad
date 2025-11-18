[]

mat = [[0.6,0.3,0.1],
       [0.1,0.8,0.1],
       [0.3,0.3,0.4]]

probsAi = [4/15,3/15,8/15] # [1/3,1/3,1/3] [1/8,3/8,4/8] [4/15,3/15,8/15]

def ReglaDeDecisionMax (matCanal):

    d = []

    for j in range(len(matCanal[0])): # para cada columna
        maxProb = -1
         
        for i in range(len(matCanal)): # busco maximo elemento (mayor prob)
            if (mat[i][j] > maxProb):
                maxProb = mat[i][j]
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

ProbabilidadDeError(mat,probsAi)