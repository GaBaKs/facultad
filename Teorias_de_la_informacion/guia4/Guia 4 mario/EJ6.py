import math

#-------------------------------- EJERCICIO 6 ---------------------------------
#Realizar una función en Python que reciba como parámetros: dos listas paralelas con la
#distribución de probabilidades de una fuente y su codificación, y calcule el rendimiento y la
#redundancia del código.
#-------------------------------- EJERCICIO 6 ---------------------------------

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

def calcula_rendimiento(ListaP, cod): #Calcula el rendimiento de un codigo
    Ln = longitud_media(ListaP,cod)
    H = calcula_entropia(ListaP,r)
    return H/Ln

def calcula_redundancia(ListaP, cod): #Calcula la redundancia de un codigo
    Ln = longitud_media(ListaP,cod)
    H = calcula_entropia(ListaP,r)
    return (Ln - H)/Ln

fuente = ['BA', 'CAB', 'A','CBA'] #Simbolos de la fuente
ListaP = [0.3, 0.1, 0.4, 0.2] #Probabilidades de la fuente

r = 2 #Cantidad de simbolos del codigo, sera la base de los logaritmos

cod = ['0', '10', '11', '100'] #Codigo propuesto / Deberia usar algun algoritmo

print("Rendimiento: ",calcula_rendimiento(ListaP,cod))
print("Redundancia: ",calcula_redundancia(ListaP,cod))