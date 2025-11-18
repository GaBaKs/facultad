[]

import math

# CODIFICACION DE FUENTES DE INFORMARCION - UNIDAD 4

"""
-------- GENERALES QUE NECESITO -----------------------------------------------------------------------------------------------------------
"""
# Devuelve alfabeto y sus probabilidades
def  AlfabetoProbabilidades(mensaje):
    cuentas=[]
    simbolos=[]

    for car in mensaje:
        if car in simbolos:
            cuentas[simbolos.index(car)]+=1
        else:
            simbolos.append(car)
            cuentas.append(1)
    
    n=len(mensaje)
    prob = [c/len(mensaje) for c in cuentas]
    return prob,simbolos

# Alfabeto codigo a partir de palabras codigo
def AlfabetoCodigo (codigo):
    alf = set()

    for palabra in codigo:
        for car in palabra:
            if car not in alf:
                alf.add(car)
    
    return alf

# Entropia en base r
def Entropia(probs,codigo):
    h=0
    r = len(AlfabetoCodigo(codigo)) 
    for p in probs:
        h += p * math.log(1/p,r)
    return h

# Longitudes de las palabras codigo
def LongitudesPalabras (codigo):
    return [len(palabra) for palabra in codigo]

# Longitud media
def LongitudMedia (probs,codigo):
    L = 0
    long = LongitudesPalabras(codigo)

    for i in range(len(codigo)):
        L += probs[i] * long[i]

    return L

# Extension de orden N (devuelve lista)
def Extension (alfabeto,n):
    if n == 0:
        return [""]
    else:
        combAnt = Extension(alfabeto,n-1)
        result = [] #inicializo alfabeto nuevo
        for simbolo in alfabeto: #por cada simbolo en el alfabeto
            for comb in combAnt: 
                result.append(comb+simbolo) #concateno las combinaciones hechas con el nuevo simbolo
        return result
    
# Probabilidades de la extension orden N
def ProbabilidadesN (alfabeto,alfabetoN,probabilidades): #probs
    probN = []

    for cadena in alfabetoN:
        prob = 1
        for simbolo in cadena:
            prob *= probabilidades[alfabeto.index(simbolo)]
        probN.append(prob)
    return probN

"""
-------------------------------------------------------------------------------------------------------------------------
"""

# ---------------------------------------------- PRIMER TEOREMA DE SHANNON ---------------------------------------------- #

"""
----- USA - AlfabetoCodigo, Entropia, LongitudesPalabras, LongitudMedia, Extension, ProbabilidadesN------

----- RECIBE - lista de probabilidades, palabras codigo, numero de la extension

si no me dan n --> n = int(input("Ingrese la extension\n"))
"""

def VerificaShannon (probs,codigo,n):
    cod = codigo # solo para que quede acorde si n==1
    p = probs
    h = Entropia(p,cod)
    print(f"H: {h: .2f}")

    # si la extension no es 1
    if (n != 1):
        alfabeto = ["1","2","3"] # CAMBIARLO DE ACUERDO A CANT DE SIMBOLOS EN LA FUENTE ORIGINAL PONER ALFENTRADA O ALGO
        alfabetoN = Extension(alfabeto,n)
        
        cod = Extension(codigo,n) # si no me dan el codigo de la extension
        # cod = [valores] # si ya me dan el codigo de la extension

        p = ProbabilidadesN(alfabeto,alfabetoN,probs)

    Ln = LongitudMedia(p,cod)
    print(f"Ln: {Ln: .2f}")
    LnN = Ln/ n
    Shannon = h <= LnN and LnN < (h + 1/n)

    if (Shannon):
        print("Cumple")
    else:
        print("No cumple")

    #return Shannon

# --------------------------------------------------------------------------------------------------------------------- #
    


# ---------------------------------------------- ALGORITMO DE HUFFMAN ---------------------------------------------- #

"""
---------- SOLO TENGO QUE MANDAR LISTA DE PROBABILIDADES-----------

---- CAPAZ USA - AlfabetoProbabilidades, si me dan un mensaje en vez de directamente las probabilidades

"""

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

# ------------------------------------------------------------------------------------------------------------------ #



