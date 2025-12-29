import math
def Entropia(prob,r):
    E=0 
    I=[math.log(1/L , r) for L in prob ]
    print("el I",I)
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
    print("la longitud del alfabeto",lengAlf)
    entropiaN=Entropia(prob,lengAlf)*N
    L=longMedia(prob,longCod(codigo))*N
    print("la entropiaN",entropiaN)
    print("La long media",L)
    if ((entropiaN<=L) and (L<=entropiaN+1)):
        return True
    else:
        return False

#codigo=["00","01","10","11"]
#prob=[0.25,0.25,0.25,0.25]
#print("cumple el teorema de Shannon?",primer_Teo_Shannon(prob,codigo,3))

#EJ2
codigoB=["BA","CAB","A","CBA"]
probB=[0.3,0.1,0.40,0.2]
print("cumple el teorema de Shannon? ej2 ",primer_Teo_Shannon(probB,codigoB,2))