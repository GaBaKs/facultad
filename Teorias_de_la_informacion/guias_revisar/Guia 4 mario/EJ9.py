import math

#-------------------------------- EJERCICIO 9 ---------------------------------
# Dadas las siguientes fuentes, generar códigos de Huffman y de Shannon-Fano:
# a) Listap = [0.2, 0.2, 0.3, 0.3]
# b) Listap = [0.4, 0.25, 0.25, 0.1]
#-------------------------------- EJERCICIO 9 ---------------------------------

def ShannonFanon(probabilidades):
    items = [[p, i] for i, p in enumerate(probabilidades)]
    codigo = ['' for _ in range(len(probabilidades))]
    items.sort(reverse=True)
    def recShannonFanon(items, codigo):
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
            recShannonFanon(items[:i + 1], codigo)
            recShannonFanon(items[i + 1:], codigo)
    recShannonFanon(items, codigo)
    return codigo

ListaPA = [0.2, 0.2, 0.3, 0.3]
ListaPB = [0.4, 0.25, 0.25, 0.1]

print("Shannon-Fanon A:    ", ShannonFanon(ListaPA))

print("Shannon-Fanon B:    ", ShannonFanon(ListaPB))
