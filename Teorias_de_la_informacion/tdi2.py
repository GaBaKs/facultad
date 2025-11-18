import math
import copy 
import tdi 

# ==============================================================================
# BLOQUE 1: CODIFICACIÓN DE FUENTE (Compresión sin pérdida)
# ==============================================================================

# ------------------------------------------------------------------------------
# Teorema de Shannon (Primer Teorema)
# ------------------------------------------------------------------------------
# Parámetros:
#   - alfabeto (list): Lista de los símbolos únicos de la fuente (ej: ['A', 'B']).
#   - probabilidades (list): Lista de probabilidades asociadas a cada símbolo.
#   - n (int): El orden de la extensión a verificar (ej: 2, 3...).
# Retorno:
#   - bool: Devuelve True si se cumple la desigualdad del teorema, False si no.
#
# Análisis para el Parcial:
# - Este teorema establece el límite fundamental de la compresión sin pérdida.
# - Verifica la desigualdad: H(S) <= L_media < H(S) + 1/n.
# - Si n (extensión) aumenta, la longitud media por símbolo se acerca asintóticamente
#   a la Entropía H(S).
# - Úsalo para justificar por qué al agrupar símbolos (extensión) mejora la eficiencia.
# ------------------------------------------------------------------------------
def teoremaDeShannon(alfabeto, probabilidades, n):
    entropia = tdi.entropiaBaseR(alfabeto, probabilidades)
    alfabetoExtendido = []
    probExtendidas = []
    tdi.extensionN(alfabeto, probabilidades, n, alfabetoExtendido, probExtendidas, n-1)
    longitud_media = tdi.longitudMedia(alfabetoExtendido, probExtendidas)
    print("Entropia: ", round(entropia, 2))
    print("Longitud Media (sub n): ", longitud_media)
    return (entropia <= longitud_media/n and longitud_media/n <= entropia+1/n)

# ------------------------------------------------------------------------------
# Teorema de Shannon Extendido
# ------------------------------------------------------------------------------
# Parámetros:
#   - alfabeto (list): Lista de símbolos (aunque la función usa un auxiliar interno).
#   - probabilidades (list): Lista de probabilidades de la fuente original.
#   - n (int): Orden de la extensión.
# Retorno:
#   - bool: True si se cumple la desigualdad con el alfabeto extendido.
#
# Análisis para el Parcial:
# - Similar al anterior, pero maneja la lógica de extensión de probabilidades internamente.
# - Recuerda: La entropía de la extensión n es n * H(S).
# - La compresión mejora a costa de aumentar exponencialmente el tamaño del diccionario.
#NOTA: Esta funcion calcula extension de las probabilidades para asociarlas a un alfabeto que se supone extendido
# es decir, me dan una posible codificacion y las probabilidades de los simbolos originales
# ------------------------------------------------------------------------------
def teoremaDeShannonExt(alfabeto, probabilidades, n):
    entropia = tdi.entropiaBaseR(alfabeto, probabilidades)
    alfabetoExtendido = []
    aux = ['a' for i in range(len(probabilidades))]
    probExtendidas = []
    tdi.extensionN(aux, probabilidades, n, alfabetoExtendido, probExtendidas, n-1)
    longitud_media = tdi.longitudMedia(alfabeto, probExtendidas)
    print("Entropia: ", round(entropia, 2))
    print("Longitud Media (sub n): ", round(longitud_media, 2))
    return (entropia <= longitud_media/n and longitud_media/n <= entropia+1/n)

