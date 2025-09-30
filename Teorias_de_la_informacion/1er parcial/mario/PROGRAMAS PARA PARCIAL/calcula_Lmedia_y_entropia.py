import math

def creaStringCodigo (C):        #lo traemos del ejercicio anterior porque necesitamos la cantidad de simbolos de x (r)
    cadena = ""
    for c in C:
        for x in c:
            if not x in cadena:
                cadena += x
    return cadena

def calculaEntropia (prob, r): #calcula entropia en base r
    Hn = 0
    for p in prob:
        Hn += p * math.log(1/p, r)
    return Hn

def calculaLongitudMedia (codigo, prob):
    L = 0
    for i in range(len(codigo)):
        L += prob[i] * len(codigo[i])
    return L

codigo = ["/","*","-","*","++","+-"]
prob = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]

r = len(creaStringCodigo(codigo))
entropia = calculaEntropia(prob,r)
Lmedia = calculaLongitudMedia(codigo,prob)

print("entropia: ",entropia)
print("longitud media :",Lmedia)