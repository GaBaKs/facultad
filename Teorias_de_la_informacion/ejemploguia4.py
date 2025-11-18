import math
import random
import copy 
import tdi 


def generalistainfoN(listap,base):
    return [math.log(1/prob,base) for prob in listap]


def entropia(listap,base):
        entropia=0
        informacion=generalistainfoN(listap,base)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia


def cuentasimbolos(palabra):
   simbolos=[]
   cant=[]
   for i in palabra:
          if i in simbolos:
               cant[simbolos.index(i)]+=1
          else:
              simbolos.append(i)
              cant.append(1)
   return simbolos,cant

def probabilidadlista(simbolos,cant):
     listaprob=[]
     total=sum(cant)
     
     for i in simbolos:
        listaprob.append(cant[simbolos.index(i)]/total)
     return listaprob

def longitudMedia(listacodigos,listaprob):
    L=0
    for p,i in zip(listaprob,listacodigos):
        L+=len(i)*p
    return L

def rendimiento(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return ent/L

def redundancia(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return (L-ent)/L


def Huffman(probs):
    nodos = [[p, [i]] for i, p in enumerate(probs)]
    codigos = ["" for _ in range(len(probs))]
    while len(nodos) > 1:
        nodos.sort(key=lambda x: x[0])
        izq = nodos.pop(0)              
        der = nodos.pop(0)
        for i in izq[1]:
            codigos[i] = '0' + codigos[i]
        for i in der[1]:
            codigos[i] = '1' + codigos[i]
        nuevo = [izq[0] + der[0], izq[1] + der[1]]
        nodos.append(nuevo)
    return codigos

def ShannonFano(probabilidades):
    items = [[p, i] for i, p in enumerate(probabilidades)]
    codigo = ['' for _ in range(len(probabilidades))]
    items.sort(reverse=True)
    def recShannonFano(items, codigo):
        if len(items) > 1:
            total = sum(p for p, _ in items)
            acc = 0
            i=0
            while i < len(items) and acc + items[i][0] < total / 2:
                acc += items[i][0]
                i += 1
            # Ahora 'i' es el índice del elemento que podría causar el "desborde"
            # Vamos a decidir si dejarlo en la izquierda o pasarlo a la derecha
            if i < len(items):
                suma_izq = sum(p for p, _ in items[:i + 1])
                suma_der = sum(p for p, _ in items[i + 1:])
                # Si la izquierda supera mucho la mitad, movemos ese elemento al otro lado
                if abs((suma_izq - items[i][0]) - (total/2)) < abs(suma_izq - (total/2)):
                    i -= 1  # mover el elemento al grupo derecho
            for p, idx in items[:i + 1]:
                codigo[idx] += '0'
            for p, idx in items[i + 1:]:
                codigo[idx] += '1'
            recShannonFano(items[:i + 1], codigo)
            recShannonFano(items[i + 1:], codigo)
    recShannonFano(items, codigo)
    return codigo

def codificar_mensaje(mensaje, fuente, codigo): #Lo convierte en un ByteArray
    mensaje_codificado = bytearray()
    buffer = ''
    
    for c in mensaje:
        indice = fuente.index(c)
        buffer+= codigo[indice]

    while len(buffer) >= 8:
        byte = buffer[:8]
        buffer = buffer[8:]
        mensaje_codificado.append(int(byte, 2))  # convierte '10101100' → entero → byte

    # Si quedan bits sobrantes, rellenamos con ceros a la derecha
    bits_sobrantes = 0
    if buffer:
        bits_sobrantes = 8 - len(buffer)
        byte = buffer.ljust(8, '0')
        mensaje_codificado.append(int(byte, 2))
     
    return mensaje_codificado,bits_sobrantes

def decodificar_mensaje(mensaje, fuente, codigo, bits_sobrantes): #Analiza un ByteArray
    
    bits = ''.join(f'{byte:08b}' for byte in mensaje)

    mensaje_decodificado = ""
    buffer = ""

    # Recorremos los bits reconstruyendo los símbolos originales

    if bits_sobrantes > 0:
        bits = bits[:-(bits_sobrantes)]

    for bit in bits:
        buffer += bit
        if buffer in codigo:
            indice = codigo.index(buffer)
            mensaje_decodificado += fuente[indice]
            buffer = ""
    return mensaje_decodificado


mensaje = 'ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB'
fuente,cant=cuentasimbolos(mensaje)
prob=probabilidadlista(fuente,cant)

#si te dan una prob o el huffman ya sabes q hacer tmb (relaciona todo con 1er teorema de shannon)


print("Fuente: ", fuente)
print("Probabilidades: ",prob)

lista_para_imprimir = [f"{valor:.4f}" for valor in prob]

print(f"Probabilidad redondeada: {lista_para_imprimir}")

Huffmanval=Huffman(prob)
Lhuff=longitudMedia(Huffmanval,prob)
shannonval=ShannonFano(prob)
Lshannon=longitudMedia(shannonval,prob)


print("Codificado de Huffman:    ", Huffmanval)
print("L de huffman: ",Lhuff)


print("Codificado de Shannon-Fano:    ", shannonval)
print("L de shannon fano: ",Lshannon)


#codificacion: 

print("Mensaje sin codificar: ",mensaje)

codificadoHuffman,bitsobrantes = codificar_mensaje(mensaje,fuente,Huffmanval)
print("mensaje codificado: ",codificadoHuffman)

decodificado= decodificar_mensaje(codificadoHuffman,fuente,Huffmanval,bitsobrantes)
print("mensaje decodificado: ",decodificado)

