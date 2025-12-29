
def tasa_de_compresion(mensaje: str, mensaje_codificado:bytearray):
    tam_original = len(mensaje.encode('utf-8'))
    tam_codificado = len(mensaje_codificado)
    tasa = tam_original / tam_codificado if tam_codificado != 0 else 0
    return tasa
