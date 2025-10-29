import math
import random


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

def MatrizDeTransicion (simbolos,cad):
    matT = [ [0 for _ in range(len(simbolos))] for _ in range(len(simbolos))]
    cadL = list(cad) #a la cadena la hago lista
    for i in range(len(simbolos)):
        for j in range(len(simbolos)):
            canti = 0
            for k in range(len(cadL) - 1): #cuento apariciones de la dupla
                if cadL[k] == simbolos[i] and cadL[k+1] == simbolos[j]:
                    canti += 1
            matT[i][j] = canti # pongo cant de la dupla en la ubicacion de la matriz

    for j in range(len(matT)):
        tot = 0
        for i in range(len(matT)):
            tot += matT[i][j] #sumo cantidades de esa letra por columna
        
        for i in range(len(matT)):
            matT[i][j] = matT[i][j] / tot
    
    return matT

def getcolumna(matriz,alfabeto,caracter):
    aux=[]
    for i in matriz:
        aux.append(i[alfabeto.index(caracter)])
    
    return aux

def simularMensaje(simbolos,matriz,longitud,simbolo_inicial):
    mensaje = []
    if simbolo_inicial == '':
        simbolo_inicial = random.choice(simbolos)[0]
    mensaje.append(simbolo_inicial)

    for x in range(longitud - 1):
        simbolo_actual = mensaje[-1]
        columna=getcolumna(matriz,simbolos,simbolo_actual)
        siguiente_simbolo=random.choices(simbolos,weights=columna,k=1)[0]
        mensaje.append(siguiente_simbolo)

    return mensaje


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

def entropiamatT(matT,vecest):
        entropi=0  
        for fila in range(len(vecest)):  
         suma=entropia(matT[fila],2)                             
         entropi+=suma*vecest[fila]                                                                                        
        return entropi

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

def creastringcodigo (C):        #lo traemos del ejercicio anterior porque necesitamos la cantidad de simbolos de x (r)
    cadena = ""
    for c in C:
        for x in c:
            if not x in cadena:
                cadena += x
    return cadena


def esCompacto (codigo, prob):
    if esInstantaneo(codigo) == False:
        return False
    else:     
        r=len(creastringcodigo(codigo))
        aux = [math.ceil(abs(math.log(x,r))) for x in prob]
        if all(len(x)<= y for x,y in zip(codigo, aux)):
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
    for p,i in zip(listaprob,listacodigos):
        L+=len(i)*p
    return L

def primershannon(codigos,prob,orden): 
    r=len(cadcod(codigos))
    ent=entropia(prob,r)
    L=longitudMedia(codigos,prob)
    print(ent," <= ",L," <= ",ent+1)

    if (ent)<=L and L<(ent+1):
        return True
    else:
        return False

def Huffman(probs):
    items = [[p, [i]] for i, p in enumerate(probs)]
    codigos = ["" for _ in range(len(probs))]
    while len(items) > 1:
        items.sort(key=lambda x: x[0])
        izq = items.pop(0)              
        der = items.pop(0)
        for i in izq[1]:
            codigos[i] = '0' + codigos[i]
        for i in der[1]:
            codigos[i] = '1' + codigos[i]
        nuevo = [izq[0] + der[0], izq[1] + der[1]]
        items.append(nuevo)
    return  codigos 

def ShannonFano(probabilidades):
    items = [[p, i] for i, p in enumerate(probabilidades)]
    codigo = ['' for _ in range(len(probabilidades))]
    items.sort(reverse=True)
    def recShannonFano(items, codigo):
        if len(items) > 1:
            total = sum(p for p, _ in items)
            acc = 0
            i=0
            while i < len(items) and acc + items[i][0] < total / 2:
                acc += items[i][0]
                i += 1
            # Ahora 'i' es el índice del elemento que podría causar el "desborde"
            # Vamos a decidir si dejarlo en la izquierda o pasarlo a la derecha
            if i < len(items):
                suma_izq = sum(p for p, _ in items[:i + 1])
                suma_der = sum(p for p, _ in items[i + 1:])
                # Si la izquierda supera mucho la mitad, movemos ese elemento al otro lado
                if abs((suma_izq - items[i][0]) - (total/2)) < abs(suma_izq - (total/2)):
                    i -= 1  # mover el elemento al grupo derecho
            for p, idx in items[:i + 1]:
                codigo[idx] += '0'
            for p, idx in items[i + 1:]:
                codigo[idx] += '1'
            recShannonFano(items[:i + 1], codigo)
            recShannonFano(items[i + 1:], codigo)
    recShannonFano(items, codigo)
    return codigo

def rendimiento(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return ent/L

def redundancia(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return (L-ent)/L

def calculamensaje(palabra):
    simbolos,cant=cuentasimbolos(palabra)
    prob=probabilidadlista(simbolos,cant)
    return simbolos,prob

