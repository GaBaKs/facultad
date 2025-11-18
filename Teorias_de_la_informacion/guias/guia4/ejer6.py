from libreria import *

def rendimiento(cod,prob):
    ent=entropia(prob,len(cadcod(cod)))
    L=longitudMedia(cod,prob)
    return ent/L

def redundancia(cod,prob):
    ent=entropia(prob,len(cadcod(cod)))
    L=longitudMedia(cod,prob)
    return (L-ent)/L

cod=["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111" ]
prob=[0.25, 0.1, 0.15, 0.1, 0.04000000000000001, 0.06, 0.15, 0.06, 0.09]

print("Rendimiento: ",rendimiento(cod,prob)," Redundancia: ",redundancia(cod,prob))

