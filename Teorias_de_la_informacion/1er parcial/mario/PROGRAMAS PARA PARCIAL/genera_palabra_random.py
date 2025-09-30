import random

def probabilidad_acumulada(probabilidades):
    acumuladas = []
    suma = 0
    for p in probabilidades:
        suma += p
        acumuladas.append(suma)
    return acumuladas

n = int(input("Ingrese cantidad de simbolos "))

alfabeto = ['a', 'b', 'c', "d", "e"]
prob = [0.15, 0.20, 0.25, 0.05, 0.40]
probAc = probabilidad_acumulada(prob)

palabra = []
for x in range(0,n):
    num = random.uniform(0,1)
    print(num)
    i = 0
    while probAc[i] < num:
        i+=1
    palabra += alfabeto[i]

print(palabra)