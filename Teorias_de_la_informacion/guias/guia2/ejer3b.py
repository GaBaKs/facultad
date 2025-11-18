import math


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