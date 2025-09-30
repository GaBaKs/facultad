import math

w = float(input("Ingrese un número decimal: "))

ListaP = [w, 1-w]

def generaEntropia (ListaP):
    entropia = w * math.log2(1/w) + (1-w) * math.log2(1/(1-w))
    return entropia

print(ListaP)
entropia = generaEntropia(ListaP)  
print(entropia)
