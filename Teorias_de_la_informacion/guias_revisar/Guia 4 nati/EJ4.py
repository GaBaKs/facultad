import math
def Entropia(w):
    H=-w*math.log2(w)-(1-w)*math.log2(1-w)
    print("La entropia de la fuente es:",H)
    return H
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

def primer_Teo_Shannon(prob, codigo, N):
    lengAlf=len(alfCod(codigo))
    entropiaN=Entropia(0.8)*N
    L=longMedia(prob,longCod(codigo))*N
    print("la entropiaN",entropiaN)
    print("La long media",L)
    if ((entropiaN<=L) and (L<=entropiaN+1)):
        return 1
    else:
        return 0
def extension(alf,prob,n):
    if n==1:
        return alf, prob
    else:
        E=[] 
        P=[] 
        aux=[]
        auxP=[]
        E, P=extension(alf,prob,n-1)
        for x in range(len(E)):
            for y in range(len(alf)) :
                aux.append(E[x]+alf[y])
                auxP.append(P[x]*prob[y])
    return aux, auxP
alf=["0","1"]
prob=[0.8,0.2]
n=3
cotainf=Entropia(0.8)*3
cotasup=cotainf+1/3 
alfN,probN=extension(alf,prob,3)
#print("la exttension de orden 3 es:",alfN)
#print("la prob de extension de orden 3 es:",probN)
codigo=["0","1"]
print("la conta inf",cotainf)
print("la cota sup",cotasup)
print("primer teorema de Shannon",primer_Teo_Shannon(prob,codigo,3))
haceer eo c 2 pero vos