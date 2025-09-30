import math
import random

#Cantidad de Informacion de Una Lista de Probabilidades
#Pre: Fuentes Nulas
#@param lista: Lista de probabilidades
#@return: Lista con la cantidad de informacion en bits de los simbolos
def infoEnBitsDeSimbolos(lista):
    cant_info = []
    for probabilidad in lista:
        if probabilidad != 0:
            cant_info.append(probabilidad*math.log2(1/probabilidad))
        else: 
            cant_info.append(0)
    return cant_info

#Entropia de Una Lista de Probabilidades
#Pre: Fuentes Nulas
#@param lista: Lista de Cantidad de Informacion
#@return: Entropia de la fuente en bits
def entropiaDeFuenteNula(cant_info):
    entropia = 0.0
    for probabilidad in cant_info:
        if probabilidad !=0: 
            entropia += probabilidad*math.log2(1/probabilidad)
    return entropia

#Genera el alfabeto y las probabilidades de un mensaje
#Pre: palabra es una cadena de caracteres no vacia
#@param palabra: cadena de caracteres
#@return: lista alfabeto y lista de probabilidades
def generaAlfabetoProbabilidades(palabra):
    alfabeto = []
    apariciones = []
    for letra in palabra:
        if letra not in alfabeto:
            alfabeto.append(letra)
            apariciones.append(1)
        else:
            apariciones[alfabeto.index(letra)] += 1
    apariciones = [a / len(palabra) for a in apariciones]
    return alfabeto, apariciones

#Genera un numero aleatorio entre 0 y 1
#@param probabilidades: Lista de probabilidades
#@return: Indice de la lista de probabilidades (Coincide con el alfabeto)
def numAleatorio(probabilidades):
    aux = 0
    acum = 0
    aleatorio = random.random()
    while(acum < aleatorio):
        acum += probabilidades[aux]
        aux += 1
    return aux-1

#Genera una palabra de longitud n a partir de un alfabeto y sus probabilidades
#@param alfabeto: Lista de simbolos
#@param probabilidades: Lista de probabilidades
#@param n: Longitud de la palabra a generar
#@return: Palabra generada
def simulaFuente(alfabeto, probabilidades, n):
    i = 0 
    indice = 0
    palabra = ""
    while(i<n):
        indice = numAleatorio(alfabeto, probabilidades)
        palabra = palabra + alfabeto[indice]
        i += 1
    return palabra

#Entropia de una fuente binaria
#@param w: Probabilidad del simbolo 1
#@return: Entropia de una fuente binaria en bits
def entropiaFuenteBinaria(w):
    fuente = [w, 1-w]
    cant_info = infoEnBitsDeSimbolos(fuente)
    aux = []
    for info in cant_info:
        aux.append(info * fuente[cant_info.index(info)])
    return sum(aux)

#Extension de una fuente
#@param alfabeto: Lista de simbolos
#@param dist_prob: Lista de probabilidades
#@param n: Longitud de las palabras a generar
#@param nueva_alfabeto: Lista vacia para guardar las palabras generadas
#@param nueva_dist_prob: Lista vacia para guardar las probabilidades de las palabras generadas
#@param i: Variable de control (iniciar en n-1)
#@return: nueva_alfabeto y nueva_dist_prob
def extensionN(alfabeto, dist_prob , n, nueva_alfabeto, nueva_dist_prob, i):
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

#Genera la matriz de transicion de una cadena
#@param cadena: Cadena de caracteres
#@return: Alfabeto y Matriz de probabilidades
def cadenaAMatriz(cadena):
    alfabeto = []
    for letra in cadena:
        if letra not in alfabeto:
            alfabeto.append(letra)
        largo = len(alfabeto)
    alfabeto.sort()
    matriz = [[0 for _ in range(largo)] for _ in range(largo)]
    for i in range(len(cadena) - 1):
        fila = alfabeto.index(cadena[i])
        col = alfabeto.index(cadena[i+1])
        matriz[fila][col] += 1
    matriz_prob = [[0 for _ in range(largo)] for _ in range(largo)]
    for j in range(largo):
        suma_col = sum(matriz[i][j] for i in range(largo))
        if suma_col > 0:
            for i in range(largo):
                matriz_prob[i][j] = round(matriz[i][j] / suma_col, 2)
    return alfabeto, matriz_prob

