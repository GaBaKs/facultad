from Huffman import Velemento,Auxelem,huffman
from Shannon_Fano import SAuxelem,Shannon_Fano_rec,shannon_fano
import math
"""def alfabeto(cadena):
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
    return res,prob"""

def codifica(alfabeto,alfcodigo,mensaje):

    codificado=""
    ba=bytearray()
    cont=0
    for x in mensaje:
       codificado+=alfcodigo[alfabeto.index(x)]
    #print("el codificado",codificado)
    while len(codificado)%8!=0:
        codificado=codificado+"0" #agrego ceros para completar el byte
        cont+=1
    for i in range(0, len(codificado), 8):
        byte = codificado[i:i+8]
        ba.append(int(byte, 2))
    ba.append(int(cont)) #agrego la cantidad de ceros que agrege al final
    #for b in ba:
        #print(format(b, '08b'))
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

alfabeto = [
  " ", ",", ".", ":", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
  "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

probs = [
  0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
  0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
  0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
  0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199,
]
mensaje="PRUEBA NUEVA.,:; HOLA"
alfabeto_codigoH=huffman(probs,alfabeto)
alfabeto_codigoS=shannon_fano(probs,alfabeto)
mensaje_codificadoH=codifica(alfabeto,alfabeto_codigoH,mensaje)
mensaje_codificadoS=codifica(alfabeto,alfabeto_codigoS,mensaje)
with open('msj_codificado_ej17_H2.dat', 'wb') as archivo:
    archivo.write(mensaje_codificadoH)
with open('msj_codificado_ej17_S.dat', 'wb') as archivo:
    archivo.write(mensaje_codificadoS)
#with open('msj_codificado_ej17_H.dat', 'rb') as archivoLect:
    #mensaje_leidoH = archivoLect.read() 
#decodifica(alfabeto,alfabeto_codigoH,mensaje_leidoH)
def Entropia(prob,r):
    E=0 
    I=[math.log(1/X, r) for X in prob ]
    #print("el I",I)
    for a in range(len(prob)) :
        E+= (prob[a]*I[a])
    return E

def longCod(cod):
    return [len(C) for C in cod ]

def longMedia(prob,cod):
    suma=0
    for x in range(len(cod)):
        suma+= prob[x] *cod[x]
    return suma

def tasa_de_compresion(mensaje: str, mensaje_codificado:bytearray):
    tam_original = len(mensaje.encode('utf-8'))
    tam_codificado = len(mensaje_codificado)
    tasa = tam_original / tam_codificado if tam_codificado != 0 else 0
    return tasa
def rendimiento(prob,cod):
    
    H=Entropia(prob,2)
    L=longMedia(prob,longCod(cod))
    if L!=0:
        nn=H/L
        R=1-nn
    else:
        nn=0
        R=1
    return nn,R
print("Tasa de compresion Huffman:",tasa_de_compresion(mensaje,mensaje_codificadoH,))
print("Tasa de compresion Shannon-Fano:",tasa_de_compresion(mensaje,mensaje_codificadoS))
print("el rendimiento y la redundancia del codigo huffman es: ",rendimiento(probs,alfabeto_codigoH))
print("el rendimiento y la redundancia del codigo shannon es: ",rendimiento(probs,alfabeto_codigoS))