# ---------------------------------------------- ALGORITMO DE SHANNON-FANO ---------------------------------------------- #

"""
---- USA - Longitud Media (CAPAZ, EN SI NO LA NECESITA PARA HACER EL CODIGO, PERO ME SUELEN PEDIR QUE LA DE)
---- CAPAZ USA - AlfabetoProbabilidades, si me dan un mensaje en vez de directamente las probabilidades

---- RECIBE - lista de probabilidades
"""

def MuestraShannonFano(probs): # FUNCION QUE LLAMO
    items = [[p, i] for i, p in enumerate(probs)] # lista de listas, conjuntos probabilidad - indice
    items.sort(reverse=True, key=lambda x: x[0]) # ordena la lista decrecientemente por el primer elemento (probs)
    
    codigo = [""] * len(probs) # inicializo para despues concatenar los simbolos de cada codigo
    ShannonFano(items, codigo) # lista de indices (inicialmente con todos)

    print("Símbolo | Prob | Código Shannon-Fano")
    for i, c in enumerate(codigo):
       print(f"   {i}     | {probs[i]: .4f}  |  {c}")

    L = LongitudMedia(codigo,probs)
    print(f"L Shannon-Fano: {L: .4f}")

    #return codigo # si hace falta devolver una lista con los strings


def ShannonFano(items, codigo):

    if len(items) > 1: # si hay mas de un simbolo
        totalProbs = sum(elem[0] for elem in items) # sumo probabilidades del grupo

        acum = 0 
        mejorDif = float("inf")
        corte = 0  

        # busco el punto de corte más equilibrado
        for i in range(1, len(items)):  # empiezo en 1 para evitar grupo vacío
            acum += items[i - 1][0] # voy acumulando las probabilidades
            dif = abs(acum - (totalProbs - acum)) # diferencia entre las probabilidades de ambos grupos
            if dif < mejorDif: # voy guardando la menor diferencia (punto donde deberia cortar, para que tengan suma de probs lo mas similares posibles)
                mejorDif = dif
                corte = i # guardo ese indice (mi punto de corte)

        # armo los codigos concatenando 0 hasta el punto de corte, y 1 en el resto de los simbolos
        for p, i in items[:corte]: # uso p,i porque son los elementos que hay en items, pero solo me interesa el i
            codigo[i] += "0"
        for p, i in items[corte:]:
            codigo[i] += "1"

        # llamo con nuevos subgrupos
        subA = sorted(items[:corte], reverse=True, key=lambda x: x[0])
        subB = sorted(items[corte:], reverse=True, key=lambda x: x[0])

        ShannonFano(subA, codigo)
        ShannonFano(subB, codigo)

# ------------------------------------------------------------------------------------------------------------------ #



# ---------------------------------------------- RENDIMIENTO Y REDUNDANCIA ---------------------------------------------- #

"""
---- USAN - Entropia, Longitud media

---- RECIBEN - lista de probabilidades, palabras codigo
"""

# Rendimiento o Eficiencia de un codigo
def Rendimiento(probs,codigo):
    h = Entropia(probs,codigo)
    L = LongitudMedia(codigo,probs)
    print(f"n: {Rendimiento(h,L):.4f}")
    #return h / L

# Redundancia de un codigo
def Redundancia(probs, codigo):
    h = Entropia(probs,codigo)
    L = LongitudMedia(codigo,probs)
    
    print(f"R: {Redundancia(h,L):.4f}")
    #return (L-h)/L

# ------------------------------------------------------------------------------------------------------------------ #



# ---------------------------------------------- DECODIFICACION BASICA DE MENSAJE ---------------------------------------------- #

"""
---- RECIBE - mensaje codificado, alfabeto codigo, alfabeto fuente
"""

def Decodificacion (codificacion,alfCodigo,alfabeto):
    decod = ""
    
    pal = ""
    i = 0
    while (i < len(codificacion)): 
        pal += codificacion[i] # uno los bits

        if(pal in alfCodigo): # cuando coincide con una de las palabras codigo
            decod += alfabeto[alfCodigo.index(pal)] + " " # agrego el simbolo correspondiente a mi decodificacion
            pal = "" # reinicio la palabra

        i += 1

    print("Mensaje decodificado: ", decod)

    # return decod

