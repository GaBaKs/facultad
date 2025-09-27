import math



def generalistainfoN(listap,base):
    return [math.log(1/prob,base) for prob in listap]

def entropia(listap,base):
        entropia=0
        informacion=generalistainfoN(listap,base)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia

def entropiabin(w):
        return (w*math.log2(1/w)+(1-w)*math.log2(1/(1-w)))

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
           vecaux=[0,0,0]
           for i in range(3):
            for j in range(3):
                vecaux[i]+=vecest[j]*matriz[i][j]
            if (abs(vecaux[i]-vecest[i])>=tolerancia):
                cumple=False
           vecest=vecaux    
    return vecest


def esNoSingular (C):
    n = len(C)
    for i in range(n):
        for j in range(n):
            if (i != j):
                if (C[i] == C[j]):
                    return False                    
    return True

def esInstantaneo (C):
    if esNoSingular(C) == False:
        return False
    else:
        n = len(C)
        for i in range(n):
            for j in range(n):
                if (i != j):
                    if C[i].startswith(C[j]):
                        return False
        return True

def esUnivoco (C):
    if esInstantaneo(C) == True:
        return True
    else: 
        S = C
        ST = []
        while True:
            aux = []
            for x in S:
                for y in C:
                    if x != y: 
                        if x.startswith(y):
                            diferencia = x[len(y):]
                            if diferencia not in aux:
                                aux.append(diferencia)
                        else:
                            if y.startswith(x):
                                diferencia = y[len(x):]
                                if diferencia not in aux:
                                  aux.append(diferencia)
            ST.append(S)
            S = aux
            if all(x not in C for x in S) and (S not in ST):
                continue
            else:
                break
        if (S in ST):
            return True
        else: 
            return False

#devuelve r
def cadcod(listacodigos):
    cadena=''
    for cod in listacodigos:
        for x in cod:
            if not x in cadena:
                cadena+=x
    return cadena

def longitud(listacodigos):    # (devuelve long de cada codigo)
    listaux=([len(long) for long in listacodigos]) 
    return listaux

def kraft(listacodigos):
   r=len(cadcod(listacodigos))
   long=longitud(listacodigos)
   suma=0
   for x in long:
        suma+=r**-x
   return suma

def longitudMedia(listacodigos,listaprob):
    L=0
    for i in range(len(listacodigos)):
        L+=len(listacodigos[i])*listaprob[i]
    return L

