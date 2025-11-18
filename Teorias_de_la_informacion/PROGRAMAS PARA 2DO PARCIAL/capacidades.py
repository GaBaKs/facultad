import math


def capacidad_canal_determinante(matriz):
    return math.log(len(matriz[0]),2)



def capacidad_canal_sin_ruido(matriz):
    return math.log(len(matriz),2)



def capacidad_canal_uniforme(matriz):
    
    sumatoria=0
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if(matriz[i][j]!=0):
                sumatoria+=(matriz[i][j] * math.log(1/matriz[i][j],2))
    
    capacidad=math.log(len(matriz[0]),2)-sumatoria

    return capacidad


matriz_canal=[[],[],[]]

# Calcula las capacidades de canal determinante, sin ruido y uniforme
# capacidad de canal determinante = entropia maxima de la salida (todos simbolos equi-probables)
# capacidad de canal sin ruido = entropia maxima de la entrada (todos simbolos equi-probables)
# capacidad de canal uniforme = entropia maxima de la salida - la perdida
# La capacidad representa el maximo de informacion que puede pasar por el canal de forma exitosa