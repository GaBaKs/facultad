from libreria import *


cod= ["0" , "1"]
prob=[0.8 , 0.2]

def primershannon(codigos2,prob2,orden): 
    codigos,prob=calculaordenN(codigos2,prob2,orden)
    r=len(cadcod(codigos))
    ent=entropia(prob,r)
    L=longitudMedia(codigos,prob)
    print(ent/orden," <= ",L/orden," <= ",ent/orden+1/orden)

    if (ent/orden)<=L/orden and L/orden<(ent/orden+1/orden):
        return True
    else:
        return False

print(primershannon(cod,prob,1))
#def huffman():

