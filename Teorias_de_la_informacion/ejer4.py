import math


alfabeto= [ "x" , "y" , "z"]
prob=[ 0.5, 0.1, 0.4 ]

def calcula(alfabeto,prob):
    calc=0
    for letra in alfabeto:
        calc+=prob[alfabeto.index(letra)]*math.log2(1/prob[alfabeto.index(letra)])
    return print("la entropia es de ",calc )


calcula(alfabeto,prob)



