import math
import random
import copy 
import tdi 

def generalistainfoN(listap,base):
    return [math.log(1/prob,base) for prob in listap]

def entropia(listap,base):
        entropia=0
        informacion=generalistainfoN(listap,base)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia

def entropiabin(w):
        return (w*math.log2(1/w)+(1-w)*math.log2(1/(1-w)))

def cuentasimbolos(palabra):
   simbolos=[]
   cant=[]
   for i in palabra:
          if i in simbolos:
               cant[simbolos.index(i)]+=1
          else:
              simbolos.append(i)
              cant.append(1)
   return simbolos,cant

def probabilidadlista(simbolos,cant):
     listaprob=[]
     total=sum(cant)
     
     for i in simbolos:
        listaprob.append(cant[simbolos.index(i)]/total)
     return listaprob

def MatrizDeTransicion (simbolos,cad):
    matT = [ [0 for _ in range(len(simbolos))] for _ in range(len(simbolos))]
    cadL = list(cad) #a la cadena la hago lista
    for i in range(len(simbolos)):
        for j in range(len(simbolos)):
            canti = 0
            for k in range(len(cadL) - 1): #cuento apariciones de la dupla
                if cadL[k] == simbolos[i] and cadL[k+1] == simbolos[j]:
                    canti += 1
            matT[i][j] = canti # pongo cant de la dupla en la ubicacion de la matriz

    for j in range(len(matT)):
        tot = 0
        for i in range(len(matT)):
            tot += matT[i][j] #sumo cantidades de esa letra por columna
        
        for i in range(len(matT)):
            matT[i][j] = matT[i][j] / tot
    
    return matT

def getcolumna(matriz,alfabeto,caracter):
    aux=[]
    for i in matriz:
        aux.append(i[alfabeto.index(caracter)])
    
    return aux

def simularMensaje(simbolos,matriz,longitud,simbolo_inicial):
    mensaje = []
    if simbolo_inicial == '':
        simbolo_inicial = random.choice(simbolos)[0]
    mensaje.append(simbolo_inicial)

    for x in range(longitud - 1):
        simbolo_actual = mensaje[-1]
        columna=getcolumna(matriz,simbolos,simbolo_actual)
        siguiente_simbolo=random.choices(simbolos,weights=columna,k=1)[0]
        mensaje.append(siguiente_simbolo)

    return mensaje


def tipofuente (matT, tol):
    r = 1
    i = 0
    while (i in range(len(matT))) and r: 
        fila = matT[i] # le doy la fila entera
        j = 0
        while j in range(len(fila) - 1) and r: # recorro fila
            k = j + 1
            while k in range(len(fila)) and r:
                if fila[j] - fila[k] > tol:
                    r = 0
                k += 1
            j += 1
        i += 1
    if r:
        print("Fuente de memoria nula")
    else:
        print("Fuente de memoria no nula")

def entropiamatT(matT,vecest):
        entropi=0  
        for fila in range(len(vecest)):  
         suma=entropia(matT[fila],2)                             
         entropi+=suma*vecest[fila]                                                                                        
        return entropi

def calculaordenN(alfabeto, prob,n):
    if n==1:
        return alfabeto,prob
    else:
        
        L,P= calculaordenN(alfabeto,prob,n-1)
        aux=[]
        auxp=[]

        for x in range(len(L)):
            for y in range(len(alfabeto)):
                aux.append(L[x] + alfabeto[y])
                auxp.append(P[x] * prob[y])

        return aux,auxp

def vectorest(matriz,vecest,tolerancia):
    cumple=False
    
    while cumple==False:
           cumple=True
           vecaux=[0,0,0]
           for i in range(3):
            for j in range(3):
                vecaux[i]+=vecest[j]*matriz[i][j]
            if (abs(vecaux[i]-vecest[i])>=tolerancia):
                cumple=False
           vecest=vecaux    
    return vecest


def esNoSingular (C):
    n = len(C)
    for i in range(n):
        for j in range(n):
            if (i != j):
                if (C[i] == C[j]):
                    return False                    
    return True

