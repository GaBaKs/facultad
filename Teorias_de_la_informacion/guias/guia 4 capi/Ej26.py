
def armaMAT(mensaje):
    """Recibe un mensaje y devuelve una lista con los valores ASCII de cada caracter con bit de paridad par."""
    mat=[]

    for i in range(1,len(mensaje)):
        car = mensaje[i]
        valor_ascii = ord(car)
        num_unos = bin(valor_ascii).count('1')
        if num_unos % 2 == 0:
            valor_con_paridad = valor_ascii << 1  # Desplazar a la izquierda y agregar 0
        else:
            valor_con_paridad = (valor_ascii << 1) | 1  # Desplazar a la izquierda y agregar 1
        for j in range(8):
            bit = (valor_con_paridad >> (7 - j)) & 1
        mat[i].append(bit)
    for j in range(8):                      #armo la paridad vertical
        for i in range(1,len(mensaje)-1):
            if mat[i][j]==1:
                cont+=1
        if cont%2==0:
            mat[0][j]=0
        else: 
            mat[0][j]=1
    conti=0                 
    contj=0
    for i in range(7):                         #armo la praridad cruzada
        if mat[0][i]==1:
            conti+=1
    for j in range(1,len(mensaje)):
        if mat[7][j]==1:
            contj+=1
    if conti%2==0 and contj%2==0:
        mat[7][0]=0
    else:
        mat[7][0]=1
    return mat

def armaBA(mat):
    """Recibe una matriz de bits y devuelve un bytearray por fila de la matriz"""
    ba=bytearray()
    for i in range(len(mat)):
        byte=0
        for j in range(8):
            byte = (byte << 1) | mat[i][j]
        ba.append(byte)
    return ba

def decodificaBA(ba:bytearray):
    """Recibe un bytearray lo convierte a matriz de bits y verifica la pariridad vertical, horizontal y cruzada
    si no tiene errores o los corrige devuelve el mensaje decodificado si no de vuelve un mensaje vacio"""
    mat=[]
    mensaje=""
    for i in range(len(ba)):
        fila=[]
        for j in range(8):
            bit=(ba[i]>>7-j)&1
            fila.append(bit)
        mat.append(fila)
    lista_errores_verticales=[]
    lista_errores_horizontales=[]
    #verifico paridad vertical
    for j in range(7):
        paridad_vertical=0
        for i in range(1,len(mat)):
            paridad_vertical+=mat[i][j]
        if paridad_vertical % 2 != mat[0][j]:
            lista_errores_verticales.append(j)
            print("Error en la columna:",j)
    #verifico paridad horizontal    
    for i in range(1,len(mat)):
        paridad_horizontal=0
        for j in range(7):
            paridad_horizontal+=mat[i][j]
        if paridad_horizontal%2 != mat[i][7]:
            lista_errores_horizontales.append(i)
            print("Error en la fila:",i)
    #verifico paridad cruzada
    paridad_cruzada_i=0
    paridad_cruzada_j=0
    for j in range(7):
        paridad_cruzada_i+=mat[0][j]
    for i in range(1,len(mat)):
        paridad_cruzada_j+=mat[i][7]    
    if paridad_cruzada_i%2 != mat[0][7] or paridad_cruzada_j%2 != mat[0][7]:            #error en la paridad, la suma de la paridad verticaly/o horizontal no coincide con la cruzada
        print("Error en la paridad cruzada")

    print("lista errores verticales:",lista_errores_verticales)
    print("lista errores horizontales:",lista_errores_horizontales)
    if len(lista_errores_verticales)==1 and len(lista_errores_horizontales)==1:     #no tiene errores detectados pero la paridad cruzada falla
        j=lista_errores_verticales[0]
        i=lista_errores_horizontales[0]
        print("Corrigiendo error en la posicion: fila",i,"columna",j)
        print("el valor era:",mat[i][j])
        mat[i][j]=1-mat[i][j] #corrijo el error cruzado
        print("el valor paso a ser:",mat[i][j])
    elif len(lista_errores_verticales)>1 and len(lista_errores_horizontales)>1:   #error corregible
        print("Error no corregible")
        return "" #error no corregible
    for i in range(1,len(mat)):
        byte=0
        for j in range(7):
            byte=(byte<<1)|mat[i][j]
        mensaje+=chr(byte)
    return mensaje
            

mata=[
    [0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,1,0],
    [1,0,1,0,0,1,1,0],
    [1,0,0,0,0,0,1,0]
]
matb=[
    [0,0,1,0,1,1,0,1],
    [1,0,0,1,1,0,0,1],
    [1,0,0,0,1,0,1,0],
    [1,0,0,1,1,1,0,0],
    [1,0,0,0,0,0,1,0]
]
matc=[
    [0,0,1,0,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,0,0,1,1,0,1,0],
    [1,0,0,1,1,1,1,1],
    [1,0,1,0,0,1,0,1]
]
matd=[
    [0,0,0,1,0,1,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,1,1,1,0],
    [1,0,0,1,1,0,0,1],
    [1,0,0,0,0,0,1,0]
]
mate=[
    [0,0,1,1,0,1,0,1],
    [1,0,0,1,1,0,1,0],
    [1,0,1,0,1,0,1,1],
    [1,0,1,0,0,1,0,0],
    [1,0,0,0,0,0,1,0]
]
matf=[
    [0,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,0,0,1,0,1,1],
    [1,0,1,0,0,1,1,0]
]
matg=[
    [0,0,0,1,1,1,0,1],
    [1,0,0,1,0,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,0,0,0,1,1,0,0],
    [1,0,0,1,1,1,1,1]
]
math=[
    [0,0,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,1],
    [1,0,0,1,0,0,0,0],
    [1,0,0,0,0,0,1,0],
    [1,0,1,0,1,0,1,0]
]
print("la longitud de la mata es:",len(matb))

armaBA(matg)
msj=decodificaBA(armaBA(matg))
print("el mensaje decodificado es:",msj)
