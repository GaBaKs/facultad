"""  Implementar funciones en Python que reciban como parámetros: una cadena de 
caracteres que contenga un alfabeto fuente y una lista de cadenas de caracteres que 
almacena una codificación en el alfabeto binario, y resuelvan lo siguiente: 
a. Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente, 
devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado. 
b. Dada una secuencia de bytes, decodificar y retornar el mensaje original. 
Sugerencia: manipular el mensaje codificado como una cadena de caracteres de unos y 
ceros, tanto para codificar como para decodificar, y realizar las conversiones entre binarios 
y enteros con las funciones de casteo correspondientes.  """
import math
def alfabeto(cadena):
    res=[]
    prob=[]
    for letra in cadena:
        if  not letra in res :
            res.append(letra)
            prob.append(1)
        else: 
         prob[res.index(letra)]+=1
    prob=[(x/len(cadena))for x in prob]
   # print(prob)
    return res,prob

def codifica(alfabeto,alfcodigo,mensaje):

    codificado=""
    ba=bytearray()
    cont=0
    for x in mensaje:
       codificado+=alfcodigo[alfabeto.index(x)]
    print("el codificado",codificado)
    while len(codificado)%8!=0:
        codificado=codificado+"0" #agrego ceros para completar el byte
        cont+=1
    for i in range(0, len(codificado), 8):
        byte = codificado[i:i+8]
        ba.append(int(byte, 2))
    ba.append(int(cont)) #agrego la cantidad de ceros que agrege al final
    for b in ba:
        print(format(b, '08b'))
    return ba

def decodifica(alfabeto,alfcodigo,ba):
    codificado=""
    mensaje=""
    for b in ba:
        codificado+=format(b, '08b')
    print("el codificado es:",codificado)
    ceros=int(codificado[-8:],2) #cantidad de ceros que agrege al final
    codificado=codificado[:len(codificado)-8-ceros] #quito los ceros y el byte que indica la cantidad de ceros
    print("el codificado sin ceros es:",codificado)
    aux=""
    for x in codificado:
        aux+=x
        if aux in alfcodigo:
            mensaje+=alfabeto[alfcodigo.index(aux)]
            aux=""
    print("el mensaje decodificado es:",mensaje)
    return mensaje

#mensaje="ABACBAACABABAACBABA"
#alf,prob =alfabeto(mensaje)
#print("el alfabeto fuente es:",alf)
#print("la probabilidad es:",prob)
#alfcodigo=shannon_fano(prob,alf)
#ba=codifica(mensaje,alfcodigo)
#decodifica(ba,alfcodigo)
