import math

def generaInfo (ListaP):
    return [math.log2(1/prob) for prob in ListaP]

def generaEntropia (ListaP):
    entropia = 0
    ListaI = generaInfo(ListaP)
    for prob in ListaP:
        entropia += prob * ListaI[ListaP.index(prob)] 
    return entropia


ListaP = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

ListaI = generaInfo(ListaP)
print("La informacion de la fuente es: ",ListaI)
entropia = generaEntropia(ListaP)  
print("La entropia de la fuente es: ",entropia)

def extencion (fuente, ListaP, N):
    if N==1:
        ext = fuente
        extP = ListaP
    else:
        ext, extP = extencion(fuente, ListaP, N-1)
        ext = ext * len(fuente)
        aux = []
        for letra in fuente:
            aux += len(fuente)**(N-1) * letra
        ext = [x + y for x, y in zip(aux, ext)]
        extP = [x * y for x in ListaP for y in extP]  
    return ext, extP
                
fuente = ['1','2','3','4','5','6']
N = 3
ext, extP = extencion(fuente, ListaP, N)
extE = 0
for prob in extP:
    extE+= prob * math.log2(1/prob)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

print("La extencion de la fuente es: ",ext)
print("La probabilidad de la extencion de la fuente es: ",extP)
print("La entropia de la extencion es: ",extE)
print("La entropia de la fuente por N es: ",entropia*N)