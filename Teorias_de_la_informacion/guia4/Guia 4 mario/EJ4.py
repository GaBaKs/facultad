import math

#-------------------------------- EJERCICIO 4 ---------------------------------
#Para una fuente binaria con ω = 0.8, calcular la extensión de orden 3 y proponer una
#codificación binaria que cumpla con el Primer Teorema de Shannon.
#-------------------------------- EJERCICIO 4 ---------------------------------

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
    N = int(input("ingrese dimension de la extension (N): "))
    Ext, Extp = extensionN(fuente, ListaP, N, [], [], N-1) #Las listas vacias seran Ext y Extp, N-1 es una variable de control que se utiliza en la funcion recursiva
    entropia = calcula_entropia(Extp,r)
    Ln = longitud_media(Extp,Ext)
    print(entropia," <= ",Ln," < ",entropia+1)
    if(entropia <= Ln < entropia+1): #Teorema de Shannon
        return print("El teorema de Shannon se cumple")
    else:
        return print("El teorema de Shannon no se cumple")
    
w = 0.8 #Probabilidad del simbolo '0'
fuente = ['0','1'] #Simbolos de la fuente
ListaP = [w,1-w] #Probabilidades de la fuente
r = 2 #Cantidad de simbolos del codigo, sera la base de los logaritmos

#En este caso utilizamos la extension de orden 3 de la fuente binaria, esta fue suficiente para cumplir con el teorema de Shannon
#Ext = ['000', '001', '010', '100', '110', '101', '011', '111']

Teorema_Shannon(fuente, ListaP, r)
