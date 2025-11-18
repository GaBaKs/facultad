




def verifica_canal_uniforme(matriz_canal):
    cond=True

    i=0 
    while(i<len(matriz_canal[0]) and cond==True):
        if(len(matriz_canal)>1):
            j=1
            while(j<len(matriz_canal) and cond==True):
                if(matriz_canal[0].count(matriz_canal[0][i])==matriz_canal[j].count(matriz_canal[0][i])):
                    j+=1
                else:
                    cond=False
            
            if(cond):
                i+=1
        else:
            print("tiene una fila sola")
            cond=False

    
    return cond




matriz_canal=[[1/3,1/6,1/2],[0.5,0,0.5]]
print(verifica_canal_uniforme(matriz_canal))

# Comprueba si el canal es uniforme verificando si cada columna son permutaciones entre si,
# esto se hace contando la frecuencia de aparicion de cada simmbolo en la primer columna y
# comparandolas con las demás, si son iguales entonces la matriz sera uniforme