#Simula una fuente de Markov a traves de su Matriz de Probabilidades
#@param alfabeto: Lista de simbolos
#@param matriz_prob: Matriz de probabilidades
#@param n: Longitud de la palabra a generar
#@return: Palabra generada
def simulaFuenteMarkov(alfabeto, matriz_prob, n):
    palabra = ""
    largo = len(alfabeto)
    indice = int(random() * largo)
    palabra += alfabeto[indice]
    for _ in range(n - 1):
        r = random()
        acum = 0
        col = indice
        for i in range(largo):
            acum += matriz_prob[i][col]
            if r <= acum:
                indice = i
                break
        palabra += alfabeto[indice]
    return palabra


#Calculo del vector estacionario de una fuente markoviana
#@param matriz: Matriz de transicion de la fuente
#@return vecEstacionario: Vector Estacionario de la fuente.
def calculaVecEstacionario(mat):
    tol_max = 1e-9
    vec_estacionario = [float(1/len(mat)) for _ in range(len(mat))] #Se empieza por una situacion de incertidumbre total
    max_dif=1.0
    max_dif_ant=1.01
    flag=False
    while max_dif>tol_max and not flag: #Se contemplan las oscilaciones
        vec_aux = [0.0 for _ in range(len(mat))]
        j=0
        for j in range(len(mat)): #Para cada fila de la matriz
            for k in range(len(mat)): #Para cada columna de la matriz
                vec_aux[j] += mat[j][k]*vec_estacionario[k]
        max_dif = max(abs(vec_aux[i] - vec_estacionario[i]) for i in range(len(mat)))
        if(max_dif>max_dif_ant):
            flag=True
        else:
            max_dif_ant=max_dif
            vec_estacionario=vec_aux.copy()
    return vec_estacionario

#Entropia de una Fuente de Markov
#Pre: Fuente Markoviana
#@param: matriz: Matriz de Transicion
#@return sum(vecEstacionario): Entropia de la fuente
def entropiaMarkoviana(matriz):
    vecEstacionario = calculaVecEstacionario(matriz)
    vec_aux = [0.0 for _ in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]!=0:
                vec_aux[j]+= matriz[i][j]*math.log2(1/matriz[i][j])
    for n in range(len(vecEstacionario)):
        vecEstacionario[n]=vecEstacionario[n] * vec_aux[n]
    return round(sum(vecEstacionario),2)

#Detecta el tipo de fuente a partir de su Matriz de Probabilidades
#@param mat: Matriz de probabilidades
#@param tol_max: Tolerancia maxima para considerar que dos valores son iguales
#@return: Imprime el tipo de fuente y el vector estacionario si es ergodica
def detectaTipoFuente(mat, tol_max):
    i=0
    flag2=False
    elemento = 0.0
    for i in range(len(mat)):
        for j in range(len(mat)):
            for elemento in mat[i]:
                 if abs(mat[i][j]-elemento)>tol_max:
                    flag2=True
                    break
            if(flag2):
                break
        if(flag2):
            break
    if (flag2):
        print("Fuente No Nula")
        vec_estacionario = [float(1/len(mat)) for _ in range(len(mat))] #Se empieza por una situacion de incertidumbre total
        max_dif=1.0
        max_dif_ant=1.01
        flag=False
        while max_dif>tol_max and not flag: #Se contemplan las oscilaciones
            vec_aux = [0.0 for _ in range(len(mat))]
            j=0
            for j in range(len(mat)): #Para cada fila de la matriz
                for k in range(len(mat)): #Para cada columna de la matriz
                    vec_aux[j] += mat[j][k]*vec_estacionario[k]
            max_dif = max(abs(vec_aux[i] - vec_estacionario[i]) for i in range(len(mat)))
            if(max_dif>max_dif_ant):
                flag=True
            else:
                max_dif_ant=max_dif
                vec_estacionario=vec_aux.copy()
        if(flag):
            print("Fuente No Ergodica")
        else:
            print("Fuente Ergodica")
            for elem in vec_aux:
                vec_aux[vec_aux.index(elem)] = round(elem,2)
            print("Vector estacionario: ", vec_aux)
    else:
        print("Fuente Nula")

#Detecta si un codigo es no singular
#@param lista: Lista de palabras codigos
#@return: True si es no singular, False en caso contrario
def codigoNoSingular(lista):
    for codigo in lista:
        lista.count(codigo)
        if lista.count(codigo) > 1:
            return False
    return True

