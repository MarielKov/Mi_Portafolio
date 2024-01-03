
def contar_palabras(texto):
    palabras = texto.split()
    cantidad = len(palabras)
    return cantidad

texto = input("Introduzca un texto:  ")
resultado = contar_palabras(texto)
print(f"Este texto tiene una cantidad de {resultado} palabras\n")