# ------------------------------------------------------------------------------------------------------------------ #



# ---------------------------------------------- CODIFICACION Y DECODIFICACION BYTEARRAY ---------------------------------------------- #

# Codifica mensaje y lo devuelve en un bytearray-----------------------------------------
"""
---- RECIBE - Alfabeto fuente, alfabeto codigo, mensaje sin codificar
"""

def CodificacionBytearray (alfabeto,alfCodigo,mensaje):

    codificacion = ""

    for simb in mensaje:
        codificacion += alfCodigo[alfabeto.index(simb)]

    print("Cadena codificada: ", codificacion)

    byteA = bytearray()

    # relleno con ceros para despues poder dividir en bytes
    while (len(codificacion) % 8 !=0):
        codificacion += '0'

    # transformo a bytearray
    for i in range(0,len(codificacion),8):
        byte = codificacion[i:i+8] # agarro un byte
        valorByte = int(byte,2) # lo hago numero entero
        byteA.append(valorByte) # lo agrego al bytearray

    print("Bytearray: ",byteA)

    return byteA


# Decodifica un bytearray y devuelve el mensaje ---------------------------------------
"""
---- RECIBE - Alfabeto fuente, alfabeto codigo, codigo en bytearray
"""

def DecodificacionByteArray (alfabeto, alfCodigo,byteA):
    
    # sin esta linea y mandando codigo en vez de byteA, es decodificacion normal
    codigo = ''.join(format(byte,'08b') for byte in byteA) # une los bytes nuevamente a una cadena en binario
    print(codigo)

    decod = ""    
    pal = ""
    i = 0
    while (i < len(codigo)): 
        pal += codigo[i] # uno los bits

        if(pal in alfCodigo): # cuando coincide con una de las palabras codigo
            decod += alfabeto[alfCodigo.index(pal)] + " " # agrego el simbolo correspondiente a mi decodificacion
            pal = "" # reinicio la palabra

        i += 1

    #return decod

    print("Mensaje decodificado: ", decod)

# ------------------------------------------------------------------------------------------------------------------ #



# ---------------------------------------------- TASA DE COMPRESION ---------------------------------------------- #

"""
---- RECIBE - mensaje sin codificar, codificacion en bytearray
"""


def TasaDeCompresion (mensaje,codigoByte):

    tamMensaje = len(mensaje.encode('utf-8')) # bytes del mensaje original
    tamCodif = len(codigoByte)

    tasa = 0
    if (tamCodif != 0):
        tasa = tamMensaje / tamCodif
        # porc = (1 - tamCodif / tamMensaje) * 100
    
    print(f"Tasa de Compresion: {tasa: .4f}")

    #return tasa

# ------------------------------------------------------------------------------------------------------------------ #



# ---------------------------------------------- ALGORITMO RLC ---------------------------------------------- #

"""
---- RECIBE - mensaje sin codificar
"""

def RLC (mensaje):

    codif = bytearray()
    cont = 1

    for i in range(1,len(mensaje)): # por cada simbolo del mensaje, empezando por el segundo

        if (mensaje[i] == mensaje[i - 1]): # si es igual al anterior
            cont += 1 # sumo apariciones consecutivas

            if (cont == 255): # limito a 255 porque es lo que puede guardar un byte
                codif.append(ord(mensaje[i - 1])) # convierto al caracter en corresp numero de ASCII
                codif.append(cont) # guardo consecutivamente su contador
                cont = 0 # reinicio, considerando que aun no avance (si el simbolo sigue siendo el mismo, se va a sumar al volver a pasar el for)
        else: # si cambio de simbolo
            codif.append(ord(mensaje[i - 1])) # guardo los registros anteriores
            codif.append(cont)
            cont = 1 # reinicio
    
    codif.append(ord(mensaje[-1])) # guardo el ultimo conteo
    codif.append(cont)

    print("Mensaje codificado: ", codif)

    # return codif

# ------------------------------------------------------------------------------------------------------------------ #




# ---------------------------------------------- DISTANCIA DE HAMMING ---------------------------------------------- #

