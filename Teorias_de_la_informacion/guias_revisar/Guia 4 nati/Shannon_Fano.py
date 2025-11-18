class Velemento:
    fuente: str
    cod: str

class SAuxelem:
    prob: float
    indice: int


def Shannon_Fano_rec(V, auxV):
    if len(auxV) == 1:
        return
    else:
        #print("el auxV ordenado parcial es:", [(x.prob, x.indice) for x in auxV])

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


def shannon_fano(prob, alf):
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
    C = [x.cod for x in V]
    return C

"""# Ejemplo de uso
alf = ["A", "B", "C", "D"]
prob = [0.4, 0.25, 0.25, 0.1]
shannon_fano(prob, alf)"""
