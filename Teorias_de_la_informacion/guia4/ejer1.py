from libreria import *


N=1
prob2=[0.3 , 0.1 , 0.4 , 0.2]
codigos2=["BA" , "CAB" , "A" , "CBA"]


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

print(primershannon(codigos2,prob2,N))