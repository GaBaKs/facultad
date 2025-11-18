import math

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

def genera_fuente(palabra): #Genera la fuente a partir de un mensaje (string)
    fuente = []
    for letra in palabra:
        if letra not in fuente:
            fuente += letra
    ListaP = [palabra.count(letra)/len(palabra) for letra in fuente] #Calcula la probabilidad de cada simbolo
    return fuente, ListaP

print("----- INCISO A -----")
palabra = 'ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB' #mensaje a codificar
fuente, ListaP = genera_fuente(palabra)
print("Fuente: ", fuente)
print("Probabilidades: ", ListaP)

print("Codificado de Huffman:    ", codigoHuffman(ListaP))
print("Codificado de Shannon-Fano:    ", codigoShannonFano(ListaP))

# Se hace una codificacion a partir de un mensaje
# A partir del mensaje obtengo la fuente, separando los smbolos distintos, con sus probabilidades al dividir las apariciones de cada simbolo por sobre el total de simbolos en el mensaje 
# Una vez con la fuente y su lista de probablidades puedo utilizar uno de los metodos de codificacion vistos

# Al codificar por Huffman se busca darle a las palabras de mayor probabilidad la codificacion mas corta, reduciendo asi el L de la fuente
# Esta codificacion se da listando las probabilidades de las palabras codigo de manera descendente y fusionando las ultimas (las menos probables) para ir formando la codificacion de la fuente,
# el resultado será una especie de arbol binario que representará a la fuente codificada, evitando ademas los prefijos (por lo tanto sera un codigo instantaneo)

# Al codificar por Shannon-Fano buscamos lo mismo que con la codificacion de Huffman, pero varia el metodo y tambien pueden variar los resultados levemente
# Esta codificacion se consigue de manera recursiva, se busca dividir las probabilidades en una rama izquierda y una derecha manteniendo una suma de probabilidades inferior a la mitad,
# si se sobrepasa ese umbral se decide si codificar con un 0 o un 1.
# Es importante aclarar que la codificacion dada por Huffman será la más optima al ser la de longitud media minima, cosa que no nos asegura el metodo de Shannon-Fano