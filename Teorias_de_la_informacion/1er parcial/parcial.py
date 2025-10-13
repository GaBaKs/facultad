import math
import random

palabra="+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"

def cuentasimbolos(palabra):
   simbolos=[]
   cant=[]
   for i in palabra:
          if i in simbolos:
               cant[simbolos.index(i)]+=1
          else:
              simbolos.append(i)
              cant.append(1)
   return simbolos,cant

def probabilidadlista(simbolos,cant):
     listaprob=[]
     total=sum(cant)
     
     for i in simbolos:
        listaprob.append(cant[simbolos.index(i)]/total)
     return listaprob

def MatrizDeTransicion (simbolos,palabra):
    matT = [ [0 for _ in range(len(simbolos))] for _ in range(len(simbolos))]
    palabraL = list(palabra) #transformo a lista
    for i in range(len(simbolos)):
        for j in range(len(simbolos)):
            canti = 0
            for k in range(len(palabraL) - 1): 
                if palabraL[k] == simbolos[i] and palabraL[k+1] == simbolos[j]:
                    canti += 1      #cuento apariciones de la cadena de 2
            matT[i][j] = canti # guardo en la matriz la cant de repeticiones

    for j in range(len(matT)):
        tot = 0
        for i in range(len(matT)):
            tot += matT[i][j] #sumo cantidades de esa letra por columna
        
        for i in range(len(matT)):
            matT[i][j] = matT[i][j] / tot
    
    return matT

def generalistainfoN(listap,base):
    return [math.log(1/prob,base) for prob in listap]

def entropia(listap,base):
        entropia=0
        informacion=generalistainfoN(listap,base)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia

def calculaordenN(alfabeto, prob,n):
    if n==1:
        return alfabeto,prob
    else:
        
        L,P= calculaordenN(alfabeto,prob,n-1)
        aux=[]
        auxp=[]

        for x in range(len(L)):
            for y in range(len(alfabeto)):
                aux.append(L[x] + alfabeto[y])
                auxp.append(P[x] * prob[y])

        return aux,auxp

def vectorest(matriz,vecest,tolerancia):
    cumple=False
    
    while cumple==False:
           cumple=True
           vecaux=[0,0,0,0]
           for i in range(4):
            for j in range(4):
                vecaux[i]+=vecest[j]*matriz[i][j]
            if (abs(vecaux[i]-vecest[i])>=tolerancia):
                cumple=False
           vecest=vecaux    
    return vecest

def tipofuente (matT, tol):
    r = 1
    i = 0
    while (i in range(len(matT))) and r: 
        fila = matT[i] # le doy la fila entera
        j = 0
        while j in range(len(fila) - 1) and r: # recorro fila
            k = j + 1
            while k in range(len(fila)) and r:
                if fila[j] - fila[k] > tol:
                    r = 0
                k += 1
            j += 1
        i += 1
    if r:
        print("Fuente de memoria nula")
    else:
        print("Fuente de memoria no nula")


#mensaje 1
simbolos,cant=cuentasimbolos(palabra)
prob=probabilidadlista(simbolos,cant)
matT=MatrizDeTransicion(simbolos,palabra)
for fila in matT:
    print([f"{val: .4f}" for val in fila])

tipofuente (matT, 0.1)
print("El alfabeto es ",simbolos,"y la probabilidad de palabra simbolo es de ",prob)
print("la entropia de la fuente es de",f"{entropia(prob,2): .4f}")
aux,auxp=calculaordenN(simbolos,prob,2)
entropiaO2=entropia(auxp,2)
print("la entropia de la extension 2 es ",f"{entropiaO2: .4f}")
print(" la probabilidad de *+ es de ",f"{auxp[aux.index("*+")]: .4f}")
print(" la probabilidad de -/ es de ",f"{auxp[aux.index("-/")]: .4f}")


#mensaje 2
print("mensaje 2")
mensaje=".;.:.:.::;:,::.;:,::,;,:;.:.;.;;:,.::.:,.:.;:::::."

simbolosb,cantb=cuentasimbolos(mensaje)
prob2=probabilidadlista(simbolosb,cantb)
matTb=MatrizDeTransicion(simbolosb,mensaje)
for fila in matTb:
    print([f"{val: .4f}" for val in fila])
tipofuente (matTb, 0.1)

print("El alfabeto es ",simbolosb,"y la probabilidad de palabraa simbolo es de ",prob2)
print("la entropia de la fuente es de",f"{entropia(prob2,2): .4f}")

vecest=[0.25, 0.25, 0.25, 0.25]

vecest=vectorest(matTb,vecest,0.1)
print(vecest)