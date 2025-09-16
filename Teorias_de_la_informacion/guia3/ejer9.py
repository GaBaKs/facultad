import math

#inciso a(devuelve r)
def cadcod(C):
    cadena=''
    for cod in C:
        for x in cod:
            if not x in cadena:
                cadena+=x
    return cadena


C = ["011","00","010","101","001","100"]   

print("ADS", cadcod(C))



# inciso b(devuelve l de cada codigo)

long=([len(long) for long in C])
print(long)

# inciso c(hace kraft)
r=len(cadcod)



def kraft(C,r):
   for x in long
        suma+=r**-x
    return suma