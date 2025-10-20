import math


listap = [0.5 , 0.25 , 0.25]

def generalistainfo(listap):
    return [math.log(1/prob) for prob in listap]

    


generalistainfo(listap)

def entropia(listap):
        entropia=0
        informacion=generalistainfo(listap)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia

entropia(listap)