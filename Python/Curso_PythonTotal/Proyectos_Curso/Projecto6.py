from pathlib import *
from os import *
import os

ruta = Path(Path.home(), "Desktop", "Python", "../Recetas")
def contador(ruta):

    i = 0
    for txt in Path(ruta).glob("**/*.txt"):

        i += 1
    return i

#def agregar_receta(ruta):

def menu():
    system('cls')
    print("----- Bienvenido a Mi recetario -----\n")

    print(f"Las recetas se encuentran en {ruta}")
    print(f"Total recetas: {contador(ruta)}")

    clave = " "

    while not clave.isnumeric() or int(clave) not in range(1,7):

        print("[1] - Leer receta\n[2] - Crear receta nueva\n[3] - Crear categoria nueva\n[4] - Eliminar receta\n[5] - Eliminar categoria\n[6] - Salir del programa\n")
        clave =input("Elija una opcion: ")

    return int(clave)

def categorias(ruta):

    print("----- CATEGORIAS -----\n")

    ruta_cat = Path(ruta)
    listaC = []
    i = 1

    for c in ruta_cat.iterdir():
        cat = str(c.name)
        print(f"[{i}] - {cat}")
        listaC.append(c)
        i += 1

    return listaC

def elegir_categoria(lista):
    clave = 'x'

    while not clave.isnumeric() or int(clave) not in range(1, len(lista) + 1):
        categoria = input("\nElije una categoria: ")
        listaC2 = lista[int(categoria) - 1]

    return listaC2

def recetas(ruta):

    print("----- RECETAS -----\n")

    ruta_rec = Path(ruta)
    listaR = []
    i = 1

    for r in ruta_rec.glob('*.txt'):
        r_str = str(r.name)
        print(f"[{i}] - {r_str}")
        listaR.append(r)
        i += 1

    return listaR

def elegir_recetas(lista):
    clave = " "

    while not clave.isnumeric() or int(clave) not in range(1, len(lista) + 1):
        receta = input("\nElija una receta: ")
        listaR2 = lista[int(receta) - 1]

    return listaR2


def crear_receta(ruta):

    valido = False

    while not valido:

        print("Escriba un nombre para su receta: \n")
        nombre = input() + '.txt'
        print("Escriba su nueva receta: \n")
        contenido = input()
        nuevaruta = Path(ruta, nombre)

        if not os.path.exists(nuevaruta):
            Path.write_text(nuevaruta, contenido)
            print(f"Tu receta {nombre} ha sido creada")
            valido = True
        else:
            print("Lo siento, esa receta ya existe")


def crear_categoria(ruta):
    valido = False

    while not valido:
        print("Escribe el nombre de la nueva categoria: \n")
        nombre = input()
        nuevaruta = Path(ruta, nombre)

        if not os.path.exists(nuevaruta):
            Path.mkdir(nuevaruta)
            print(f"Tu nueva categoria {nombre} ha sido creada")
            valido = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(F"La categoria {categoria.name} ha sido eliminada")


def atras():
    volver = " "

    while volver.lower() != 'v':
        volver = input("\nPresione V para volver al menu: ")



final = False

while not final:

    opc = menu()

    if opc == 1:

        listaC = categorias(ruta)
        listaC2 = elegir_categoria(listaC)
        listaR = recetas(listaC2)
        listaR2 = elegir_recetas(listaR)
        print(Path.read_text(listaR2))
        atras()

    elif opc == 2:

        listaC = categorias(ruta)
        listaC2 = elegir_categoria(listaC)
        crear_receta(listaC2)
        atras()

    elif opc == 3:

        crear_categoria(ruta)
        atras()

    elif opc == 4:

        listaC = categorias(ruta)
        listaC2 = elegir_categoria(listaC)
        listaR = recetas(listaC2)
        listaR2 = elegir_recetas(listaR)
        Path(listaR2).unlink()
        print(f"La receta {listaR2.name} ha sido eliminada")
        atras()

    elif opc == 5:
        listaC = categorias(ruta)
        listaC2 = elegir_categoria(listaC)
        Path(listaC2).rmdir()
        print(F"La categoria {listaC2.name} ha sido eliminada")
        atras()

    elif opc == 6:
        final = True