# ------------------------------------------------------------------------------
# Cálculo de Rendimiento y Redundancia
# ------------------------------------------------------------------------------
# - El Rendimiento indica cuánta información real hay por cada bit que se envía.
# Parámetros:
#   - alfabeto (list): Lista de símbolos del código propuesto.
#   - probabilidades (list): Distribución de probabilidades de la fuente.
# Retorno:
#   - tuple (float, float): Un par de valores (rendimiento, redundancia).
#
# Análisis para el Parcial:
# - Rendimiento (eta): H(S) / L. Indica qué tan eficiente es el código (máx 1 o 100%).
# - Redundancia: 1 - Rendimiento. Indica cuánto espacio se desperdicia.
# - Un código óptimo (Huffman) intenta minimizar la redundancia.
# - Si L = H(S), el rendimiento es 1 (código compacto ideal).
# ------------------------------------------------------------------------------
def calculaRendimiento(alfabeto, probabilidades):
    entropia = tdi.entropiaBaseR(alfabeto, probabilidades)
    longitud_media = tdi.longitudMedia(alfabeto, probabilidades)
    rendimiento = entropia / longitud_media
    redundancia = 1 - rendimiento
    return rendimiento, redundancia

# ------------------------------------------------------------------------------
# Algoritmo de Huffman
# ------------------------------------------------------------------------------
# Parámetros:
#   - probs (list): Lista de probabilidades de los símbolos (deben sumar 1.0).
# Retorno:
#   - list: Lista de cadenas binarias (los códigos) correspondientes a cada probabilidad.
#
# Análisis para el Parcial:
# - Es un código ÓPTIMO (genera la menor longitud media posible símbolo a símbolo).
# - Es un código prefijo (instantáneo): ninguna palabra es prefijo de otra.
# - Construcción: "Bottom-up" (de abajo hacia arriba). Se agrupan los dos menos probables.
# - Importante: Siempre L_Huffman < L_ShannonFano (o igual en el mejor caso).
# - "Si bien ambos algoritmos buscan asignar códigos cortos a símbolos probables, Huffman tiene mayor rendimiento (o igual) 
# porque construye el árbol de codificación de manera exacta basándose en las probabilidades individuales paso a paso de abajo hacia arriba y de forma recursiva. 
# En cambio, Shannon-Fano intenta aproximar divisiones ideales de probabilidad arriba hacia abajo, lo cual no siempre resulta en la longitud media mínima posible."
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Algoritmo de Shannon-Fano
# ------------------------------------------------------------------------------
# Parámetros:
#   - probabilidades (list): Lista de probabilidades de los símbolos.
# Retorno:
#   - list: Lista de cadenas binarias (los códigos) correspondientes a cada símbolo.
#
# Análisis para el Parcial:
# - Es un código SUB-ÓPTIMO.
# - Construcción: "Top-down" (división sucesiva). Se intenta dividir el conjunto de
#   probabilidades en dos mitades que sumen lo mismo (o lo más cercano posible).
# - Puede dar lugar a códigos menos eficientes que Huffman si las divisiones no son equilibradas.
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Funciones de Codificación (Encoder/Decoder)
# ------------------------------------------------------------------------------
# Parámetros (Encoder):
#   - cadena (str): Mensaje original a comprimir.
#   - fuente (list): Lista de símbolos del alfabeto fuente.
#   - codigo (list): Lista de códigos binarios asignados a la fuente (ej: Huffman).
# Retorno (Encoder):
#   - bytearray: Los datos comprimidos en formato binario (listos para guardar).
#
# Parámetros (Decoder):
#   - fuente (list): Lista de símbolos originales.
#   - codigo (list): Lista de códigos binarios (el diccionario).
# Retorno (Decoder):
#   - str: El mensaje original reconstruido.
#
# Análisis para el Parcial:
# - Estas funciones simulan la transmisión real.
# - El encoder empaqueta bits en bytes (rellenando con ceros si es necesario).
# - El decoder requiere el diccionario (fuente + códigos) para reconstruir el mensaje.
# - Esto ilustra que el código debe ser unívocamente decodificable.
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Run Length Coding (RLC)
# ------------------------------------------------------------------------------
# Parámetros (rlc_encode):
#   - mensaje (str): Cadena de texto a comprimir (ej: "AAAABBB").
# Retorno (rlc_encode):
#   - bytearray: Secuencia de pares [carácter, cantidad].
#
# Parámetros (rlc_decode):
#   - mensaje (bytearray): El mensaje codificado con RLC.
# Retorno (rlc_decode):
#   - str: El mensaje original expandido.
#
# Análisis para el Parcial:
# - Método de compresión simple basado en repeticiones consecutivas.
# - Ideal para fuentes con baja entropía local (muchos símbolos repetidos seguidos),
#   como imágenes binarias simples o fondos uniformes.
# - Si la fuente tiene alta entropía (mucha variabilidad), RLC puede AUMENTAR el tamaño
#   del archivo (rendimiento negativo).
# ------------------------------------------------------------------------------
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

