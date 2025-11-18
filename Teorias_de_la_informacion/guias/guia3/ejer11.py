import math
from libreria import *
listacodigos = ['==','<','<=','>','>=','<>']
probV =        [0.10,0.5,0.1,0.2,0.05,0.05]

ent=entropia(probV,2)


def longitudMedia(listacodigos,listaprob):
    L=0
    for i in range(len(listacodigos)):
        L+=len(listacodigos[i])*listaprob[i]
    return L

print("entropia: ",ent,"long media: ",longitudMedia(listacodigos,probV))