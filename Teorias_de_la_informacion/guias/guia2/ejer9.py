import math







def entropia(w):
        return (w*math.log2(1/w))
w=0.25
print("el valor de w es de ", w, "y la entropia es de ",entropia(w)+entropia(1-w))
w=0.75
print("el valor de w es de ", w, "y la entropia es de ",entropia(w)+entropia(1-w))
w=0.5
print("el valor de w es de ", w, "y la entropia es de ",entropia(w)+entropia(1-w))
w=0.5
print("el valor de w es de ", w, "y la entropia es de ",entropia(w)+entropia(1-w))
w=0.5
print("el valor de w es de ", w, "y la entropia es de ",entropia(w)+entropia(1-w))

