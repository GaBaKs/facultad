import math

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

def genera_prob_simultaneas(prob_salida,matriz_posteriori): 
    prob_simultanea = []
    for i in range(len(matriz_posteriori)): 
        prob = []
        fila = matriz_posteriori[i]
        for j in range(len(fila)):
            prob.append(fila[j]*prob_salida[j])
        prob_simultanea.append(prob)
    return prob_simultanea

def calcula_ruido(prob_apriori,matriz_canal):
    prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
    matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
    matriz_simultaneas = genera_prob_simultaneas(prob_salida,matriz_posteriori)
    ruido = 0
    r = 2 #Medidas en bits
    for i in range(len(matriz_simultaneas)):
        fila = matriz_simultaneas[i]
        for j in range(len(fila)):
            if matriz_posteriori[i][j] != 0:
                ruido+= fila[j]*math.log(1/matriz_posteriori[i][j],r)
    return ruido

def calcula_perdida(prob_apriori,matriz_canal):
    prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
    matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
    matriz_simultaneas = genera_prob_simultaneas(prob_salida,matriz_posteriori)
    perdida = 0
    r = 2 #Medidas en bits
    for i in range(len(matriz_simultaneas)):
        fila = matriz_simultaneas[i]
        for j in range(len(fila)):
            if matriz_canal[i][j] != 0:
                perdida+= fila[j]*math.log(1/matriz_canal[i][j],r)
    return perdida

def calcula_entropia_afin(prob_apriori,matriz_canal):
    prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
    matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
    matriz_simultaneas = genera_prob_simultaneas(prob_salida,matriz_posteriori)
    entropia_afin = 0
    r = 2 #Medidas en bits
    for i in range(len(matriz_simultaneas)):
        fila = matriz_simultaneas[i]
        for j in range(len(fila)):
            if fila[j] != 0:
                entropia_afin+= fila[j]*math.log(1/fila[j],r)
    return entropia_afin    

def calcula_informacion_mutua(prob_apriori,matriz_canal):
    prob_salida = genera_prob_salida(matriz_canal,prob_apriori)
    matriz_posteriori = genera_prob_posteriori(prob_apriori,prob_salida,matriz_canal)
    matriz_simultaneas = genera_prob_simultaneas(prob_salida,matriz_posteriori)
    informacion_mutua = 0
    r = 2 #Medidas en bits
    for i in range(len(matriz_simultaneas)):
        fila = matriz_simultaneas[i]
        for j in range(len(fila)):
            if (prob_apriori[i]*prob_salida[j]) != 0 and fila[j] != 0:
                informacion_mutua+= fila[j]*math.log(fila[j]/(prob_apriori[i]*prob_salida[j]),r)
    return informacion_mutua    


prob_apriori = [0.50, 0.50]
matriz_canal = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]

ruido = calcula_ruido(prob_apriori,matriz_canal) #inciso A
print("El ruido en el canal es: H(A/B) = ",round(ruido,4))

perdida = calcula_perdida(prob_apriori,matriz_canal) #Inciso B
print("La perdida en el canal es: H(B/A) = ",round(perdida,4))

entropia_afin = calcula_entropia_afin(prob_apriori,matriz_canal) #Inciso C
print("La entropia afin del canal es: H(A,B) = ",round(entropia_afin,4))

informacion_mutua = calcula_informacion_mutua(prob_apriori,matriz_canal) #Inciso D
print("La informacion mutua del canal es: I(A,B) = I(B,A) = ",round(informacion_mutua,4))

# El ruido es la informacion que se pierde luego de utilizar el canal y mide la incertidumbre sobre la entrada conociendo la salida
# Se calcula como la entropia a posteriori

# La perdida es la informacion que se pierde luego de utilizar el canal y mide la incertidumbre sobre la salida conociendo la entrada (la entrada ya tiene perdida)
# Se calcula haciendo la sumatoria de las probabilidades simultaneas multiplicada por su cantidad de informacion

# La entropia afin mide la incertidumbre total del canal
# Se calcula haciendo la sumatoria de las columnas de la matriz de probabilidades simultaneas multiplicada por su cantidad de informacion

# La informacion mutua es la cantidad de informacion que se transmite correctamente al canal
# Se calcula como la sumatoria de las probabilidades simultaneas multiplicada por el logaritmo en base r (2 en nuestro caso)
# de las probabilidades simultaneas divido la multiplicacion de las probabilidades de la entrada y de la salida
# Para hacerlo simplemente recorro las matrices en paralelo haciendo la cuenta