# ==============================================================================
# BLOQUE 2: CONTROL DE ERRORES (Hamming y Paridad)
# ==============================================================================

# ------------------------------------------------------------------------------
# Distancia de Hamming
# ------------------------------------------------------------------------------
# Parámetros:
#   - lista (list): Lista de palabras código (cadenas binarias de igual longitud).
# Retorno:
#   - No retorna valor (imprime los resultados en consola: distancia, detección y corrección).
#
# Análisis para el Parcial:
# - Es la cantidad de bits que difieren entre dos palabras código.
# - Distancia mínima del código (d_min): Es la menor distancia entre cualquier par de palabras válidas.
# - Capacidad de DETECCIÓN: Se detectan hasta (d_min - 1) errores.
# - Capacidad de CORRECCIÓN: Se corrigen hasta (d_min - 1) / 2 errores (división entera).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Paridad (VRC)
# ------------------------------------------------------------------------------
# Parámetros (char_a_byte...):
#   - char (char): Carácter a codificar.
# Retorno (char_a_byte...):
#   - str: Cadena de 8 bits (7 de datos + 1 paridad par).
#
# Parámetros (verificar_byte...):
#   - byte (str): Cadena de 8 bits recibida.
# Retorno (verificar_byte...):
#   - bool: True si la paridad es correcta, False si hay error.
#
# Análisis para el Parcial:
# - Mecanismo simple de detección (no corrección por sí solo).
# - Se añade 1 bit para hacer que el número total de unos sea par (paridad par) o impar.
# - Aumenta la distancia de Hamming a 2 (detecta errores simples).
# ------------------------------------------------------------------------------
def char_a_byte_con_paridad(char):
    ascii_val = ord(char)
    binario_7bits = format(ascii_val, '07b')
    num_bits_1 = binario_7bits.count('1')
    bit_paridad = '1' if num_bits_1 % 2 == 0 else '0'
    byte_con_paridad = binario_7bits + bit_paridad
    return byte_con_paridad

def verificar_byte_con_paridad(byte):
    binario_7bits = byte[:7]
    bit_paridad = byte[7]
    num_bits_1 = binario_7bits.count('1')
    paridad_calculada = '1' if num_bits_1 % 2 == 0 else '0'
    return paridad_calculada == bit_paridad

# ==============================================================================
# BLOQUE 3: CANALES DE INFORMACIÓN (Teoría de Canal Discreto sin Memoria)
# ==============================================================================

# ------------------------------------------------------------------------------
# Funciones Utilitarias de Fuente
# ------------------------------------------------------------------------------
# Parámetros:
#   - cadena (str): Texto o secuencia de datos a analizar.
# Retorno:
#   - generaCadenaCodificada -> list: Alfabeto único ordenado.
#   - cadenaADistribucion -> tuple: (alfabeto, lista_de_probabilidades).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Entropía a Priori H(A)
# ------------------------------------------------------------------------------
# Parámetros:
#   - probs_a_priori (list): Probabilidades P(ai) de la entrada.
# Retorno:
#   - float: Valor de la entropía H(A) en bits.
#
# Análisis para el Parcial:
# - H(A) = Σ P(ai) log(1/P(ai)).
# - Es la incertidumbre inicial antes de usar el canal.
# - Es el límite máximo de información que se podría recuperar si el canal fuera perfecto.
# ------------------------------------------------------------------------------
def entropiaAPriori(probs_a_priori):
    entropia = 0
    for p in probs_a_priori:
        if p > 0:
            entropia += p * math.log2(1/p)
    return round(entropia, 4)

