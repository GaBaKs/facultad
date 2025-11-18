


def probabilidad_error(matriz,probabilidades):
    if(1/len(probabilidades)==probabilidades[0]):
        probabilidad=0
        for i in range(len(matriz)):
            indice_maximo=0
            maximo=-999
            for j in range(len(matriz[0])):
                if(matriz[i][j]>maximo):
                    maximo=matriz[i][j]                 # saco el maximo de la columna y guardo su valor e indice
                    indice_maximo=j

            for j in range(len(matriz[0])):                   #sumo los valores de la matriz, menos los del maximo
                if(j!=indice_maximo):
                    probabilidad+=matriz[i][j]


        return 1/len(probabilidades) * probabilidad                #devuelvo 1/r * sumatoria p(b/a)
        
    else:
        probabilidad=0
        for i in range(len(matriz)):
            indice_maximo=0
            maximo=-999
            sumatoria=0
            for j in range(len(matriz[0])):
                if(matriz[i][j]>maximo):
                    maximo=matriz[i][j]                 # saco el maximo de la columna y guardo su valor e indice
                    indice_maximo=j
            
            for j in range(len(matriz[0])):
                if(j!=indice_maximo):
                    sumatoria+=matriz[i][j]
            probabilidad+=sumatoria*probabilidades[i]
            print("sumatoria ",sumatoria," multiplico ",probabilidades[j])
            print("probabilidad ",probabilidad)

        return probabilidad    
            
            

            

probabilidades=[4/15,3/15,8/15 ]

matriz=[[0.6,0.3,0.1],[0.1,0.8,0.1],[0.3,0.3,0.4]]

print("probabilidad de error ",probabilidad_error(matriz,probabilidades))

# Calcula la probabilidad de error del canal
# Para esto se busca el valor de probabilidad maxima de la fila y se suma el resto
# el resultado del valor maximo - la suma del resto nos da el error de la fila y 
# haciendo un promedio (en caso de tener diferentes valores maximos estos se ponderan)
# y asi obteniendo el error del canal que como su nombre indica representa las probabilidades
# de obtener una salida erronea proveniente de una entrada X