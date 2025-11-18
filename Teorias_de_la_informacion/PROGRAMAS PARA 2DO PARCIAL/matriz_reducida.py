


def matriz_canal_reducido(matriz):
    matriz_reducida=matriz
    cond=True
    i=0
    while(len(matriz_reducida[0])>1 and cond==True ):
        if(i<len(matriz_reducida[0])-2):
            j=i+1
            reduccion=False         #esta condicion me dice si ya reduci la matriz por lo q deberia empezar a comparar desde el inicio
            while(j<len(matriz_reducida[0]) and reduccion==False): 
                if(verifica_CL(matriz_reducida,i,j)):
                    matrizDet=matriz_determinante(matriz_reducida,i,j)
                    print(matrizDet)
                    matriz_reducida=matriz_producto_vectorial(matriz_reducida,matrizDet)
                    reduccion=True
                else:
                   j+=1
            
            if(reduccion==False):      #si no la reduci continuo buscando columnas que sean CL y si no arranco desde el inicio
                i+=1
            else:
                i=0
        else:
            cond=False      #ya no puedo reducir mas la matriz                      
            
    return matriz_reducida


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



def suma(matriz1,matriz2,i,j):
    sumatoria=0

    for k in range(len(matriz1[0])):
        sumatoria+=matriz1[i][k]*matriz2[k][j]        



    return sumatoria



def matriz_producto_vectorial(matriz1,matriz2):            #hace el producto vectorial para obtener la matriz
    mat_resultante=[]

    for i in range(len(matriz1)):           #recorre las filas de matriz 1
        mat_resultante.append([])
        for j in range(len(matriz2[0])):  #recorre las columnas de matriz2
            mat_resultante[i].append(suma(matriz1,matriz2,i,j))

    return mat_resultante


matriz=[[1/6,1/3,1/2,0],[1/12,1/6,1/4,1/2]]

print("matriz reducida: ",matriz_canal_reducido(matriz))

# A partir de una matriz realizo las reducciones posibles y devuelvo la matriz del canal reducido 
# simplemente analizo todas las combinaciones de columnas y compruebo si se pudieran reducir
# Dado este caso las reduzco calculando la multiplicacion vectorial entre mi matriz original y la matriz
# reducida en una columna, ya que esta se convierte en una combinacion de las columnas reducidas
# y finalmente obtengo la matriz reducida
# Si las columnas reducidas resultasen identicas la reduccion será sin ruido y podremos comprimir
# la matriz sin consecuencia alguna