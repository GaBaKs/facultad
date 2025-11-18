from Huffman import Velemento,Auxelem,huffman
from Shannon_Fano import SAuxelem,Shannon_Fano_rec,shannon_fano
import math
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

def decodifica_info_pri(alfabeto,alfcodigo,ba):
    codificado=""
    mensaje=""
    for b in ba:
        codificado+=format(b, '08b')
    print("el codificado es:",codificado)
    ceros=int(codificado[:8],2) #cantidad de ceros que agrege al final
    codificado=codificado[8:len(codificado)-8-ceros] #quito los ceros y el byte que indica la cantidad de ceros
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
alfabeto_codigoH=huffman(probs,alfabeto)
alfabeto_codigoS=shannon_fano(probs,alfabeto)
with open('msj_codificado_ej17_H2.dat', 'rb') as archivoLect:
    mensaje_leidoH = archivoLect.read() 
decodifica(alfabeto,alfabeto_codigoH,mensaje_leidoH)
