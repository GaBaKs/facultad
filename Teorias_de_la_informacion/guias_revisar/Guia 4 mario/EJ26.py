import math

#-------------------------------- EJERCICIO 26 ---------------------------------
# Dadas las siguientes matrices que contienen mensajes representados con código ASCII y
# sus bits de paridad vertical, longitudinal y cruzada, detectar los errores y, en caso de ser
# posible, recuperar el mensaje original:
#-------------------------------- EJERCICIO 26 ---------------------------------

def paridad_caracter(caracter):
    byte = []
    val = bin(ord(caracter))
    for x in val[2:]: #Se saltea el '0b' inicial
        byte.append(x)
    if val.count('1') % 2 == 0:
        byte.append('0') #Bit de paridad par
    else:
        byte.append('1') #Bit de paridad impar
    return byte

def verifica_paridad(byte):
    paridad = byte.pop()
    cantidad_unos = byte.count('1')
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
    #Verifica cantidad de errores comprobando los bits de paridad verticales
    for i in range(len(matriz)):
        fila = matriz[i]
        if not verifica_paridad(fila):
            errores+=1
            coord_x = i
            fv = True

    #Verifica cantidad de errores comprobando los bits de paridad longitudinales
    for j in range(6): #Una columna menos, por la de paridad horizontal
        columna = [fila[j] for fila in matriz]
        if not verifica_paridad(columna):
            errores+=1
            coord_y = j
            fl = True

    #Dependiendo la cantidad de errores recupera el mensaje o indica que no fue posible recuperarlo
    
    if errores == 0: #No hay errores
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
        if((errores == 2) and (fl and fv)): #Se puede recuperar el mensaje, ya que hay errores corregibles
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
            print("No se puede decodificar el mensaje")

def genera_matriz_codigo(mensaje):
    mensaje = list(mensaje)
    matriz = []
    for c in mensaje:
        matriz.append(paridad_caracter(c)) #Columna de paridad horizontal
    vertical = []
    for i in range(7): #Fila de paridad vertical
        columna = [fila[i] for fila in matriz]
        if columna.count('1') % 2 == 0:
            vertical.append('0')
        else:
            vertical.append('1')
    if vertical.count('1') % 2 == 0: #Bit de paridad cruzada, con revisar uno de las 2 paridades basta para crear el cruzado
        vertical.append('0')
    else:
        vertical.append('1')
    matriz.insert(0,vertical) #Agrego la fila de paridad vertical a la matriz, siendo esta la primer fila
    return matriz



mensaje = "Terminé el ejercicio :)"

matriz = genera_matriz_codigo(mensaje)
recupera_mensaje(matriz)