# ------------------------------------------------------------------------------
# Matriz de Transición del Canal P(bj/ai)
# ------------------------------------------------------------------------------
# Parámetros:
#   - cad1 (str): Cadena enviada (Entrada A).
#   - cad2 (str): Cadena recibida (Salida B).
# Retorno:
#   - list[list[float]]: Matriz donde M[i][j] es P(bj/ai).
#
# Análisis para el Parcial:
# - Las filas deben sumar 1. Representan P(Salida | Entrada).
# - Se construye empíricamente comparando qué se envió vs qué se recibió.
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Probabilidades de Salida P(bj)
# ------------------------------------------------------------------------------
# - Es la probabilidad "global" de que aparezca un cierto símbolo en el receptor, sin importar de dónde vino. En criollo, contar 0s y 1s sin mas.
# Parámetros:
#   - probs_a_priori (list): Probabilidades de entrada P(ai).
#   - matriz_de_transicion (list[list]): Matriz del canal P(bj/ai).
# Retorno:
#   - list: Probabilidades de salida P(bj).
#
# Análisis para el Parcial:
# - Probabilidad Total: P(bj) = Σ P(ai) * P(bj/ai).
# - Necesario para calcular H(B) y aplicar Bayes para las probabilidades a posteriori.
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Probabilidades Simultáneas P(ai, bj)
# ------------------------------------------------------------------------------
# - Probabilidad de que ocurra el par (ai, bj).
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - list[list]: Matriz conjunta P(ai, bj).
#
# Análisis para el Parcial:
# - P(ai, bj) = P(ai) * P(bj/ai).
# - Representa la probabilidad conjunta de que ocurra el par entrada-salida.
# - La suma de toda esta matriz debe ser 1.
# - Base para calcular H(A,B).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Probabilidades a Posteriori P(ai/bj)
# ------------------------------------------------------------------------------
# - Esta es la probabilidad "hacia atrás". Es la que mira el receptor después (a posteriori) de haber recibido un dato. Contar 0s y 1s a la salida y ver de dónde vinieron.
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - list[list]: Matriz de probabilidades inversas P(ai/bj).
#
# Análisis para el Parcial:
# - Teorema de Bayes: P(ai/bj) = P(ai, bj) / P(bj).
# - Es la "visión del receptor": Dado que recibí 'bj', ¿cuál es la prob. de que enviaran 'ai'?
# - Fundamental para el Decodificador Ideal (elegir el ai con máx P(ai/bj)).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Entropía a Posteriori H(A/bj)
# ------------------------------------------------------------------------------
# - Es la media de la incertidumbre que queda luego de recibir un simbolo. A mayor entropía, más dudas tengo de lo que se envio en promedio.
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - list: Lista de entropías, una por cada símbolo de salida 'bj'.
#
# Análisis para el Parcial:
# - Mide la incertidumbre restante sobre la entrada DESPUÉS de recibir un símbolo concreto 'bj'.
# - Si H(A/bj) = 0, recibir 'bj' me dice con total certeza qué se envió.
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Equivocación o Ruido del Canal H(A/B)
# ------------------------------------------------------------------------------
# - Es una manera de ponderar que tan seguro estoy de lo que se envio sabiendo lo que llego.
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - float: El valor medio del ruido en bits.
#
# Análisis para el Parcial:
# - Es el promedio ponderado de las entropías a posteriori H(A/bj).
# - Representa la información PERDIDA o incertidumbre promedio que queda sobre A después de haber visto la salida B.
# - Al acoplar canales en serie, el ruido NUNCA disminuye. La información mutua solo puede mantenerse o reducirse.
# - Si H(A/B) = 0, el canal es SIN RUIDO, lo que significa que al ver la salida bj sabes exactamente qué letra ai se envió.
# - Siempre H(A/B) <= H(A).
# ------------------------------------------------------------------------------
def calculaRuido(probs_a_priori, matriz_de_transicion):
    N = len(probs_a_priori)
    M = len(matriz_de_transicion[0])
    probs_salida = probsDeSalida(probs_a_priori, matriz_de_transicion)
    entropia_a_posteriori = entropiaAPosteriori(probs_a_priori, matriz_de_transicion)
    H_media = 0
    for j in range(M):
        H_media += probs_salida[j] * entropia_a_posteriori[j]
    return round(H_media, 4)

