import math


def calculaordenN(alf, prob,n):
    if n==1:
        return alf,prob
    else:
        
        L,P= calculaordenN(alf,prob,n-1)
        aux=[]
        auxp=[]

        for x in range(len(L)):
            for y in range(len(alf)):
                aux.append(L[x] + alf[y])
                auxp.append(P[x] * prob[y])

        return aux,auxp

alf=['a','b','c','d']
prob=[0.6, 0.2, 0.2, 0.2]
n=2
L,P=calcula(alf,prob,n)
print(L)
print(P)

    