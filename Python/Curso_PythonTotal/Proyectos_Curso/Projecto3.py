frase = input("Escriba aqui: ")
lista_letras = []

frase = frase.lower()

lista_letras.append(input("Ingrese primera letra: ".lower()))
lista_letras.append(input("Ingrese segunda letra: ".lower()))
lista_letras.append(input("Ingrese tercera letra: ".lower()))

print("\nCantidad de letras\n".center(3))

letra1 = frase.count(lista_letras[0])
letra2 = frase.count(lista_letras[1])
letra3 = frase.count(lista_letras[2])

print(f"En esta frase hay:\n {letra1} letras {lista_letras[0]}\n {letra2} letras {lista_letras[1]}\n {letra3} letras {lista_letras[2]}")

print("\nCantidad de palabras\n".center(3))

palabras = frase.split()
print(f"{len(palabras)} palabras")

print("\nInicio/Final\n".center(3))

inicio = frase[0].upper()
final = frase[-1].upper()
print(f"Letra inicial: {inicio} Letra final: {final}")

print("\nAl reves\n".center(3))

palabras.reverse()
reves = ' '.join(palabras)
print(f"Texto al revés: {reves}")

print("\nBuscar Python\n".center(3))

python = 'python' in frase
dic = {True:"sí", False:"no"}
print(f"Existe la palabra 'Python' en: {dic[python]} ")

