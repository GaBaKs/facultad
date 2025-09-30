import math

def extencion (fuente, prob, N):
    if N==1:
        ext = fuente
        extP = prob
    else:
        ext, extP = extencion(fuente, prob, N-1)
        ext = ext * len(fuente)
        aux = []
        for letra in fuente:
            aux += len(fuente)**(N-1) * letra
        ext = [x + y for x, y in zip(aux, ext)]
        extP = [x * y for x in prob for y in extP]  
    return ext, extP
                
fuente = ['A','B','C','D'] 
prob = [0.25,0.25,0.25,0.25]
N = 3 #CANTIDAD DE SIMBOLOS
ext, extP = extencion(fuente, prob, N)

print("extension",ext)
print("probabilidades de la extension",extP)
