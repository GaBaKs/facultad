
def asigna_paridad(car):
    """Recibe un caracter y devuelve su valor ASCII con bit de paridad par."""
    valor_ascii = ord(car)
    num_unos = bin(valor_ascii).count('1')
    if num_unos % 2 == 0:
        return valor_ascii << 1  # Desplazar a la izquierda y agregar 0
    else:
        return (valor_ascii << 1) | 1  # Desplazar a la izquierda y agregar 1

def verifica_bit_paridad(valor):
    """Recibe un valor entero y verifica su bit de paridad.
    Devuelve True si la paridad es correcta (par), False si es incorrecta (impar)."""
    num_unos= valor & 0b11111110 #quito el ultimo bit que es el de paridad
    num_unos = bin(num_unos).count('1')
    return num_unos % 2 == 0 and (valor & 0b00000001) == 0 or num_unos % 2 == 1 and (valor & 0b00000001) == 1

"""car='C'
valor_con_paridad = asigna_paridad(car)
print(f"El valor ASCII de '{car}' con bit de paridad es: {valor_con_paridad} (binario: {bin(valor_con_paridad)})")
es_paridad_correcta = verifica_bit_paridad(valor_con_paridad)   
print(f"EL bi de la paridad es correcta?: {es_paridad_correcta}")"""