"""
---- RECIBE - Alfabeto codigo
"""

def DistanciaDeHamming (alfCodigo):

    distH = 999
    i = 0

    for pal in alfCodigo:
        for pal2 in alfCodigo:
            if (pal != pal2):
                dist = 0
                for i in range(len(pal)): # cuenta distancia de Hamming entre ambas palabras
                    if (pal[i] != pal2[i]):
                        dist += 1
                if (dist < distH):
                    distH = dist

    print("Distancia de Hamming del codigo: ",distH)

    return distH

# ------------------------------------------------------------------------------------------------------------------ #




# ---------------------------------------------- DISTANCIA DE HAMMING ---------------------------------------------- #

"""
---- USA - DistanciaDeHamming

---- RECIBE - Alfabeto codigo
"""

# Cant errores que se pueden detectar, cant errores que se pueden corregir
def Errores (alfCodigo):

    distH = DistanciaDeHamming(alfCodigo)

    detectar = distH - 1
    corregir = (distH - 1) / 2

    print("Errores que se pueden detectar: ", detectar)
    print("Errores que se pueden corregir: ", corregir)

    #return detectar, corregir

# ------------------------------------------------------------------------------------------------------------------ #




# ---------------------------------------------- PARIDADES ---------------------------------------------- #

"""
------------ CODIFICACION - Recibir cadena, devolver matriz de paridades --------------

Transforma cadena de caracteres en su matriz binaria con bits de paridades
y despues transforma la matriz a un byterray - LO PUEDO SACAR Y QUEDARME SOLO CON LA MATRIZ

---- USA - Copias y pegar tal cual esta aca, porque usa unicamente eso

---- RECIBE - Cadena de caracteres

"""

def ParidadVertical (mat,matPar): # arma matPar igual a mat pero con columna extra de paridad vertical

    for fila in mat:
        cantUnos = fila.count('1') # cuento cantidad de unos de la fila
        paridad = '1' if (cantUnos % 2) else '0' # bit de paridad 1 si la cantidad de unos es impar, sino 0
        matPar.append(fila + paridad) # agrego bit de paridad al final de cada fila
    
    for fila in matPar:
        print(fila)

    #return matPar


def ParidadLongitudinal (matPar): # agrega fila a matPar

    cantCol = len(matPar[0])
    parL = ""

    for col in range(cantCol):
        cantUnos = sum(fila[col] == '1' for fila in matPar) # cuento los unos en la columna
        paridad = '1' if (cantUnos % 2) else '0' # bit de paridad
        parL += paridad # voy armando la fila

    matPar.insert(0,parL) # agrego fila de paridad vertical arriba del todo (por convencion)

    #return matPar


def ParidadCruzada(matPar):
    colV = [fila[-1] for fila in matPar]  # ultima columna (parV)
    filaL = matPar[0] # primera fila (parL)

    paridad = '1' if ((colV.count('1') + filaL.count('1')) % 2) else '0' # calculo bit de paridad cruzada

    filaUlt = list(matPar[-1]) # convierto fila a lista de caracteres (para poder modificarla)
    filaUlt[-1] = paridad # le doy el bit que corresponde

    matPar[-1] = ''.join(filaUlt) # agrego bit de paridad cruzada en el ultimo elemento de la matriz

    # return matPar

# Pasa cadena de texto a cadena de numeros binarios
def TextoABits (cadena):
    return [format(ord(car), '08b') for car in cadena] # transforma cada caracter de la cadena a binario


def CodificaCadenaABytearray (cadena): # cadena si me dan una sola cadena, mat si me dan ya la matriz (sin paridades)

    matPar = [] 

    #SACAR SENTENCIA SI YA ME DAN LA MATRIZ
    mat = TextoABits(cadena) # la transformo en cadena de bits

    ParidadVertical(mat,matPar) # agrego a la matriz la paridad vertical
    ParidadLongitudinal(matPar) # agrego a la matriz la paridad longitudinal
    ParidadCruzada(matPar) # agrego a la matriz la paridad cruzada


    # SI QUIEREN MATRIZ DE PARIDAD
    
    # MUESTRA MATRIZ, VER CON QUE LA LLAMO
    # return matPar

    # SI QUIEREN BYTEARRAY
    #byteA = bytearray(int(fila,2) for fila in matPar) # transformo a bytearray
    #print("Bytearray: ",byteA)
    # return byteA


