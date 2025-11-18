import math

#devuelve un alfabeto unico ordenado
def generaCadenaCodificada(cadena):
    alfabeto = sorted(list(set(cadena)))
    return alfabeto

def cadenaADistribucion(cadena):
    alfabeto = generaCadenaCodificada(cadena)
    apariciones = []
    for simbolo in alfabeto:
        apariciones.append(cadena.count(simbolo))
    total_simbolos = len(cadena)
    distribucion = [a / total_simbolos for a in apariciones]
    return alfabeto, distribucion

def entropiaAPriori(probs_a_priori):
    entropia = 0
    for p in probs_a_priori:
        if p > 0:
            entropia += p * math.log2(1/p)
    return round(entropia, 4)

def generaMatrizCanal(cad1, cad2):
    aux1 = generaCadenaCodificada(cad1)
    aux2 = generaCadenaCodificada(cad2)
    n = len(aux1)
    m = len(aux2)
    matriz = [[0 for j in range(m)] for i in range(n)]
    for i in range(len(cad1)):
        fila = aux1.index(cad1[i])
        col = aux2.index(cad2[i])
        matriz[fila][col] += 1
    for i in range(n):
        total = cad1.count(aux1[i])
        if total > 0:
            for j in range(m):
                matriz[i][j] /= total
    return matriz

def probsDeSalida(probs_a_priori, matriz_de_transicion):
    N = len(probs_a_priori)
    M = len(matriz_de_transicion[0])
    probs_salida = []
    for j in range(M):
        acum = 0
        for i in range(N):
            acum += matriz_de_transicion[i][j] * probs_a_priori[i]
        probs_salida.append(acum)
    return probs_salida

def calculaProbsSimultaneas(probs_a_priori, matriz_de_transicion):
    N = len(probs_a_priori)
    M = len(matriz_de_transicion[0])
    probs_simultaneas = []
    for i in range(N):
        fila_simultanea = []
        for j in range(M):
            prob_simultanea = probs_a_priori[i] * matriz_de_transicion[i][j]
            fila_simultanea.append(prob_simultanea)
        probs_simultaneas.append(fila_simultanea)
    return probs_simultaneas

def calculaProbsAPosteriori(probs_a_priori, matriz_de_transicion):
    N = len(probs_a_priori)
    M = len(matriz_de_transicion[0])
    probs_salida = probsDeSalida(probs_a_priori, matriz_de_transicion)
    probs_simultaneas = calculaProbsSimultaneas(probs_a_priori, matriz_de_transicion)
    probs_a_posteriori = []
    for i in range(N):
        fila_posteriori = []
        for j in range(M):
            prob_simultanea = probs_simultaneas[i][j]
            prob_salida = probs_salida[j]
            if prob_salida != 0:
                prob_post = prob_simultanea / prob_salida
            else:
                prob_post = 0
            fila_posteriori.append(prob_post)
        probs_a_posteriori.append(fila_posteriori)
    return probs_a_posteriori

def entropiaAPosteriori(probs_a_priori, matriz_de_transicion):
    N = len(probs_a_priori)
    M = len(matriz_de_transicion[0])
    probs_a_posteriori = calculaProbsAPosteriori(probs_a_priori, matriz_de_transicion)
    entropia = []
    for j in range(M):
        H = 0
        for i in range(N):
            p = probs_a_posteriori[i][j]
            if p > 0:
                H += p * math.log2(1/p)
        entropia.append(H)
    return entropia

def calculaRuido(probs_a_priori, matriz_de_transicion):
    N = len(probs_a_priori)
    M = len(matriz_de_transicion[0])
    probs_salida = probsDeSalida(probs_a_priori, matriz_de_transicion)
    entropia_a_posteriori = entropiaAPosteriori(probs_a_priori, matriz_de_transicion)
    H_media = 0
    for j in range(M):
        H_media += probs_salida[j] * entropia_a_posteriori[j]
    return round(H_media, 4)

def calculaInformacionMutua(probs_a_priori, matriz_de_transicion):
    h_a = entropiaAPriori(probs_a_priori)
    h_a_dado_b = calculaRuido(probs_a_priori, matriz_de_transicion)
    info_mutua = h_a - h_a_dado_b
    return round(info_mutua, 4)

def calculaEntropiaAfin(probs_a_priori, matriz_de_transicion):
    probs_simultaneas = calculaProbsSimultaneas(probs_a_priori, matriz_de_transicion)
    N = len(probs_simultaneas)
    if N == 0:
        return 0
    M = len(probs_simultaneas[0])
    entropia = 0
    for i in range(N):
        for j in range(M):
            if probs_simultaneas[i][j] > 0:
                entropia += probs_simultaneas[i][j] * math.log2(1/probs_simultaneas[i][j])
    return round(entropia, 4)

def esCanalSinRuido(matriz_de_transicion):
    for j in range(len(matriz_de_transicion[0])):
        cont = 0
        for i in range(len(matriz_de_transicion)):
            if not math.isclose(matriz_de_transicion[i][j], 0.0):
                cont += 1
        if cont > 1:
            return False
    return True

def esCanalDeterminante(matriz_de_transicion):
    for i in range(len(matriz_de_transicion)):
        cont = 0
        for j in range(len(matriz_de_transicion[0])):
            if math.isclose(matriz_de_transicion[i][j], 1.0):
                cont += 1
        if cont != 1:
            return False
    return True

def esCanalUniforme(matriz_del_canal):
    if not matriz_del_canal:
        return False
    primera_fila_ordenada = sorted(matriz_del_canal[0])
    for i in range(1, len(matriz_del_canal)):
        fila_actual_ordenada = sorted(matriz_del_canal[i])
        if len(primera_fila_ordenada) != len(fila_actual_ordenada):
            return False
        for k in range(len(primera_fila_ordenada)):
            if not math.isclose(primera_fila_ordenada[k], fila_actual_ordenada[k]):
                return False
    return True

entrada="abcacaabbcacaabcacaaabcaca"
alfent=generaCadenaCodificada(entrada)
salida="01010110011001000100010011"
alfsal=generaCadenaCodificada(salida)



matriz_canal=generaMatrizCanal(entrada,salida)

print("Matriz: ",matriz_canal)

# Muestra matriz segun par (i,j)
for i in range(len(matriz_canal)): # i es el índice de la fila
    for j in range(len(matriz_canal[i])): # j es el índice de la columna
        print(f"  ({alfent[i]}, {alfsal[j]}) = {matriz_canal[i][j]: .4f}", end=" ")
    print() # salto de línea para pasar a la siguiente fila

