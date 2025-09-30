import math

def generaInfo (ListaP):
    return [math.log2(1/prob) for prob in ListaP] #ARMA LA LISTA CON LA INFORMACION DE CADA SIMBOLO

ListaS = ['A','B','C','D','E','F'] #EJEMPLO DE SIMBOLOS DEL CODIGO
ListaP = [1/9, 1/6, 1/9, 1/9, 1/6, 1/3] #LISTA DE PROBABILIDADES

ListaI = generaInfo(ListaP)
print("INFORMACION:",ListaI)