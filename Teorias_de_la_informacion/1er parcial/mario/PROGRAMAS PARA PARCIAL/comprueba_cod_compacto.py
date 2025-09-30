import math

def creaStringCodigo (C):        #lo traemos del ejercicio anterior porque necesitamos la cantidad de simbolos de x (r)
    cadena = ""
    for c in C:
        for x in c:
            if not x in cadena:
                cadena += x
    return cadena

def calculaLongitudMedia (codigo, prob):
    L = 0
    for i in range(len(codigo)):
        L += prob[i] * len(codigo[i])
    return L

def esCompacto (codigo, prob):
    Lmedia = calculaLongitudMedia(codigo,prob)
    Lbase = 0
    r = len(creaStringCodigo(codigo))
    for x in prob:
        Lbase += math.ceil(math.log((1/x), r))

    if Lmedia <= Lbase:
        return True
    else:
        return False

def esCompacto (codigo, prob): #comprueba para cantidades de informacion no exactas(no fracciones)
    r=len(creaStringCodigo(codigo))
    aux = [math.ceil(abs(math.log(x,r))) for x in prob]
    if all(len(x)<= y for x,y in zip(codigo, aux)):
        return True
    else:
        return False

codigo = [")", "[]", "]]", "([","[()]", "([)]"]
prob = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]

print(esCompacto(codigo,prob))