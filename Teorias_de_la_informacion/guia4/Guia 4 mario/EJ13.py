import math

#-------------------------------- EJERCICIO 13 ---------------------------------
# Dada una fuente de información que emite el siguiente mensaje representativo:
# 58784784525368669895745123656253698989656452121702300223659
# a. Calcular la entropía de la fuente
# b. Construir una codificación de Huffman
# c. Generar una codificación de Shannon-Fano
# d. Comparar la longitud media, el rendimiento y la redundancia de cada código
#-------------------------------- EJERCICIO 13 ---------------------------------

def genera_fuente(palabra):
    fuente = []
    for letra in palabra:
        if letra not in fuente:
            fuente += letra
    ListaP = [palabra.count(letra)/len(palabra) for letra in fuente] #Calcula la probabilidad de cada simbolo
    return fuente, ListaP

def calcula_entropia(prob,r): #Calcula la entropia de una fuente
    entropia = 0
    for p in prob:
        entropia = entropia + p * (math.log(1/p, r))
    return entropia 

def ShannonFano(probabilidades):
    items = [[p, i] for i, p in enumerate(probabilidades)]
    codigo = ['' for _ in range(len(probabilidades))]
    items.sort(reverse=True)
    def recShannonFano(items, codigo):
        if len(items) > 1:
            total = sum(p for p, _ in items)
            acc = 0
            i=0
            while i < len(items) and acc + items[i][0] < total / 2:
                acc += items[i][0]
                i += 1
            # Ahora 'i' es el índice del elemento que podría causar el "desborde"
            # Vamos a decidir si dejarlo en la izquierda o pasarlo a la derecha
            if i < len(items):
                suma_izq = sum(p for p, _ in items[:i + 1])
                suma_der = sum(p for p, _ in items[i + 1:])
                # Si la izquierda supera mucho la mitad, movemos ese elemento al otro lado
                if abs((suma_izq - items[i][0]) - (total/2)) < abs(suma_izq - (total/2)):
                    i -= 1  # mover el elemento al grupo derecho
            for p, idx in items[:i + 1]:
                codigo[idx] += '0'
            for p, idx in items[i + 1:]:
                codigo[idx] += '1'
            recShannonFano(items[:i + 1], codigo)
            recShannonFano(items[i + 1:], codigo)
    recShannonFano(items, codigo)
    return codigo

def Huffman(probs):
    items = [[p, [i]] for i, p in enumerate(probs)]
    codigos = ["" for _ in range(len(probs))]
    while len(items) > 1:
        items.sort(key=lambda x: x[0])
        izq = items.pop(0)              
        der = items.pop(0)
        for i in izq[1]:
            codigos[i] = '0' + codigos[i]
        for i in der[1]:
            codigos[i] = '1' + codigos[i]
        nuevo = [izq[0] + der[0], izq[1] + der[1]]
        items.append(nuevo)
    return  codigos 

def longitud_media(prob, alfabeto): #Calcula la longitud media de un codigo
    Ln = 0
    for p, x in zip(prob, alfabeto):
        Ln = Ln + p * len(x)
    return Ln

def calcula_rendimiento(ListaP, cod): #Calcula el rendimiento de un codigo
    Ln = longitud_media(ListaP,cod)
    H = calcula_entropia(ListaP,r)
    return H/Ln

def calcula_redundancia(ListaP, cod): #Calcula la redundancia de un codigo
    Ln = longitud_media(ListaP,cod)
    H = calcula_entropia(ListaP,r)
    return (Ln - H)/Ln

palabra = '58784784525368669895745123656253698989656452121702300223659'
fuente, ListaP = genera_fuente(palabra)

print("Fuente: ", fuente)
print("Probabilidades: ", ListaP)
r = 2 #Tomo r = cantidad de simbolos en la fuente
H = calcula_entropia(ListaP,r)
print("Entropía de la fuente: ", H)

#----- INCISOS DE HUFFMAN -----
codH = Huffman(ListaP)
print("Código de Huffman: ", codH)

L = longitud_media(ListaP,codH)
print("Longitud media del código de Huffman: ", L)
print("Rendimiento del código de Huffman: ", calcula_rendimiento(ListaP,codH))
print("Redundancia del código de Huffman: ", calcula_redundancia(ListaP,codH))

#----- INCISOS DE SHANNON-FANO -----
codSF = ShannonFano(ListaP)
print("Código de Shannon-Fano: ", codSF)

L = longitud_media(ListaP,codSF)
print("Longitud media del código de Shannon-Fano: ", L)
print("Rendimiento del código de Shannon-Fano: ", calcula_rendimiento(ListaP,codSF))
print("Redundancia del código de Shannon-Fano: ", calcula_redundancia(ListaP,codSF))


