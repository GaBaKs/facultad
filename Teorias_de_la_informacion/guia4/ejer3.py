from libreria import *


N=2
prob2=[0.5 , 0.2 , 0.3]
codigos2=["11","010","00"]
codigos3=["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111" ]

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

print(primershannon(codigos2,prob2,1))  # esta bien
ext,extp=calculaordenN(codigos2,prob2,N)
print(primershannon(codigos3,extp,N)) ## no se si esta bien