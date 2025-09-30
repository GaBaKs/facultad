import math

matriz= [
    [0.58 , 0.43 , 0.3],
    [0.17 , 0.43 , 0.1],
    [0.25 , 0.14 , 0.6]
    ]
vecx= [0.3333,0.3333,0.3333]
tol=0.000001

def vectorest(matriz,vecx,tol):
    cumple=False
    
    while cumple==False:
           cumple=True
           vecaux=[0,0,0]
           for i in range(3):
            for j in range(3):
                vecaux[i]+=vecx[j]*matriz[i][j]
            if (abs(vecaux[i]-vecx[i])>=tol):
                cumple=False
           vecx=vecaux
           print("vecaux es",vecaux)         
    return vecx
    
def generalista(listap):
    return [prob*math.log2(1/prob) for prob in listap]

def entropia(matriz,vecx):
        entropia=0  
        for fila in range(len(matriz)):                                   
         entropia+=sum(generalista(matriz[fila]))*vecx[fila]                                                                                        
        return entropia

print("vecx original: ",vecx)
vecx=vectorest(matriz,vecx,tol)
print("vec cambiado:",vecx)
print("la entropia total es de ",entropia(matriz,vecx))