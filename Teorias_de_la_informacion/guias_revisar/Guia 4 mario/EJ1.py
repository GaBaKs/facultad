import math

#-------------------------------- EJERCICIO 1 ---------------------------------
# Codificar una función booleana en Python que reciba como parámetros: una lista con la
# distribución de probabilidades de una fuente, otra lista con palabras código para la
# extensión de orden N y el valor de N, y verifique si el código cumple con el Primer Teorema
# de Shannon.
#-------------------------------- EJERCICIO 1 ---------------------------------

def extensionN(alfabeto, dist_prob , n, nueva_alfabeto, nueva_dist_prob, i): #Calcula la extension de una fuente y sus probabilidades
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

def calcula_entropia(prob,r): #Calcula la entropia de una fuente
    entropia = 0
    for p in prob:
        entropia = entropia + p * (math.log(1/p, r))
    return entropia 

def longitud_media(prob, alfabeto): #Calcula la longitud media de un codigo
    Ln = 0
    for p, x in zip(prob, alfabeto):
        Ln = Ln + p * len(x)
    return Ln

def Teorema_Shannon(fuente, ListaP, r): #Verfica si se cumple el teorema de Shannon
    N = 2
    Ext, Extp = extensionN(fuente, ListaP, N, [], [], N-1) #Las listas vacias seran Ext y Extp, N-1 es una variable de control que se utiliza en la funcion recursiva
    entropia = calcula_entropia(Extp,r)
    Ln = longitud_media(Extp,Ext)
    print(entropia," <= ",Ln," < ",entropia+1)
    if(entropia <= Ln < entropia+1): #Teorema de Shannon
        return print("El teorema de Shannon se cumple")
    else:
        return print("El teorema de Shannon no se cumple")
    
fuente = ['BA', 'CAB', 'A','CBA'] #Simbolos de la fuente
ListaP = [0.3, 0.1, 0.4, 0.2] #Probabilidades de la fuente
r = 3 #Cantidad de simbolos del codigo, sera la base de los logaritmos

Teorema_Shannon(fuente, ListaP, r)
