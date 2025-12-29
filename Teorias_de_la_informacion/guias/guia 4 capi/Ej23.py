from Dist_Hamming import hamming_completo
cod1=["0100100","0101000","0010010","0100000"]
cod2=["0100100","0010010","0101000","0100001"]
cod3=["0110000","0000011","0101101","0100110"]
dist,errores_detectables,errores_corregibles=hamming_completo(cod1)
print("La distancia mininima del cod 1 es:",dist)
print("Cantidad de errores detectables y corregibles del cod 1:",errores_detectables,errores_corregibles,"\n")

dist,errores_detectables,errores_corregibles=hamming_completo(cod2)
print("La distancia mininima del cod 2 es:",dist)
print("Cantidad de errores detectables y corregibles del cod 2:",errores_detectables,errores_corregibles,"\n")

dist,errores_detectables,errores_corregibles=hamming_completo(cod3)
print("La distancia mininima del cod 3 es:",dist)
print("Cantidad de errores detectables y corregibles del cod 3:",errores_detectables,errores_corregibles,"\n")