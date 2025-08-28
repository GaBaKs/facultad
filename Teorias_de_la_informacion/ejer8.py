import math


w= 0.5




def entropia(w):
        return (w*math.log2(1/w))

print("el valor de la entropia es de ",entropia(w)+entropia(1-w))