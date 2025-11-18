


def esNoSingular (C):
    n = len(C)
    for i in range(n):
        for j in range(n):
            if (i != j):
                if (C[i] == C[j]):
                    return False                    #preguntar si rompe la programacion estructurada
    return True


def esInstantaneo (C):
    if esNoSingular(C) == False:
        return False
    else:
        n = len(C)
        for i in range(n):
            for j in range(n):
                if (i != j):
                    if C[i].startswith(C[j]):
                        return False
        return True


def esUnivoco (C):
    if esInstantaneo(C) == True:
        return True
    else: 
        S = C
        ST = []
        while True:
            aux = []
            for x in S:
                for y in C:
                    if x != y: 
                        if x.startswith(y):
                            diferencia = x[len(y):]
                            if diferencia not in aux:
                                aux.append(diferencia)
                        else:
                            if y.startswith(x):
                                diferencia = y[len(x):]
                                if diferencia not in aux:
                                  aux.append(diferencia)
            ST.append(S)
            S = aux
            if all(x not in C for x in S) and (S not in ST):
                continue
            else:
                break
        if (S in ST):
            return True
        else: 
            return False






C = ['011','000','010','101','001','100']

print(esNoSingular(C))
print(esInstantaneo(C))
print(esUnivoco(C))