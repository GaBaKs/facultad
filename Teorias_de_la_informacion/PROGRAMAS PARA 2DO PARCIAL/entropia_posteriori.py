import math

def genera_entropia_apriori(prob_apriori):
    r = 2 #Por ser en binits
    entropia = 0
    for p in prob_apriori:
        entropia+= p*math.log(1/p,r)
    return entropia

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
            if prob_salida[j] != 0:
                aux.append((fila[j]*prob_apriori[i])/prob_salida[j])
        matriz_posteriori.append(aux)
    return matriz_posteriori

def genera_entropia_posteriori(prob_apriori,matriz_canal):
    prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
    matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
    entropia = []
    r = 2 #Por ser en binits
    for i in range(len(matriz_posteriori[0])):
        columna = [fila[i] for fila in matriz_posteriori]
        aux = 0
        for x in columna:
            if x != 0:
                aux+= x*math.log(1/x,r)
        entropia.append(aux)
    return entropia

def genera_prob_simultaneas(prob_salida,matriz_posteriori): 
    prob_simultanea = []
    for i in range(len(matriz_posteriori)): 
        prob = []
        fila = matriz_posteriori[i]
        for j in range(len(fila)):
            prob.append(fila[j]*prob_salida[j])
        prob_simultanea.append(prob)
    return prob_simultanea

# Parece que anda

prob_apriori = [2/5, 3/5]
matriz_canal = [
    [3/5, 2/5],
    [1/3, 2/3]
]

entropia_apriori = genera_entropia_apriori(prob_apriori)
print("Entropia a-priori: ",entropia_apriori)

entropia_posteriori = genera_entropia_posteriori(prob_apriori,matriz_canal)
print("Entropias a-posteriori: ",entropia_posteriori)

prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
prob_simultaneas = genera_prob_simultaneas(prob_salida,matriz_posteriori)

print("La matriz de probabilidades condicionales es: ",prob_simultaneas)

# Calculo la entropia a priori como la entropia normal, haciendo la sumatoria de la multiplicacion 
# de la cantidad de informacion por la probabilidad de entrada de cada simbolo

# Calculo la entropia a posteriori, haciendo la sumatoria de la multiplicacion 
# de la cantidad de informacion por la probabilidad de salida de cada simbolo, hay una entropia por columna
# ya que cada una pertenece a un simbolo de salida. Al finalizar pongo todas las entropias en un vector

