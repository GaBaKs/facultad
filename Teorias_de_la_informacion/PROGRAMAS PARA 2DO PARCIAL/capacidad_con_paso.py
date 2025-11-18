
import math

def probs_salida(probs_entrada,matriz):             #calcula las probabilidades de los elementos de salida(P[bj]), devuelve una lista
    probs_salida=[]
    
    for j in range(len(matriz[0])):
        sumatoria=0
        for i in range(len(probs_entrada)):
            sumatoria+=probs_entrada[i]*matriz[i][j]
        
        probs_salida.append(sumatoria)

    return probs_salida

def matriz_aposteriori(probabilidades_entrada,probabilidades_salida,matriz):            #calcula la matriz con las probabilidades aposteriori(P[ai/bj])
    matriz_posteriori=[]
    

    for i in range(len(matriz)):
        matriz_posteriori.append([])
        for j in range(len(probabilidades_salida)):
            if(probabilidades_salida[j]):
                aux=(probabilidades_entrada[i]*matriz[i][j])/probabilidades_salida[j]       # P(ai/bj)=(P(bj/ai)*P(ai))/P(bj)
            matriz_posteriori[i].append(aux)

    return matriz_posteriori


def matriz_eventos_simultaneos(probabilidades_entrada,matriz):          #cada elemento de la matriz lo calcule con P(bj/ai) . P(ai)
    matriz_simultaneos=[]

    for i in range(len(probabilidades_entrada)):
        matriz_simultaneos.append([])
        for j in range(len(matriz[i])):
            matriz_simultaneos[i].append(matriz[i][j] * probabilidades_entrada[i])
    



    return matriz_simultaneos



def informacion_mutua(probabilidades,matriz):
    probs_post=probs_salida(probabilidades,matriz)
    matriz_apos=matriz_aposteriori(probabilidades,probs_post,matriz)
    matriz_simultaneos=matriz_eventos_simultaneos(probabilidades,matriz)
    informacion=0

    for i in range(len(probabilidades)):
        for j in range(len(probs_post)):
            if((matriz_simultaneos[i][j]!=0 and probabilidades[i]*probs_post[j])!=0):
                informacion+=matriz_simultaneos[i][j] * math.log2(matriz_simultaneos[i][j]/(probabilidades[i]*probs_post[j]))


    return informacion




def capacidad_y_probPaso(matriz):

    i=0
    informacion_maxima=-9999            
    prob_paso=0
    while(i<=1):
        probabilidades=[i,1-i]
        if(informacion_mutua(probabilidades,matriz)>informacion_maxima):
            informacion_maxima=informacion_mutua(probabilidades,matriz)              #calculo la informacion mutua apartir de la probabilidad de paso
            prob_paso=i                                                 #si es la maxima(momentaneamente) guardo su probabilidad de paso y su informacion mutua
        
        i+=0.0001 # paso




    return informacion_maxima,prob_paso



matriz_canal_binario=[[0.77,0.23],[0.2,0.8]]
capacidad,prob_paso=capacidad_y_probPaso(matriz_canal_binario)

print("capacidad: ",capacidad)
print("probabilidad de paso ",prob_paso)

# Calcula la capacidad con un metodo numerico iterando con un paso designado sobre la matriz y calculando
# informacion util transmitida (informacion mutua), quedandose con la maxima
# calculo la informacion mutua apartir de la probabilidad de paso
# si es la maxima(momentaneamente) guardo su probabilidad de paso y su informacion mutua
# avanzo con el paso designado hasta llegar a 1
# con esto puedo hallar la capacidad (informacion mutua maxima)
# y la probabilidad perteneciente al paso usado en esa iteracion