# ------------------------------------------------------------------------------
# Información Mutua I(A,B)
# ------------------------------------------------------------------------------
# - Cantidad de Información Útil o Valida que atraviesa el canal en un momento determinado.
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - float: Información mutua en bits.
#
# Análisis para el Parcial:
# - Tip: Pensalo como un Diagrama de Venn con H(A) y H(B).
# - EL CONCEPTO MÁS IMPORTANTE. Mide la información útil que atraviesa el canal.
# - Fórmulas:
#   1) I(A,B) = H(A) - H(A/B)  (Entropía Fuente - Ruido)
#   2) I(A,B) = H(B) - H(B/A)  (Entropía Salida - Pérdida)
#   3) I(A,B) = H(A) + H(B) - H(A,B)
# - Si I(A,B) = 0, el canal es inútil (salida independiente de entrada).
# - La CAPACIDAD C es el máximo de I(A,B).
# ------------------------------------------------------------------------------
def calculaInformacionMutua(probs_a_priori, matriz_de_transicion):
    h_a = entropiaAPriori(probs_a_priori)
    h_a_dado_b = calculaRuido(probs_a_priori, matriz_de_transicion)
    info_mutua = h_a - h_a_dado_b
    return round(info_mutua, 4)

# ------------------------------------------------------------------------------
# Entropía Afín o Conjunta H(A,B)
# ------------------------------------------------------------------------------
# - Incertidumbre total del sistema considerando pares (entrada, salida).
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - float: Entropía conjunta en bits.
#
# Análisis para el Parcial:
# - Incertidumbre total del sistema considerando pares (entrada, salida).
# - En el diagrama de Venn de entropías, es la unión de los conjuntos H(A) y H(B).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Pérdida del Canal H(B/A)
# ------------------------------------------------------------------------------
# - Es una manera de ponderar que tan seguro estoy de lo que llega al conocer lo que sale.
# Parámetros:
#   - probs_a_priori (list): P(ai).
#   - matriz_de_transicion (list[list]): P(bj/ai).
# Retorno:
#   - float: Pérdida en bits.
#
# Análisis para el Parcial:
# - A veces llamada "dispersión". Mide la incertidumbre de la salida dada la entrada.
# - H(B/A) = Σ P(ai) * H(B/ai).
# - Si H(B/A) = 0, el canal es DETERMINANTE (cada entrada produce una única salida fija).
# - En el diagrama de Venn, representa la parte de H(B) que no se solapa con H(A).
# ------------------------------------------------------------------------------
def calculaPerdida(probs_a_priori, matriz_de_transicion):
    probs_simultaneas = calculaProbsSimultaneas(probs_a_priori, matriz_de_transicion)
    N = len(probs_simultaneas)
    if N == 0:
        return 0
    M = len(probs_simultaneas[0])
    perdida = 0
    for i in range(N):
        for j in range(M):
            p_simultanea = probs_simultaneas[i][j] 
            if p_simultanea > 0:
                p_condicional = matriz_de_transicion[i][j]
                perdida += p_simultanea * math.log2(1/p_condicional)      
    return round(perdida, 4)

# ------------------------------------------------------------------------------
# Verificación: Canal Sin Ruido
# ------------------------------------------------------------------------------
# Parámetros:
#   - matriz_de_transicion (list[list]): Matriz del canal.
# Retorno:
#   - bool: True si es un canal sin ruido.
#
# Análisis para el Parcial:
# - Matriz: Máximo un valor no nulo por COLUMNA.
# - Implicación: H(A/B) = 0.
# - Conocer la salida identifica perfectamente la entrada.
# - I(A,B) = H(A). Capacidad = log2(N_entradas).
# ------------------------------------------------------------------------------
def esCanalSinRuido(matriz_de_transicion):
    for j in range(len(matriz_de_transicion[0])):
        cont = 0
        for i in range(len(matriz_de_transicion)):
            if not math.isclose(matriz_de_transicion[i][j], 0.0):
                cont += 1
        if cont > 1:
            return False
    return True

