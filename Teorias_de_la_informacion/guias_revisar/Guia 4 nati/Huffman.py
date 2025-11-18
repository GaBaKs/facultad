class Velemento:
    fuente: str
    cod: str
class Auxelem:
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
        auxelem=Auxelem()
        auxelem.prob=prob[i]
        auxelem.indices=[i]
        auxV.append(auxelem)

    auxV.sort(key=lambda x: x.prob, reverse=True)
    #print("el auxV ordenado es:",[(x.prob,x.indices) for x in auxV])
    while len(auxV)>1:
        e1=auxV.pop()
        e2=auxV.pop()
        for i in e1.indices:
            V[i].cod="0"+V[i].cod
        for i in e2.indices:
            V[i].cod="1"+V[i].cod
        
        nuevoelem=Auxelem()
        nuevoelem.prob=e1.prob+e2.prob
        nuevoelem.indices=e1.indices+e2.indices
        auxV.append(nuevoelem)
        auxV.sort(key=lambda x: x.prob, reverse=True)
        #print("el auxV ordenado es:",[(x.prob,x.indices) for x in auxV])
    print("el codigo huffman es:")
    for x in V:
        print(f"{x.fuente} : {x.cod}")
    C=[x.cod for x in V]
    return C
