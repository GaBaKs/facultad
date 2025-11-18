import math

#-------------------------------- EJERCICIO 11 ---------------------------------
#  Desarrollar dos funciones en Python que reciban como parámetro una lista con la
# distribución de probabilidades de una fuente de información y generen una lista de
# cadenas de caracteres con codificaciones binarias de Huffman y de Shannon-Fano.
#-------------------------------- EJERCICIO 11 ---------------------------------

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

def genera_fuente(palabra):
    fuente = []
    for letra in palabra:
        if letra not in fuente:
            fuente += letra
    ListaP = [palabra.count(letra)/len(palabra) for letra in fuente] #Calcula la probabilidad de cada simbolo
    return fuente, ListaP

palabra = input("Ingrese una palabra: ")
fuente, ListaP = genera_fuente(palabra)

print("Fuente: ", fuente)
print("Probabilidades: ", ListaP)

print("Codificado de Huffman:    ", Huffman(ListaP))

print("Codificado de Shannon-Fano:    ", ShannonFano(ListaP))