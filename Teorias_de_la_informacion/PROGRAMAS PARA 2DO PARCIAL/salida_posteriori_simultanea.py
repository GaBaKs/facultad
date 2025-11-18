import math

#-------------------------------- EJERCICIO 7 ---------------------------------
# Realizar funciones en Python que reciban como parámetros: una lista con las
# probabilidades a priori y la matriz de probabilidades condicionales del canal, y devuelvan:
# a. Una lista con las probabilidades de los símbolos de salida
# b. Una matriz con las probabilidades a posteriori del canal
# c. Una matriz con las probabilidades de los eventos simultáneos
#-------------------------------- EJERCICIO 7 ---------------------------------

def genera_prob_salida(matriz_canal,prob_apriori):
    prob_salida = []
    for i in range(len(matriz_canal[0])): 
        columna = [fila[i] for fila in matriz_canal]
        prob = 0
        for j in range(len(columna)):
            prob+= columna[j]*prob_apriori[j]
        prob_salida.append(prob)
    return prob_salida

def genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal):
    matriz_posteriori = []
    for i in range(len(matriz_canal)): 
        aux = []
        fila = matriz_canal[i]
        for j in range(len(fila)):
            aux.append((fila[j]*prob_apriori[i])/prob_salida[j])
        matriz_posteriori.append(aux)
    return matriz_posteriori

def genera_prob_simultaneas(prob_salida,matriz_posteriori): 
    prob_simultanea = []
    for i in range(len(matriz_posteriori)): 
        prob = []
        for j in range(len(matriz_posteriori)):
            prob.append(matriz_posteriori[i][j]*prob_salida[j])
        prob_simultanea.append(prob)
    return prob_simultanea

prob_apriori = [0.3, 0.3, 0.4]
matriz_canal = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]


prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
print("Probabilidades de salida: ",prob_apriori)
matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
print("Probabilidades a-posteriori: ",matriz_posteriori)
prob_simultaneas = genera_prob_simultaneas(prob_salida,matriz_posteriori)
print("Probabilidades simultaneas: ",prob_simultaneas)

# A partir de la matriz del canal calculo las probabilidades de los simbolos de salida haciendo la sumatoria resutante de 
# recorrer la matriz elemento a elemento y multiplicarlo por la probabilidad de entrada

# Calculo la matriz a posteriori como la resutante de
# recorrer la matriz del canal elemento a elemento y multiplicarlo por la probabilidad de entrada y dividirlo por la probabilidad de salida
# una vez hecho el calculo para un elemento lo añado a mi matriz posteriori

# Calculo la matriz de probabilidades simultaneas como la resutante de
# recorrer la matriz posteriori elemento a elemento y multiplicarlo por la probabilidad de salida
# una vez hecho el calculo para un elemento lo añado a mi matriz posteriori

