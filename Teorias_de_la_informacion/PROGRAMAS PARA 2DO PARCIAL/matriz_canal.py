import math
#-------------------------------- EJERCICIO 2 ---------------------------------
# Codificar una función en Python que reciba como parámetros dos cadenas de caracteres
# que contengan secuencias de entrada y de salida de un canal y retorne la matriz que
# representa dicho canal
#-------------------------------- EJERCICIO 2 ---------------------------------

def matriz_canal(entrada, salida):
    entrada = list(entrada)
    salida = list(salida)
    aux = []
    dimension = len(entrada) # len(entrada) = len(salida)
    simbolos = []
    for i in range(dimension):
        if not entrada[i] in simbolos:
            simbolos.append(entrada[i])
            aux.append([0,0]) #Solucion supuesta para una salida binaria
        
        if salida[i] == '1':
            aux[simbolos.index(entrada[i])][1]+=1
        else: #Es un 0
            aux[simbolos.index(entrada[i])][0]+=1

    matriz = []
    prob_apriori = []
    for i in range(len(simbolos)):
        cant = entrada.count(simbolos[i])
        prob_apriori.append(cant/len(entrada))
        matriz.append([aux[i][0]/cant,aux[i][1]/cant]) 

    return matriz, prob_apriori, simbolos

entrada = "00001111"
salida = "00001111"

matriz, prob_apriori, filas = matriz_canal(entrada,salida)
print("Matriz del canal: ",matriz)
print("Cada fila de la matriz representa: ",filas)
print("Las probabilidades a-priori son las siguientes: ",prob_apriori)

# Arma la matriz del canal calculando las probabilidades de que con x entrada haya y salida
# A partir de 2 mensajes de igual longitud compruebo simbolo por simbolo si coinciden con la salida o no
# y calculo su probabilidad una vez analizado todo el mensaje
