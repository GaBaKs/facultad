import random
import math

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

def generalistainfoN(listap,base):
    return [math.log(1/prob,base) for prob in listap]

def entropia(listap,base):
        entropia=0
        informacion=generalistainfoN(listap,base)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia

def esNoSingular (C):
    n = len(C)
    for i in range(n):
        for j in range(n):
            if (i != j):
                if (C[i] == C[j]):
                    return False                    
    return True

def esInstantaneo (C):
        n = len(C)
        for i in range(n):
            for j in range(n):
                if (i != j):
                    if C[i].startswith(C[j]):
                        return False
        return True

def esUnivoco (C):

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

def esCompacto (codigo, prob):
    if esInstantaneo(codigo) == False:
        return False
    else:     
        r=len(cadcod(codigo))
        aux = [math.ceil(abs(math.log(x,r))) for x in prob]
        if all(len(x)<= y for x,y in zip(codigo, aux)):
            return True
        else:
            return False
        
def sardinas(codigo):
    if esInstantaneo(codigo):
        print("Es instantaneo")
    else:
        print("No es instantaneo")
        if esUnivoco(codigo):
            print("Es univoco")
        else:
            print("No es univoco")
            if esNoSingular(codigo):
                print("es no singular")
            else:
                print("es codigo bloque")

def resuelve(codigo,prob):

    alfabeto=cadcod(codigo)

    print("la entropia es ",f"{entropia(prob,2): .4f}")
    L=longitudMedia(codigo,prob)
    print("longitud media: ",f"{L: .4f}")
    kraftvalor=kraft(codigo)
    print("valor de kraft: ",kraftvalor)
    if kraftvalor<=1:
        print("cumple con kraft-macmillan")
    else:
        print("no cumple con kraft-macmillan")
    sardinas(codigo)
    if esCompacto(codigo,prob):
        print("el codigo ingresado es compacto")
    else:
        print("el codigo ingresado no es compacto")

#pregunta 6
codigo=[ "])" , "(", ")[" ,"[" , "(]" ]
prob=[0.15, 0.25, 0.05, 0.45, 0.10]
resuelve(codigo,prob)
#pregunta 7
print("pregunta 7")
codigo=[ ",;" , ";", ":." ,"." , ",:" ]
prob=[0.15, 0.25, 0.05, 0.45, 0.10]
resuelve(codigo,prob)
