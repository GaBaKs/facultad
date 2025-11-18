import math
def Entropia(prob,r):
    E=0 
    I=[math.log(1/L , r) for L in prob ]
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

def primer_Teo_Shannon(prob, codigo, N):
    lengAlf=len(alfCod(codigo))
    entropiaN=Entropia(prob,lengAlf)*N
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
prob=[0.5,0.2,0.3]

C1= [ "11", "010", "00" ]
C2= [ "10", "001", "110", "010", "0000", "0001", "111", "0110", "0111" ]
ext,probN=extension(C1,prob,2)
print("la prob de la extension es: ",probN)
print("cumple el teorema de Shannon? ej2 C1",primer_Teo_Shannon(prob,C1,1))
print("cumple el teorema de Shannon? ej2 C2",primer_Teo_Shannon(probN,C2,1))