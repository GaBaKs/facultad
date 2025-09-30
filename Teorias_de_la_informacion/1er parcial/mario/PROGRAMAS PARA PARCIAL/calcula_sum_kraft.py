def creaStringCodigo (C):       
    cadena = ""
    for c in C:
        for x in c:
            if not x in cadena:
                cadena += x
    return cadena

def listaLongitudes(C):
    longitudes = []
    for c in C:
        longitudes.append(len(c))
    return longitudes

def inecuacionKraft (C):
    resultado = 0
    r = len(creaStringCodigo(C))
    longitudes = listaLongitudes(C)
    for i in range(len(C)):
        resultado += r**(-longitudes[i])
    return resultado


C = [")", "[]", "]]", "([","[()]", "([)]"]
cadena = creaStringCodigo(C)
longitudes = listaLongitudes(C)
kraft = inecuacionKraft(C)

print(cadena)   #cadena de caracteres con el alfabeto codigo
print(longitudes)  #longitudes de las palabras codigo
print(kraft)  #sumatoria de la inecuación de Kraft