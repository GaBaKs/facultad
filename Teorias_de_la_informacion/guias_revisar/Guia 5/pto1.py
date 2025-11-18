[]
# canal 1
# entrada = "1101011001101010010101010100011111"
# salida = "1001111111100011101101010111110110"

# canal 2
# entrada = "110101100110101100110101100111110011"
# salida = "110021102110022010220121122100112011"

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

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

# Muestra cada simbolo enlistado con su probabilidad
def MuestraSimbolos (simbolos,prob):
    for s,p in zip(simbolos,prob):
        print(f"{s}: {p: .4f}")

# Obtiene y muestra la matriz del canal a partir de las cadenas de entrada y salida
def MatrizDelCanal(entrada,salida):

    probsAPriori,alfEnt = AlfabetoProbabilidades(entrada)
    probsSal,alfSal = AlfabetoProbabilidades(salida)
    print("Probabilidades a priori:")
    MuestraSimbolos(alfEnt,probsAPriori)

    mat = [ [0] * len(alfSal) for _ in range(len(alfEnt)) ] # inicializo matriz

    # veo el simbolo de entrada y su correspondiente simbolo de salida
    for simbEnt, simbSal in zip(entrada,salida): # zip junta los elem de ambas cadenas por posicion
        mat[alfEnt.index(simbEnt)][alfSal.index(simbSal)] += 1 # en mat(i,j) sumo cant veces que entro ai y salio bj

    for i in range(len(mat)):
        cantAi= sum(mat[i]) # cuento cant apariciones del simbolo de entrada (ai)
        if cantAi != 0:
            mat[i] = [elem / cantAi for elem in mat[i]] # divido toda la fila por la cantidad de apariciones, para obtener prob condicional
        
    # Muestra matriz segun par (i,j)
    for i in range(len(mat)): # i es el índice de la fila
        for j in range(len(mat[i])): # j es el índice de la columna
            print(f"  ({alfEnt[i]}, {alfSal[j]}) = {mat[i][j]: .4f}", end=" ")
        print() # salto de línea para pasar a la siguiente fila

    #return mat


MatrizDelCanal(entrada,salida)