# ------------------------------------------------------------------------------
# Verificación: Canal Determinante
# ------------------------------------------------------------------------------
# Parámetros:
#   - matriz_de_transicion (list[list]): Matriz del canal.
# Retorno:
#   - bool: True si es un canal determinante.
#
# Análisis para el Parcial:
# - Matriz: Exactamente un 1.0 por FILA (resto ceros).
# - Implicación: H(B/A) = 0 (Pérdida nula).
# - I(A,B) = H(B). Capacidad = log2(N_salidas).
# ------------------------------------------------------------------------------
def esCanalDeterminante(matriz_de_transicion):
    for i in range(len(matriz_de_transicion)):
        cont = 0
        for j in range(len(matriz_de_transicion[0])):
            if math.isclose(matriz_de_transicion[i][j], 1.0):
                cont += 1
        if cont != 1:
            return False
    return True

# ------------------------------------------------------------------------------
# Canal Compuesto (En Serie)
# ------------------------------------------------------------------------------
# Parámetros:
#   - matriz_a (list[list]): Matriz del primer canal.
#   - matriz_b (list[list]): Matriz del segundo canal.
# Retorno:
#   - list[list]: Matriz resultante de la composición (producto matricial).
#
# Análisis para el Parcial:
# - Multiplicación de matrices: P(C/A) = P(B/A) * P(C/B).
# - Propiedad fundamental: La información mutua NUNCA aumenta en cascada.
#   I(A, C) <= min(I(A,B), I(B,C)).
# - "Data processing inequality".
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Columnas Reducibles (Reducción Suficiente)
# ------------------------------------------------------------------------------
# Parámetros (columnasReducibles):
#   - matriz_del_canal (list[list]): Matriz del canal P(bj/ai).
#   - index1 (int): Índice de la primera columna (j).
#   - index2 (int): Índice de la segunda columna (k).
# Retorno (columnasReducibles):
#   - bool: True si las columnas son proporcionales y por tanto reducibles.
#
# Análisis para el Parcial:
# - Dos salidas 'bj' y 'bk' son reducibles si sus columnas en la matriz son PROPORCIONALES.
# - Condición Teórica: P(ai/bj) = P(ai/bk) para todo 'ai'.
# - Significado: Ambas salidas aportan la MISMA información a posteriori sobre la entrada.
# - Se pueden sumar esas columnas sin perder información mutua: I(A,B) = I(A, B_reducido).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Generación de Matriz de Reducción R
# ------------------------------------------------------------------------------
# Parámetros:
#   - num_columnas_original (int): Número total de columnas de la matriz actual.
#   - index1 (int): Columna a combinar.
#   - index2 (int): Columna a combinar.
# Retorno:
#   - list[list]: Matriz R que, al multiplicarse por la original, reduce las columnas.
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Multiplicación de Matrices
# ------------------------------------------------------------------------------
# Parámetros:
#   - A (list[list]): Primera matriz (mxn).
#   - B (list[list]): Segunda matriz (nxp).
# Retorno:
#   - list[list]: Matriz resultado C (mxp).
#
# Análisis para el Parcial:
# - Necesaria para calcular la reducción (P_reducida = P_original * R).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Reducción Automática del Canal (Reducciones Suficientes)
# ------------------------------------------------------------------------------
# Parámetros:
#   - matrizCanal (list[list]): La matriz original del canal P(bj/ai).
# Retorno:
#   - list[list]: La matriz del canal totalmente reducida.
#
# Análisis para el Parcial:
# - Aplica iterativamente reducciones suficientes.
# - La matriz resultante conserva la misma Información Mutua I(A,B) que la original.
# - Funciona mediante la multiplicación por la matriz de reducción R.
# ------------------------------------------------------------------------------
def ReduccionesSuficientes(matrizCanal):
    cantColumnas = len(matrizCanal[0])
    contReducciones = 999
    matrizRS = [fila[:] for fila in matrizCanal] # Copia segura de la matriz
    
    while (contReducciones != 0):
        contReducciones = 0
        i = 0
        while contReducciones == 0 and i < len(matrizRS[0]):
            j = i + 1
            while contReducciones == 0 and j < len(matrizRS[0]):
                if (columnasReducibles(matrizRS, i, j)):
                    # Se genera la matriz R y se multiplica P * R para reducir
                    matrizRS = matrizCanalCompuesto(matrizRS, generar_matriz_reduccion(len(matrizRS[0]), i, j))
                    contReducciones += 1
                j += 1
            i += 1
    return matrizRS