def esInstantaneo (C):
    if esNoSingular(C) == False:
        return False
    else:
        n = len(C)
        for i in range(n):
            for j in range(n):
                if (i != j):
                    if C[i].startswith(C[j]):
                        return False
        return True

def esUnivoco (C):
    if esInstantaneo(C) == True:
        return True
    else: 
        S = C
        ST = []
        while True:
            aux = []
            for x in S:
                for y in C:
                    if x != y: 
                        if x.startswith(y):
                            diferencia = x[len(y):]
                            if diferencia not in aux:
                                aux.append(diferencia)
                        else:
                            if y.startswith(x):
                                diferencia = y[len(x):]
                                if diferencia not in aux:
                                  aux.append(diferencia)
            ST.append(S)
            S = aux
            if all(x not in C for x in S) and (S not in ST):
                continue
            else:
                break
        if (S in ST):
            return True
        else: 
            return False

def creastringcodigo (C):        #lo traemos del ejercicio anterior porque necesitamos la cantidad de simbolos de x (r)
    cadena = ""
    for c in C:
        for x in c:
            if not x in cadena:
                cadena += x
    return cadena


def esCompacto (codigo, prob):
    if esInstantaneo(codigo) == False:
        return False
    else:     
        r=len(creastringcodigo(codigo))
        aux = [math.ceil(abs(math.log(x,r))) for x in prob]
        if all(len(x)<= y for x,y in zip(codigo, aux)):
            return True
        else:
            return False
        

#devuelve r
def cadcod(listacodigos):
    cadena=''
    for cod in listacodigos:
        for x in cod:
            if not x in cadena:
                cadena+=x
    return cadena

def longitud(listacodigos):    # (devuelve long de cada codigo)
    listaux=([len(long) for long in listacodigos]) 
    return listaux

def kraft(listacodigos):
   r=len(cadcod(listacodigos))
   long=longitud(listacodigos)
   suma=0
   for x in long:
        suma+=r**-x
   return suma

def longitudMedia(listacodigos,listaprob):
    L=0
    for p,i in zip(listaprob,listacodigos):
        L+=len(i)*p
    return L


def primershannon(codigos2,prob2,orden): 
    codigos,prob=calculaordenN(codigos2,prob2,orden)
    r=len(cadcod(codigos))
    ent=entropia(prob,r)
    L=longitudMedia(codigos,prob)
    print(ent," <= ",L," <= ",ent+1)

    if (ent<=L) and (L<=ent+1):
        return True
    else:
        return False


def rendimiento(cod,prob):
    ent=entropia(prob,len(cadcod(cod)))
    L=longitudMedia(cod,prob)
    return ent/L

def redundancia(cod,prob):
    ent=entropia(prob,len(cadcod(cod)))
    L=longitudMedia(cod,prob)
    return (L-ent)/L

# Algoritmo de Huffman
def Huffman (probs):
    # pares probabilidad, indice
    items = [[p, [i]] for i, p in enumerate(probs)]
    
    codigo = [""] * len(probs)

    # hasta q quede uno solo
    while len(items) > 1:
        
        items.sort(reverse = True, key = lambda x: x[0]) # ordena la lista decrecientemente por el primer elemento (probs)
        
        # saco de items los dos elementos de menor probabilidad
        menor = items.pop()
        segMenor = items.pop()

        # armo codigo de cada simbolo a partir de concatenar a la izquierda, 0 o 1 segun corresponda
        for i in menor[1]:
            codigo[i] = "0" + codigo[i]
        for i in segMenor[1]:
            codigo[i] = "1" + codigo[i]
        
        # sumo las probabilidades y pongo los indices juntos
        sumaProb = menor[0] + segMenor[0]
        nuevoElem = [sumaProb, menor[1] + segMenor[1]]

        # inserto el elemento nuevo en items, ahora con las probs e indices juntos
        items.append(nuevoElem)

    print("Símbolo | Prob | Código Huffman")
    for i, c in enumerate(codigo):
        print(f"   {i}     | {probs[i]}  |  {c}")

    # return codigo

