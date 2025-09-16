import math

#inciso a(devuelve r)
def cadcod(C):
    cadena=''
    for cod in C:
        for x in cod:
            if not x in cadena:
                cadena+=x
    return cadena


#C = ["011","000","010","101","001","100"]   
C= ['']
print("ADS", cadcod(C))

# inciso b(devuelve l de cada codigo)

long=([len(long) for long in C])
print(long)

# inciso c(hace kraft)

r=len(cadcod(C))



def kraft(long,r):
    suma=0
    for x in long:
        suma+=pow(r,-x)
    return suma
   
print('craft1: ',kraft(long,r))

