import math
from libreria import *

#codigo = [")", "[]", "]]", "([","[()]", "([)]"]
codigo= [".,", ";", ",,", ":","...",",:;"]
prob = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]



if esCompacto(codigo,prob):
    print("es compacto")
else:
    print("no es compacto")