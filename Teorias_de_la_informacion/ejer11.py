import math

lista=['1','2','3','4','5','6']
listap = [1/9 , 1/6, 1/9, 1/9, 1/6, 1/3]

def generalista(listap):
    return [math.log2(1/prob) for prob in listap]

    
generalista(listap)

def entropia(listap):
        entropia=0
        listai=generalista(listap)
        for i in listap:
            entropia+=i*listai[listap.index(i)]
        
        
        return print("la entropia es de ",entropia)

entropia(listap)

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

alf=['a','b','c','d']
prob=[0.6, 0.2, 0.2, 0.2]
n=4
L,P=calcula(alf,prob,n)
print(L)
print(P)

    