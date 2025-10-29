from libreria import *

def rendimiento(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return ent/L

def redundancia(cod,prob):
    ent=entropia(prob,2)
    L=longitudMedia(cod,prob)
    return (L-ent)/L

cod=["11" , "010" , "00"]
prob=[0.5 , 0.2 , 0.3]

print("Rendimiento: ",rendimiento(cod,prob)," Redundancia: ",redundancia(cod,prob))

