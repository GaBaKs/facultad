import math

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

def codigoShannonFano(probabilidades):
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
            if i < len(items):
                suma_izq = sum(p for p, _ in items[:i + 1])
                suma_der = sum(p for p, _ in items[i + 1:])
                if abs((suma_izq - items[i][0]) - (total/2)) < abs(suma_izq - (total/2)):
                    i -= 1 
            for p, idx in items[:i + 1]:
                codigo[idx] += '0'
            for p, idx in items[i + 1:]:
                codigo[idx] += '1'
            recShannonFano(items[:i + 1], codigo)
            recShannonFano(items[i + 1:], codigo)
    recShannonFano(items, codigo)
    return codigo

def codigoHuffman(probs):
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
    return codigos

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

ListaP = [0.385, 0.154, 0.128, 0.154, 0.179]

r = 2 #Tomo r = 2 ya que no se especifica en el enunciado
H = calcula_entropia(ListaP,r)
print("Entropía de la fuente: ", H)

#----- INCISOS DE HUFFMAN -----
codH = codigoHuffman(ListaP)
print("Código de Huffman: ", codH)

L = longitud_media(ListaP,codH)
print("Longitud media del código de Huffman: ", L)
print("Rendimiento del código de Huffman: ", calcula_rendimiento(ListaP,codH))
print("Redundancia del código de Huffman: ", calcula_redundancia(ListaP,codH))

#----- INCISOS DE SHANNON-FANO -----
codSF = codigoShannonFano(ListaP)
print("Código de Shannon-Fano: ", codSF)

L = longitud_media(ListaP,codSF)
print("Longitud media del código de Shannon-Fano: ", L)
print("Rendimiento del código de Shannon-Fano: ", calcula_rendimiento(ListaP,codSF))
print("Redundancia del código de Shannon-Fano: ", calcula_redundancia(ListaP,codSF))



# Se calcula el rendimiento del codigo, esto se hace dividiendo la entropia por la longitud media,
# tambien se calcula la redundancia dividiendo el resultado de la resta entre la longitud media y la entropia sobre la longitud media
# El rendimiento representa la eficiencia del codigo a la hora de transmitir informacion util
# La redundancia es la inversa de la eficiencia y representa que la informacion no util que fue transmitida por el canal, indica los datos omitidos