##Detecta si un codigo es instantaneo
#@param lista: Lista de palabras codigo
#@return: True si es instantaneo, False en caso contrario
def codigoInstantaneo(lista):
    aux = lista[0]
    flag=True
    for codigo in lista:
        for otro_codigo in lista:
            if codigo != otro_codigo and otro_codigo.startswith(codigo):
                flag=False
    return flag
        
#Detecta si un codigo es univoco
#@param lista: Lista de palabras codigo
#@return: True si es univoco, False en caso contrario
def codigoUnivoco(lista):
    subconjunto = []
    subconjunto_anterior = []
    flag2=False
    for codigo in lista:
        for otro_codigo in lista:
            if codigo != otro_codigo and otro_codigo.startswith(codigo):
                resto=otro_codigo[len(codigo):]
                subconjunto.append(resto)
                if resto == "":
                    flag2=True
    while  set(subconjunto) != set(subconjunto_anterior) and not flag2:
        subconjunto_anterior = subconjunto.copy()
        for codigo in subconjunto:
            for otro_codigo in lista:
                if otro_codigo.startswith(codigo):
                    resto = otro_codigo[len(codigo):]
                    if resto not in subconjunto:
                        subconjunto.append(resto)
                    if resto == "":
                        flag2=True
    return not flag2

#Genera una cadena codificada a partir de un alfabeto de codigo
#@param alfabeto_codigo: Lista de palabras codigo
#@return: Cadena con el alfabeto generado
def generaCadenaCodificada(alfabeto_codigo):
    alf=""
    for palabra in alfabeto_codigo:
        for letra in palabra:
            if not letra in alf:
                alf+=letra
    return alf

#Calcula la base r del alfabeto de codigo
#@param alfabeto: Lista de palabras codigo
#@return: Base r del alfabeto
def calculaBaseR(alfabeto):
    return len(generaCadenaCodificada(alfabeto))

#Calcula la longitud de las palabras codigo
#@param codigos: Lista de palabras codigo
#@return: Lista con las longitudes de las palabras codigo
def longitudPalabrasCodigo(codigos):
    longitudes = []
    for codigo in codigos:
        longitudes.append(len(codigo))
    return longitudes


#Calcula la suma de la inecuacion de Kraft
#@param alfabeto: Lista de palabras codigo
#@return: Suma de la inecuacion de Kraft (debe ser <= 1 para que el codigo sea instantaneo)
def inecuacionDeKraft(alfabeto):
    acum = 0
    r = calculaBaseR(alfabeto)
    long = longitudPalabrasCodigo(alfabeto)
    for tam in long:
        acum += r**-tam
    if acum <=1:
        print("Cumple con la inecuacion: ",round(acum,4),"<= 1")
    else:
        print("No cumple con la inecuacion: ",round(acum,4),"> 1")

#Calcula la entropia de una fuente en base r
#@param alfabeto: Lista de palabras codigo
#@param probabilidades: Lista de probabilidades de las palabras codigo
#@return: Entropia de la fuente en base r
def entropiaBaseR(alfabeto, probabilidades):
    acum = 0
    r = calculaBaseR(alfabeto)
    for p in probabilidades:
        if p!=0:
            acum += p * math.log(1/p, r)
    return acum

#Calcula la longitud media de un alfabeto codigo
#@param alfabeto: Lista de palabras codigo
#@param probabilidades: Lista de probabilidades de las palabras codigo
#@return: Longitud media del alfabeto codigo
def longitudMedia(alfabeto, probabilidades):
    acum = 0
    for i in range(len(alfabeto)):
        acum += probabilidades[i] * len(alfabeto[i])
    return acum

#Detecta si un codigo es compacto
#@param codigo: Lista de palabras codigo
#@param probabilidades: Lista de probabilidades de las palabras codigo
#@return: True si es compacto, False en caso contrario
def codigoCompacto(codigo,probabilidades):
    aux = []
    r = calculaBaseR(codigo)
    for palabra in codigo:
        aux.append(math.ceil(math.log(1/probabilidades[codigo.index(palabra)],r))) #Calcula la informacion de cada palabra codigo en base r
    for i in range(len(codigo)):
        if aux[i] < len(codigo[i]): #Si la cantidad de informacion es distinta de la longitud de la palabra codigo sale
            return False 
    return True
