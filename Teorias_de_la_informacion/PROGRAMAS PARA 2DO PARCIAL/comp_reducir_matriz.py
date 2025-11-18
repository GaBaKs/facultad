

def verifica_CL(mat,m1,m2):
    cond=True
    i=0
    hay_cte=False
    while(i<(len(mat)) and cond==True):
        
        if(not hay_cte):
            if(mat[i][m1]==0 and mat[i][m2]==0):
                i+=1
            else:
                if(mat[i][m1]==0):
                    cond=False
                else:
                    if(mat[i][m2]==0):
                        cte=0
                        hay_cte=True
                        i+=1
                    else:
                        cte=mat[i][m1]/mat[i][m2]
                        hay_cte=True
                        i+=1
        else:
            if(mat[i][m1]==0 and mat[i][m2]==0):
                i+=1
            else:
                if(mat[i][m1]==0):
                    cond=False
                else:
                    if(mat[i][m2]==0):
                        if(cte==0):
                            i+=1
                        else:
                            cond=False
                    else:
                        if(mat[i][m1]/mat[i][m2]==cte ):
                            i+=1
                        else:
                            cond=False
        


    return cond 

def matriz_determinante(matriz,m1,m2):
    matDet=[]

    if(verifica_CL(matriz,m1,m2)):
        for j in range(len(matriz[0])):
            matDet.append([])
            for i in range(len(matriz[0])-1):
                if(i==j):
                    matDet[j].append(1)
                else:
                    matDet[j].append(0)
        
        matDet.insert(m2,matDet[m1])
        matDet.remove(matDet[len(matDet)-1])
       
        

    return matDet

matriz=[[0.4,0.6,0.8,0],[0.3,0,0.6,0],]
m1=0
m2=2

print("condicion: ",verifica_CL(matriz,m1,m2))
print("matriz determinante: ",matriz_determinante(matriz,m1,m2))

# Verifico si las columnas de la matriz son linealmente dependientes, por lo que puedo hallar una constante que al multiplicar una columna
# por esta será igual a la otra columna, esto se hace para comprobar si es posible reducir la columna
# Simplemente comparo 2 columnas, moviendome elemento a elemento analizo si existe tal constante, si esta no existe
# o se da el caso de que no es la misma constante para toda la columna la condicion sera falsa
# si existe y es unica la condicion será verdadera y podremos reducir las columnas