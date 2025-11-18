import math
def Entropia(prob,r):
    E=0 
    I=[math.log(1/X, r) for X in prob ]
    #print("el I",I)
    for a in range(len(prob)) :
        E+= (prob[a]*I[a])
    return E

def alfCod(cod):
    aux=set()    
    for x in cod:
        for y in x:
            if y not in aux:
                aux.add(y)
    #print("el alfabeto codigo es:",aux)
    return aux 

def longCod(cod):
    return [len(c) for c in cod ]

def longMedia(prob,cod):
    suma=0
    for x in range(len(cod)):
        suma+= prob[x] *cod[x]
    return suma

def rendimiento(prob,cod):
    
    H=Entropia(prob,len(alfCod(cod)))
    L=longMedia(prob,longCod(cod))
    if L!=0:
        nn=H/L
        R=1-nn
    else:
        nn=0
        R=1
    return nn,R

fuente=["A","B","C","D","E"]
prob=[0.2,0.15,0.1,0.3,0.25]
cod1=["01","111","110","101","100"]
cod2=["00","01","10","110","111"]
cod3=["0110","010","0111","1","00"]
cod4=["11","001","000","10","01"]
for i in range(1,5):
    exec(f"print('el rendimiento y la redundancia del codigo {i} es: ',rendimiento(prob,cod{i}))")