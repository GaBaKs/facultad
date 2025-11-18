import math

#-------------------------------- EJERCICIO 8 ---------------------------------
#Comparar los rendimientos y las redundancias de los siguientes códigos:
#Codigo propuesto 1 = ['01', '111', '110', '101','100']
#Codigo propuesto 2 = ['00', '01', '10', '110','111'] 
#Codigo propuesto 3 = ['0110', '010', '0111', '1','00'] 
#Codigo propuesto 4 = ['11', '001', '000', '10','01']
#-------------------------------- EJERCICIO 8 ---------------------------------

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

fuente = ['A','B','C','D','E'] #Simbolos de la fuente
ListaP = [0.2, 0.15, 0.1, 0.3, 0.25] #Probabilidades de la fuente

r = 2 #Cantidad de simbolos del codigo, sera la base de los logaritmos

cod1 = ['01', '111', '110', '101','100'] #Codigo propuesto 1
cod2 = ['00', '01', '10', '110','111'] #Codigo propuesto 2
cod3 = ['0110', '010', '0111', '1','00'] #Codigo propuesto 3
cod4 = ['11', '001', '000', '10','01'] #Codigo propuesto 4

print("Rendimiento: ",calcula_rendimiento(ListaP,cod4))
print("Redundancia: ",calcula_redundancia(ListaP,cod4))