import math

#-------------------------------- EJERCICIO 5 ---------------------------------
#Para una fuente binaria con ω = 0.7:
#a. Obtener una codificación mediante el algoritmo de Huffman
#b. Codificar la extensión de orden 2 mediante el algoritmo de Shannon-Fano
#c. Comprobar si las codificaciones cumplen con el Primer Teorema de Shannon
#-------------------------------- EJERCICIO 5 ---------------------------------

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

def extensionN(alfabeto, dist_prob , n, nueva_alfabeto, nueva_dist_prob, i): #Calcula la extension de una fuente y sus probabilidades
    if i < 0:
        return nueva_alfabeto, nueva_dist_prob
    else:
        if i != n-1:
            k=0
            while k<len(alfabeto)**n:
                m=0
                while m<len(alfabeto):
                    j=0
                    while j<len(alfabeto)**i:
                        nueva_alfabeto[k]=nueva_alfabeto[k]+alfabeto[m]
                        nueva_dist_prob[k]=nueva_dist_prob[k]*dist_prob[m]
                        j+=1
                        k+=1
                    m+=1
            return extensionN(alfabeto, dist_prob, n, nueva_alfabeto, nueva_dist_prob, i-1)
        else:
            k=0
            m=0
            while m<len(alfabeto):
                j=0
                while j<len(alfabeto)**i:
                    nueva_alfabeto.append(alfabeto[m])
                    nueva_dist_prob.append(dist_prob[m])
                    j+=1
                m+=1
            return extensionN(alfabeto, dist_prob, n, nueva_alfabeto, nueva_dist_prob, i-1)

def calcula_entropia(prob,r): #Calcula la entropia de una fuente
    entropia = 0
    for p in prob:
        entropia = entropia + p * (math.log(1/p, r))
    return entropia 

def longitud_media(prob, alfabeto): #Calcula la longitud media de un codigo
    Ln = 0
    for p, x in zip(prob, alfabeto):
        Ln = Ln + p * len(x)
    return Ln

def Teorema_Shannon(fuente, ListaP, r): #Verfica si se cumple el teorema de Shannon
    entropia = calcula_entropia(ListaP,r)
    Ln = longitud_media(ListaP,fuente)
    print(entropia," <= ",Ln," < ",entropia+1)
    if(entropia <= Ln < entropia+1): #Teorema de Shannon
        return print("El teorema de Shannon se cumple")
    else:
        return print("El teorema de Shannon no se cumple")


w = 0.7
r = 2
fuente = ['0','1']
ListaP = [w, 1-w]

print("Huffman:    ", Huffman(ListaP))
Teorema_Shannon(fuente, ListaP, r)

Ext, ExtP = extensionN(fuente, ListaP, 2, [], [], 1) #Las listas vacias seran Ext y Extp, N-1 es una variable de control, el 2 es la dimension de la extension (N)
print("Shannon-Fanno:    ", ShannonFano(ExtP))
Teorema_Shannon(ShannonFano(ExtP), ExtP, r) #Analiza si se cumple el teorema de Shannon para el codigo propuesto utilizando Shannon-Fanon