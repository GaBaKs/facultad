[]

import math

codigo = ["BC","A","C","BA","BB"]
probs = [0.13,0.34,0.37,0.12,0.04]

"""
Verificar si es compacto

1. Calculo entropia
2. Calculo longitud media
3. Compruebo que la longitud de cada palabra sea menor
    o igual a logr Pi-1
"""

def AlfabetoCodigo (codigo):
    alf = set()

    for palabra in codigo:
        for car in palabra:
            if car not in alf:
                alf.add(car)
    
    return alf

def Entropia (codigo,probs,r):
    H = 0

    for i in range(len(codigo)):
        H += probs[i] * math.log(1/probs[i], r)

    return H

def LongitudesPalabras (codigo):
    return [len(palabra) for palabra in codigo]

def LongitudMedia (codigo,probs,long):
    L = 0

    for i in range(len(codigo)):
        L += probs[i] * long[i]

    return L

def EsCompacto (codigo,probs,long,r):
    rta = 1
    if(Entropia(codigo,probs,r) <= LongitudMedia(codigo,probs,long)):
        i = 0
        while (i in range(len(long))) and rta:
            if long[i] > math.ceil(math.log(1/probs[i],r)):
                rta = 0
            i += 1
    
    return rta



long = LongitudesPalabras(codigo)
r =  len(AlfabetoCodigo(codigo))

if EsCompacto(codigo,probs,long,r):
    print("Es compacto")
else:
    print("No es compacto")