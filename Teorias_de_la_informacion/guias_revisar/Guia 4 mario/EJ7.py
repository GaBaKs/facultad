import math

#-------------------------------- EJERCICIO 7 ---------------------------------
#Comparar los rendimientos y las redundancias de los códigos del ejercicio 3.
#-------------------------------- EJERCICIO 7 ---------------------------------

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

def calcula_rendimiento(ListaP, cod): #Calcula el rendimiento de un codigo
    Ln = longitud_media(ListaP,cod)
    H = calcula_entropia(ListaP,r)
    return H/Ln

def calcula_redundancia(ListaP, cod): #Calcula la redundancia de un codigo
    Ln = longitud_media(ListaP,cod)
    H = calcula_entropia(ListaP,r)
    return (Ln - H)/Ln

ListaP = [0.5, 0.2, 0.3] #Probabilidades de la fuente

r = 2 #Cantidad de simbolos del codigo, sera la base de los logaritmos

cod1 = ['11', '010', '00'] #Codigo propuesto 1
cod2 = ['10', '001', '110', '010', '0000', '0001', '111', '0110', '0111'] #Codigo propuesto 2


print("Rendimiento: ",calcula_rendimiento(ListaP,cod1))
print("Redundancia: ",calcula_redundancia(ListaP,cod1))

N =int(input("ingrese dimension de la extension (N): "))
Ext, ExtP = extensionN(['A','B','C'], ListaP , N, [], [], N-1)

print("Rendimiento: ",calcula_rendimiento(ExtP,cod2))
print("Redundancia: ",calcula_redundancia(ExtP,cod2))