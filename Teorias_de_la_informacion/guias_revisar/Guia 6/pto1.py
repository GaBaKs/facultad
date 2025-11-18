[]

mat = [[0.3,0.5,0.2],
       [0.2,0.3,0.5],
       [0.5,0.2,0.3]]

# funcion booleana, devuelve si es un canal sin ruido
def CanalSinRuido(mat):
    sinRuido = True
    j = 0

    while(j in range(len(mat[0])) and sinRuido):
        sinRuido = (sum(1 for i in range(len(mat)) if mat[i][j] != 0)) == 1
        j += 1
    
    if (sinRuido): print("Canal SIN ruido")
    else: print("Canal CON ruido")

    #return sinRuido

# booleana
def CanalDeterminante(mat):
    det = True
    i = 0

    while(i in range(len(mat)) and det):
        det = (sum(1 for j in range(len(mat[0])) if mat[i][j] != 0)) == 1
        i += 1
    
    if (det): print("Canal determinante")
    else: print("Canal NO determinante")

    #return det

CanalSinRuido(mat)
CanalDeterminante(mat)