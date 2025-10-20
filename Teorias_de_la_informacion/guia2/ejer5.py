import math




def generalistainfoN(listap,base):
    return [math.log(1/prob,base) for prob in listap]

def entropia(listap,base):
        entropia=0
        informacion=generalistainfoN(listap,base)
        for i in listap:
            entropia+=i*informacion[listap.index(i)]
        return entropia


def cuentasimbolos(palabra,simbolos,cant):
   for i in palabra:
          if i in simbolos:
               cant[simbolos.index(i)]+=1
          else:
              simbolos.append(i)
              cant.append(1)

def probabilidadlista(simbolos,cant):
     listaprob=[]
     total=sum(cant)
     
     for i in simbolos:
        listaprob.append(cant[simbolos.index(i)]/total)
     return listaprob

abecedario="ABDAACAABACADAABDAADABDAAABDCDCDCDC"
simbolos2=[]
cant2=[]
cuentasimbolos(abecedario,simbolos2,cant2)
print("Todos los simbolos son ",simbolos2, "y la cant de aparicion de cada uno es",cant2)



print("la probabilidad de cada elemento es de ",probabilidadlista(simbolos2,cant2))