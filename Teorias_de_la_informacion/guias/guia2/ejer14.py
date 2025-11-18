import math



def vectorest(matriz,vecest,tolerancia):
    cumple=False
    
    while cumple==False:
           cumple=True
           vecaux=[0,0,0]
           for i in range(3):
            for j in range(3):
                vecaux[i]+=vecest[j]*matriz[i][j]
            if (abs(vecaux[i]-vecest[i])>=tol):
                cumple=False
           vecest=vecaux    
    return vecest
    
def generalista(listap):
    return [prob*math.log2(1/prob) for prob in listap]

    


def entropiamatriz(matriz,vecest):
        entropia=0  
        for fila in range(len(matriz)):                                   
         entropia+=sum(generalista(matriz[fila]))*vecest[fila]                                                                                        
        return entropia

matriz= [
    [0.58 , 0.43 , 0.3],
    [0.17 , 0.43 , 0.1],
    [0.25 , 0.14 , 0.6]
    ]
vecest= [0.3333,0.3333,0.3333]
tol=0.1



print("vecx original: ",vecest)
vecest=vectorest(matriz,vecest,tol)
print("vec cambiado:",vecest)
print("la entropia total es de ",entropiamatriz(matriz,vecest))