palabra = input("Introduce una palabra: ")

alfabeto = [] #TODOS LOS SIMBOLOS CODIGO
for letra in palabra:
    if letra not in alfabeto:
        alfabeto += letra
ListaP = [palabra.count(letra)/len(palabra) for letra in alfabeto] #CALCULA LA PROBABILIDAD DE APARICION DE UN SIMBOLO

print("SIMBOLOS DEL CODIGO:",alfabeto)
print("LISTA DE PROBABILIDADES:",ListaP)