"""
------------ DECODIFICACION --------------

Vefifica si se puede transformar la matriz de paridades (o bytearray) a la cadena correspondiente
Si hay muchos errores, lo dice (no se podria transformar)

---- USA - Copias y pegar tal cual esta aca, porque usa unicamente eso

---- RECIBE - Matriz de paridades o bytearray (SI ES BYTEARRAY, CAMBIAR PARAMETRO Y SACARLE # A matPar = ...)

"""

def VerificaParidades (matPar): # verifica si las paridades dieron algun error

    cantFil = len(matPar) 
    cantCol = len(matPar[0])
    errorFil = errorCol = -1 # inicializo errores
    r = 0 # si hay demasiados errores, devuelvo 0

    for i in range(1,cantFil):
        cantUnos = matPar[i].count('1') # cuento unos de cada fila
        if (cantUnos % 2 != 0): # si la cantidad no es par, hay error
            errorFil = i  # guardo indice de donde esta el error
    
    for j in range(cantCol): # idem filas
        cantUnos = sum(matPar[i][j] == '1' for i in range(cantFil))
        if (cantUnos % 2 != 0):
            errorCol = j

    if (errorFil == -1 and errorCol == -1): # si no hay errores, devuelvo 1
        r = 1
    else:
        if (errorFil != -1 and errorCol != -1): # si hay un error, lo corrijo y devuelvo 2
            r = 2
            fila = list(matPar[errorFil])
            fila[errorCol] = '1' if fila[errorCol] == '0' else '0' # correccion del error
            matPar[errorFil] = ''.join(fila)

    return r    

def DecodificaCadena (matPar): # (matPar) si me dan matriz de paridades, (byteA) si me dan bytearray

    # SACARLO SI YA ME DAN LA MATRIZ DE PARIDADES
    #matPar = [format(byte,'09b') for byte in byteA]

    cadena = ""
    verif = VerificaParidades(matPar)

    if (verif): # 0 si tiene muchos errores, 1 si no hubo errores, 2 si tuvo un error y se lo corrigio
        mat = matPar[1:] # saco fila paridad longitudinal

        if (verif == 2):
            print("En el codigo se encontro y corrigio un error simple")

        for fila in mat:
            bitsDatos = fila[:-1] # saco bit de paridad vertical
            cadena += chr(int(bitsDatos,2)) # tranformo la fila en un entero, y busco el caracter Ascii al que hace referencia, voy concatenando para formar la palabra
    else:
        print("El codigo tiene demasiados errores")

    print("Cadena: ", cadena)
    
    #return cadena

# ------------------------------------------------------------------------------------------------------------------ #




# ---------------------------------------------- EXTRAS ---------------------------------------------- #

"""
ByteCarParidad - pasa caracter en num ascii (7 bits) y en el bit 8 guarda el bit de paridad correspondiente a los otros 7 bits

VerificaByte - recibe el byte de la funcion anterior y verifica que la paridad sea correcta

---- RECIBE - Caracter
"""

def ByteCarParidad (car): 

    carASCII = ord(car) # paso el caracter a su num ascii
    cantUnos = bin(carASCII).count("1") # paso el numero a binario y cuento los unos

    paridad = 1 if (cantUnos % 2) else 0 # si la cantidad de unos es impar, la paridad es 1, sino es 0

    byte = (carASCII << 1) | paridad

    print("Byte caracter y paridad: ", byte)

    return byte

def VerificaByte (byte):

    paridad = byte & 1 # bit menos significativo
    carASCII = byte >> 1 # saco bit de paridad

    cantUnos = bin(carASCII).count("1")
    paridadVerif = 1 if (cantUnos % 2) else 0 # deberia ser 0 si hay paridad par

    if (paridad == paridadVerif):
        print("El byte es correcto")
    else:
        print("Error detectado en el byte")

# ------------------------------------------------------------------------------------------------------------------ #