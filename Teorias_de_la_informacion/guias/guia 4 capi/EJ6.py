"""Realizar una función en Python que reciba como parámetros: dos listas paralelas con la
distribución de probabilidades de una fuente y su codificación, y calcule el rendimiento y la
redundancia del código 
el rendimiento nn es H/L y la renduncancia R es 1- el rendimiento"""
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
prob=[0.5,0.2,0.3]
cod1=["11", "010", "00" ]
prob2=[0.25, 0.1, 0.15, 0.1, 0.04000000000000001, 0.06, 0.15, 0.06, 0.09]
cod2=["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111" ]
print("el rendimiento y la redundancia del codigo 1 es: ",rendimiento(prob,cod1))
print("el rendimiento y la redundancia del codigo 2 es: ",rendimiento(prob2,cod2))   