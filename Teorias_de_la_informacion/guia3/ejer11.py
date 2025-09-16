import math
listap = ['==','<','<=','>','>=','<>']

probV = [0.10,0.5,0.1,0.2,0.05,0.05]

def cadcod(listap):
    cadena=''
    for cod in listap:
        for x in cod:
            if not x in cadena:
                cadena+=x
    return cadena

r=len(cadcod(listap))

def generalista(listap,r):
    return [prob*math.log(1/prob,r) for prob in listap]


def entropia(listap):
        entropia=0
        listai=generalista(probV)
        for i in listai:
            entropia+=i*listai[listap.index(i)]
        
        
        return print("la entropia es de ",entropia)

entropia(listap)