#palabra = 'ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB'
#simbolos,cant=cuentasimbolos(palabra)
#prob=[0.2, 0.2, 0.3, 0.3]

#print("Fuente: ", simbolos)
#print("Probabilidades: ", prob)

#print("Codificado de Huffman:    ", Huffman(prob))
#print("Codificado de Shannon-Fano:    ", ShannonFano(prob))
def Huffman(probs):
    nodos = [[p, [i]] for i, p in enumerate(probs)]
    codigos = ["" for _ in range(len(probs))]
    while len(nodos) > 1:
        nodos.sort(key=lambda x: x[0])
        izq = nodos.pop(0)              
        der = nodos.pop(0)
        for i in izq[1]:
            codigos[i] = '0' + codigos[i]
        for i in der[1]:
            codigos[i] = '1' + codigos[i]
        nuevo = [izq[0] + der[0], izq[1] + der[1]]
        nodos.append(nuevo)
    return codigos

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

def rendimiento(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return ent/L

def redundancia(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return (L-ent)/L

def calculamensaje(palabra):
    simbolos,cant=cuentasimbolos(palabra)
    prob=probabilidadlista(simbolos,cant)
    return simbolos,prob

def codificar_mensaje(mensaje, fuente, codificacion): #Lo convierte en un ByteArray
    mensaje_codificado = bytearray()
    buffer = ''
    
    for c in mensaje:
        indice = fuente.index(c)
        buffer+= codificacion[indice]

    while len(buffer) >= 8:
        byte = buffer[:8]
        buffer = buffer[8:]
        mensaje_codificado.append(int(byte, 2))  # convierte '10101100' → entero → byte

    # Si quedan bits sobrantes, rellenamos con ceros a la derecha
    bits_sobrantes = 0
    if buffer:
        bits_sobrantes = 8 - len(buffer)
        byte = buffer.ljust(8, '0')
        mensaje_codificado.append(int(byte, 2))
     
    return mensaje_codificado,bits_sobrantes

def decodificar_mensaje(mensaje, fuente, codificacion, bits_sobrantes): #Analiza un ByteArray
    
    bits = ''.join(f'{byte:08b}' for byte in mensaje)

    mensaje_decodificado = ""
    buffer = ""

    # Recorremos los bits reconstruyendo los símbolos originales

    if bits_sobrantes > 0:
        bits = bits[:-(bits_sobrantes)]

    for bit in bits:
        buffer += bit
        if buffer in codificacion:
            indice = codificacion.index(buffer)
            mensaje_decodificado += fuente[indice]
            buffer = ""
    return mensaje_decodificado

def rlc_encode(mensaje):
    resultado = bytearray()
    n = len(mensaje)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and mensaje[i] == mensaje[i + 1]:
            count += 1
            i += 1
        resultado.append(ord(mensaje[i])) 
        resultado.append(count)            
        i += 1
    return resultado

def rlc_decode(mensaje):
    resultado = []
    n = len(mensaje)
    i = 0
    while i < n:
        char = chr(mensaje[i]) 
        count = mensaje[i + 1] 
        resultado.append(char * count)
        i += 2
    return ''.join(resultado)

def ratioCompresion(original, comprimido):
    return len(original) / len(comprimido)

def distanciaDeHamming(lista):
    n = len(lista)
    if n < 2:
        return 0 
    distancia_minima = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            distancia = sum(c1 != c2 for c1, c2 in zip(lista[i], lista[j]))
            if distancia < distancia_minima:
                distancia_minima = distancia
    print('Distancia de Haming: ', distancia_minima)
    print('Cantidad de errores que se pueden detectar: ', int(distancia_minima - 1))
    print('Cantidad de errores que se pueden corregir: ', int((distancia_minima - 1) / 2))

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

def calculaEntropiaFilaCanal(matriz_de_transicion):
    entropia = 0
    if not matriz_de_transicion: 
        return 0
    for p in matriz_de_transicion[0]:
        if p > 0:
            entropia += p * math.log2(1/p)
    return entropia

def columnasReducibles(matriz_del_canal, index1, index2):
    num_filas = len(matriz_del_canal)
    if num_filas == 0:
        return False
    constante_c = None 
    for i in range(num_filas):
        val1 = matriz_del_canal[i][index1]
        val2 = matriz_del_canal[i][index2]
        
        if not math.isclose(val2, 0.0):
            ratio_actual = val1 / val2           
            if constante_c is None:
                constante_c = ratio_actual
            else:
                if not math.isclose(ratio_actual, constante_c):
                    return False 
        else: 
            if not math.isclose(val1, 0.0):
                return False
    return True

def matrizCanalCompuesto(matriz_a, matriz_b):
    filas_a = len(matriz_a)
    if filas_a == 0: return []
    cols_a = len(matriz_a[0])
    filas_b = len(matriz_b)
    if filas_b == 0: return []
    cols_b = len(matriz_b[0])

    if cols_a != filas_b:
        raise ValueError(f"Dimensiones incompatibles: Col(A)={cols_a} != Filas(B)={filas_b}")
    
    matriz_c = []
    for i in range(filas_a):
        fila = [0.0] * cols_b
        matriz_c.append(fila)
    
    for i in range(filas_a):      
        for j in range(cols_b):     
            suma = 0.0
            for k in range(cols_a): 
                suma += matriz_a[i][k] * matriz_b[k][j]
            matriz_c[i][j] = suma
    return matriz_c

def generar_matriz_reduccion(num_columnas_original, index1, index2):
    M = num_columnas_original
    M_reducido = M - 1
    col_a_mantener = min(index1, index2)
    col_a_eliminar = max(index1, index2)
    
    matriz_r = []
    for i in range(M):
        matriz_r.append([0.0] * M_reducido)
    
    j_nuevo = 0
    indice_destino_mantener = 0 
    
    for j_viejo in range(M):
        if j_viejo == col_a_eliminar:
            matriz_r[j_viejo][indice_destino_mantener] = 1.0
        elif j_viejo == col_a_mantener:
            matriz_r[j_viejo][j_nuevo] = 1.0
            indice_destino_mantener = j_nuevo 
            j_nuevo += 1
        else:
            matriz_r[j_viejo][j_nuevo] = 1.0
            j_nuevo += 1
            
    return matriz_r

def multiplicarMatrices(A, B):
    filas_a = len(A)
    cols_a = len(A[0])
    filas_b = len(B)
    cols_b = len(B[0])
    
    if cols_a != filas_b:
        raise ValueError("Dimensiones incompatibles")

    C = [[0.0] * cols_b for _ in range(filas_a)]
    
    for i in range(filas_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += A[i][k] * B[k][j]
    return C

def calculaCapacidadCanal(matriz_de_transicion):
    N = len(matriz_de_transicion)
    if N == 0: return 0
    M = len(matriz_de_transicion[0])
    
    if esCanalDeterminante(matriz_de_transicion):
        return round(math.log2(M), 4)
    elif esCanalSinRuido(matriz_de_transicion):
        return round(math.log2(N), 4)
    elif esCanalUniforme(matriz_de_transicion): 
        h_fila = calculaEntropiaFilaCanal(matriz_de_transicion)
        return round(math.log2(M) - h_fila, 4)
    else:
        print("El canal no es de un tipo especial. Usar método numérico.")
        return -1

def probDeError(matriz_de_transicion, probs_a_priori):
    matriz_copiada = copy.deepcopy(matriz_de_transicion)
    suma=0.0
    for j in range(len(matriz_copiada[0])):
        maximo = 0
        aux = 0
        for i in range(len(matriz_copiada)):
            if matriz_copiada[i][j] > maximo:
                maximo = matriz_copiada[i][j]
                aux = i
        matriz_copiada[aux][j] = 0.0

        for i in range(len(matriz_copiada[0])):
            suma+= matriz_copiada[i][j] * probs_a_priori[i]

    return round(suma, 4)