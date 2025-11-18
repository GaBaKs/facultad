import math

#-------------------------------- EJERCICIO 26 ---------------------------------
# Dadas las siguientes matrices que contienen mensajes representados con código ASCII y
# sus bits de paridad vertical, longitudinal y cruzada, detectar los errores y, en caso de ser
# posible, recuperar el mensaje original:
#-------------------------------- EJERCICIO 26 ---------------------------------

def verifica_paridad(byte):
    x = byte.copy()
    paridad = x.pop()
    cantidad_unos = x.count('1')
    flag = False
    if cantidad_unos % 2 == 0 and paridad == '0': #Cantidad de 1s par -> bit de paridad = 0
        flag = True
    else:
        if cantidad_unos % 2 != 0 and paridad == '1': #Cantidad de 1s impar -> bit de paridad = 1
            flag = True
    return flag

def recupera_mensaje(matriz): #Podria ahorrar codigo, pero anda asi que ya fue 
    errores = 0
    fl = False
    fv = False
    fc = True

    cruzv = matriz[0]
    cruzh = [fila[7] for fila in matriz]

    if (not verifica_paridad(cruzv)) or (not verifica_paridad(cruzh[::-1])):
        fc = False    

    #Verifica cantidad de errores comprobando los bits de paridad verticales
    for i in range(len(matriz)):
        fila = matriz[i]
        if not verifica_paridad(fila):
            errores+=1
            coord_x = i
            fv = True

    #Verifica cantidad de errores comprobando los bits de paridad longitudinales
    for j in range(7): #Una columna menos, por la de paridad horizontal
        columna = [fila[j] for fila in matriz]
        if not verifica_paridad(columna[::-1]):
            errores+=1
            coord_y = j
            fl = True
    
    #Dependiendo la cantidad de errores recupera el mensaje o indica que no fue posible recuperarlo
    
    if errores == 0 and fc: #No hay errores
        mensaje = []
        flag = False #La uso para saltear la primer fila, que son los bits de paridad verticales
        for fila in matriz:
            if flag:
                byte = "".join(fila[:-1])
                valor = int(byte,2)
                mensaje.append(chr(valor))
            else:
                flag = True
        print(mensaje)
    else:
        if((errores == 2) and (fl and fv and fc)): #Se puede recuperar el mensaje, ya que hay errores corregibles
            if(errores == 2): #Tiene errores, se corrige el mensaje
                print("Se encontro un error en la posicion: [ ",coord_x," ; ",coord_y," ]")
                if matriz[coord_x][coord_y] == '0':
                    matriz[coord_x][coord_y] = '1'
                else:
                    matriz[coord_x][coord_y] = '0'
            mensaje = []
            flag = False #La uso para saltear la primer fila, que son los bits de paridad verticales
            for fila in matriz:
                if flag:
                    byte = "".join(fila)
                    valor = int(byte,2)
                    mensaje.append(chr(valor))
                else:
                    flag = True
            print(mensaje)
        else:
            print("No se puede decodificar el mensaje, pedir retransmision del mismo")

matriz = [
    ['0', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '0', '0', '0', '0', '1', '1', '1'], 
    ['1', '0', '0', '0', '0', '0', '1', '0'],  
    ['1', '0', '1', '0', '0', '1', '1', '0'],  
    ['1', '0', '0', '0', '0', '0', '1', '0']   
]

recupera_mensaje(matriz)


# Si me dan un mensaje genero una matriz agregando la fila y columna correspondiente a la paridad horizontal, vertical y el bit de paridad cruzada
# Compruebo que las paridades verticales, horizontales y cruzadas se cumplan al ver si hay 1s o 0s pares o impares
# Si la cruzada no se cumple considero el mensaje perdido y vuelvo a pedir su transmision
# Viendo las distancias de hamming compruebo si la cantidad de errores es corregible o si debo pedir una nueva transmision del mensaje
# Si puedo corregirlo lo hago y luego proceso la matriz para decodificar el mensaje