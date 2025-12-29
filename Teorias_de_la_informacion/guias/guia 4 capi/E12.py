import math

def Entropia(prob,r):
    E=0 
    I=[math.log(1/X, r) for X in prob ]
    #print("el I",I)
    for a in range(len(prob)) :
        E+= (prob[a]*I[a])
    return E

class Velemento:
    fuente: str
    cod: str
class HAuxelem:
    prob:float
    indices: list[int]
def huffman(prob,alf):
    V=[]
    for i in range(len(alf)):
        elem=Velemento()
        elem.fuente=alf[i]
        elem.cod=""
        V.append(elem)
    auxV=[]
    for i in range(len(prob)):
        Hauxelem=HAuxelem()
        Hauxelem.prob=prob[i]
        Hauxelem.indices=[i]
        auxV.append(Hauxelem)

    auxV.sort(key=lambda x: x.prob, reverse=True)
    #print("el auxV ordenado es:",[(x.prob,x.indices) for x in auxV])
    while len(auxV)>1:
        e1=auxV.pop()
        e2=auxV.pop()
        for i in e1.indices:
            V[i].cod="0"+V[i].cod
        for i in e2.indices:
            V[i].cod="1"+V[i].cod
        
        nuevoelem=HAuxelem()
        nuevoelem.prob=e1.prob+e2.prob
        nuevoelem.indices=e1.indices+e2.indices
        auxV.append(nuevoelem)
        auxV.sort(key=lambda x: x.prob, reverse=True)
      #  print("el auxV ordenado es:",[(x.prob,x.indices) for x in auxV])
    print("el codigo huffman es:")
    for x in V:
        print(f"{x.fuente} : {x.cod}")
    C=[x.cod for x in V]
    return C
    

class SAuxelem:
    prob: float
    indice: int


def Shannon_Fano_rec(V, auxV):
    if len(auxV) == 1:
        return
    else:
       # print("el auxV ordenado parcial es:", [(x.prob, x.indice) for x in auxV])

        # Buscar el punto donde las sumas de prob se equilibran más
        total = sum(x.prob for x in auxV)
        acum = 0
        min_dif = float('inf')
        corte = 0

        for i in range(len(auxV) - 1):
            acum += auxV[i].prob
            dif = abs(acum - (total - acum))
            if dif < min_dif:
                min_dif = dif
                corte = i + 1  # el corte es después del i-ésimo

        # Asignar los bits 0 / 1 según el grupo
        for i in range(corte):
            V[auxV[i].indice].cod += "0"
        for i in range(corte, len(auxV)):
            V[auxV[i].indice].cod += "1"

        # Llamadas recursivas sobre cada grupo
        Shannon_Fano_rec(V, auxV[:corte])
        Shannon_Fano_rec(V, auxV[corte:])


def Shannon_Fano(prob, alf):
    V = []
    for i in range(len(alf)):
        elem = Velemento()
        elem.fuente = alf[i]
        elem.cod = ""
        V.append(elem)

    auxV = []
    for i in range(len(prob)):
        Sauxelem = SAuxelem()
        Sauxelem.prob = prob[i]
        Sauxelem.indice = i
        auxV.append(Sauxelem)

    auxV.sort(key=lambda x: x.prob, reverse=True)
    Shannon_Fano_rec(V, auxV)

    print("El código Shannon–Fano final es:")
    for x in V:
        print(f"{x.fuente} : {x.cod}")
    C=[x.cod for x in V]
    return C

def alfCod(cod):
    aux=set()    
    for x in cod:
        for y in x:
            if y not in aux:
                aux.add(y)
    #print("el alfabeto codigo es:",aux)
    return aux 

def longCod(cod):
    return [len(c) for c in cod ]

def longMedia(prob,cod):
    suma=0
    for x in range(len(cod)):
        suma+= prob[x] *cod[x]
    return suma

def rendimiento(prob,cod):
    
    H=Entropia(prob,len(alfCod(cod)))
    L=longMedia(prob,longCod(cod))
    if L!=0:
        nn=H/L
        R=1-nn
    else:
        nn=0
        R=1
    return nn,R

alf=["A","B","C","D","E"]
prob=[0.385,0.154,0.128,0.154,0.179]
print("la entropia es:",Entropia(prob,2))
Huff=huffman(prob,alf)
Shann=Shannon_Fano(prob,alf)
print("la longitud media del codigo huffman es:",longMedia(prob,longCod(Huff)))
print("la longitud media del codigo shannon es:",longMedia(prob,longCod(Shann)))
print("el rendimiento y la redundancia del codigo huffman es: ",rendimiento(prob,Huff))
print("el rendimiento y la redundancia del codigo shannon es: ",rendimiento(prob,Shann))
