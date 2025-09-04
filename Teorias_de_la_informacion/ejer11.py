import math


def generalista(listap):
    return [math.log2(1/prob) for prob in listap]

    


def entropia(listap):
        entropia=0
        listai=generalista(listap)
        for i in listap:
            entropia+=i*listai[listap.index(i)]

        return entropia



def calcula(alf, prob,n):
    if n==1:
        return alf,prob
    else:
        
        L,P= calcula(alf,prob,n-1)
        aux=[]
        auxp=[]

        for x in range(len(L)):
            for y in range(len(alf)):
                aux.append(L[x] + alf[y])
                auxp.append(P[x] * prob[y])

        return aux,auxp

lista=['x','y','z']
listap = [0.5 , 0.1 , 0.4]
n=2
generalista(listap)
print(n*entropia(listap))

L,P=calcula(lista,listap,n)
print(L)
print(P)
print(entropia(P))
    

