import math
from libreria import *

mensaje="BBAAACCAAABCCCAACCCBBACCAABBAA"
tol=0.1

simbolos,cant=cuentasimbolos(mensaje)

prob=probabilidadlista(simbolos,cant)

matT=MatrizDeTransicion(simbolos,mensaje)

tipofuente(matT,tol)

vecest=[0.33, 0.33, 0.33]



def entropiamatT(matT,vecest):
        entropi=0  
        for fila in range(len(vecest)):  
         suma=entropia(matT[fila],2)                             
         entropi+=suma*vecest[fila]                                                                                        
        return entropi

print("valor de la entropia: ",entropiamatT(matT,vecest))

