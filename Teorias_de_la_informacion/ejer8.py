import math


w= 0.5


def entropiabin(w):
        return (w*math.log2(1/w)+(1-w)*math.log2(1/(1-w)))

print(entropiabin(w))