# ------------------------------------------------------------------------------
# Verificación: Canal Uniforme
# ------------------------------------------------------------------------------
# Parámetros:
#   - matriz_del_canal (list[list]): Matriz del canal.
# Retorno:
#   - bool: True si es uniforme.
#
# Análisis para el Parcial:
# - Definición: Todas las filas son permutaciones de la primera fila.
# - Implicación: La Entropía condicional H(B/ai) es igual para cualquier fila 'i'.
# - Simplifica el cálculo de Capacidad: C = log(M_salidas) - H(Fila_del_canal).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Capacidad del Canal (Casos Especiales)
# ------------------------------------------------------------------------------
# - Limite teorico del canal de transmitir informacion util o valida.
# Parámetros:
#   - matriz_de_transicion (list[list]): Matriz del canal.
# Retorno:
#   - float: Capacidad C en bits (o -1 si no es caso especial).
#
# Análisis para el Parcial:
# - Capacidad C = max(I(A,B)).
# - Esta función usa atajos algebraicos para canales especiales.
# - Determinante: log(Salidas).
# - Sin Ruido: log(Entradas).
# - Uniforme: log(Salidas) - H(fila).
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Capacidad Numérica (Canal Binario General)
# ------------------------------------------------------------------------------
# Parámetros:
#   - matriz_de_transicion (list[list]): Matriz del canal (debe ser 2 entradas).
#   - paso (float): Tamaño del paso para iterar 'w' (ej: 0.01).
# Retorno:
#   - No retorna valor (imprime la capacidad C y la distribución óptima).
#
# Análisis para el Parcial:
# - Si el canal no es uniforme/simétrico, hay que iterar variando P(a1)=w y P(a2)=1-w.
# - Se busca el valor de w que maximice I(A,B).
# ------------------------------------------------------------------------------
def capacidadCanalBinario(matriz_de_transicion, paso):
    if len(matriz_de_transicion) != 2:
        print("Error: Esta función es solo para canales binarios.")
        return

    w = 0.0
    vec = [w, 1.0 - w]
    max_info = calculaInformacionMutua(vec, matriz_de_transicion)
    prob_asociada = w
    w += paso
    
    while w <= 1.0:
        vec = [w, 1.0 - w]
        aux = calculaInformacionMutua(vec, matriz_de_transicion)
        if aux > max_info:
            max_info = aux
            prob_asociada = w
        w += paso
        w = round(w, 10) 

    print(f"Info Mutua Máxima (Capacidad C): {round(max_info, 4)} bits")
    print(f"Se alcanza con P(a1)={round(prob_asociada, 4)}, P(a2)={round(1.0 - prob_asociada, 4)}")

# ------------------------------------------------------------------------------
# Probabilidad de Error (Pe)
# ------------------------------------------------------------------------------
# - Cuantifica qué tan probable es que, al aplicar una "regla de decisión" para adivinar qué se envió, el receptor se equivoque.
# Parámetros:
#   - matriz_de_transicion (list[list]): Matriz del canal P(bj/ai).
#   - probs_a_priori (list): Probabilidades de entrada P(ai).
# Retorno:
#   - float: Probabilidad de error total Pe.
#
# Análisis para el Parcial:
# - Calcula Pe usando el esquema de Decisión Ideal (Máxima Probabilidad A Posteriori).
# - Para cada salida 'bj', se decide que se envió el 'ai' que maximiza P(ai/bj).
# - Pe = Σ P(ai) * P(error | ai).
# - Importante: Usamos deepcopy para no alterar la matriz original durante el cálculo.
# ------------------------------------------------------------------------------
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