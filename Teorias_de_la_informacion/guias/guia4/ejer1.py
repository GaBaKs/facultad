from libreria import *


N=7
prob2=[0.3 , 0.1 , 0.4 , 0.2]
codigos2=["BA" , "CAB" , "A" , "CBA"]

def primershannon(codigos2,prob2,orden): 
    codigos,prob=calculaordenN(codigos2,prob2,orden)
    r=len(cadcod(codigos))
    ent=entropia(prob,r)
    L=longitudMedia(codigos,prob)
    print(ent," <= ",L," <= ",ent+1)

    if (ent<=L) and (L<=ent+1):
        return True
    else:
        return False

print(primershannon(codigos2,prob2,N))