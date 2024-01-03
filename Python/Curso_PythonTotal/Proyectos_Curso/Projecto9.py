import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

hoy = datetime.date.today()

ruta = Path(Path.home(), "Desktop", "Python", "Mi_Gran_Directorio")
mi_patron = r'N\D{3}-\d{5}'

listanum = []

encontrados = []

def numeros(archivo, patron):

    archivo2 = open(archivo, 'r')
    texto = archivo2.read()

    if re.search(patron, texto):

        return re.search(patron, texto)

    else:
        return ' '

def listas(ruta):

    for carpeta, subcarpeta, archivo in os.walk(ruta):

        for a in archivo:
            resultado = numeros(Path(carpeta,a), mi_patron)

            if resultado != ' ':

                listanum.append((resultado.group()))
                encontrados.append(a.title())

def menu():

    indice = 0
    print("--------------------------")

    print(f'Fecha: {hoy.day}/{hoy.month}/{hoy.year}')
    print("\n")

    print('ARCHIVO\t\t\tNRO. SERIE')
    print("--------------------------")

    for a in encontrados:

        print(f"{a}\t{listanum[indice]}")
        indice += 1

    print("\n")
    print(f"Números encotrados: {len(listanum)}")
    print("--------------------------")

listas(ruta)
menu()

fin = time.time()
duracion = fin - inicio

print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")