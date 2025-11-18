from libreria import *




print("----- INCISO A -----")
palabra = 'ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB'
simbolos,cant=cuentasimbolos(palabra)
prob=[0.2, 0.2, 0.3, 0.3]

print("Fuente: ", simbolos)
print("Probabilidades: ", prob)

#print("Codificado de Huffman:    ", Huffman(prob))
print("Codificado de Shannon-Fano:    ", ShannonFano(prob))


print("----- INCISO B -----")
palabra = 'AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO'
simbolos,cant=cuentasimbolos(palabra)
prob=probabilidadlista(simbolos,cant)

print("Fuente: ", simbolos)
print("Probabilidades: ", prob)

#print("Codificado de Huffman:    ", Huffman(prob))
print("Codificado de Shannon-Fano:    ", ShannonFano(prob))

def calculamensaje(palabra):
    simbolos,cant=cuentasimbolos(palabra)
    prob=probabilidadlista(simbolos,cant)
    return simbolos,prob