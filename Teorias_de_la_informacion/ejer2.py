import random

cad="abcdeeeeee"
alfabeto= [ ]
prob=[ ]


def  generalista(alfabeto,prob,cad):
    cantidad=len(cad)
    for letra in cad:
        if letra not in alfabeto:
            alfabeto.append(letra)
            prob.append(cad.count(letra)/cantidad)
    return print(alfabeto, prob)


generalista(alfabeto,prob,cad)

#inciso b

acum= [0.5 , 0.8 , 1.0]
alf= ['a' ,'b','c']
def simulacion():
    i=0;
    cadena=''
    for cant in range(5):
        num=random.uniform(0,1)
        print("caso: ",cant,"numero random:", num)
        while num >acum[i]:
            i+=1
        cadena+=alf[i]
        i=0
    return print(cadena)

simulacion()