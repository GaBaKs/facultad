import math

def generaInfo (ListaP):
    return [math.log2(1/prob) for prob in ListaP] #ARMA LA LISTA CON LA INFORMACION DE CADA SIMBOLO

def generaEntropia (ListaP):
    entropia = 0
    ListaI = generaInfo(ListaP)
    for prob in ListaP:
        entropia += prob * ListaI[ListaP.index(prob)] #CALCULA LA ENTROPIA DE LA FUENTE
    return entropia


ListaP = [1/9, 1/6, 1/9, 1/9, 1/6, 1/3] #LISTA DE PROBABILIDADES

entropia = generaEntropia(ListaP)  
print("ENTROPIA:",entropia) #ENTROPIA DE LA FUENTE