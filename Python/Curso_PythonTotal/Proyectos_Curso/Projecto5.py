from random import *

listap = ["otorrinonaringologo", "programador", "farmaceutico", "oxitocina"]
listacorrecto = []
listausado = []

intentos = 6
aciertos = 0

print("Bienvenido al Ahorcado")

def azarpalabra(listap):

    palabra = choice(listap)
    palabra2 = set(palabra)
    setp2 = len(palabra2)

    return setp2, palabra

def guiones_letras(palabra, listacorrecto):
    listag = []
    for n in palabra:
       if n in listacorrecto:
           listag.append(n)
       else:
           listag.append("-")
    print(" ".join(listag))

def pedir():
    letra = " "
    abc = "abcdefghijklmnñopqrstuvwxyz"
    vof = False

    while not vof:
        letra = input("Su letra: ")
        if letra in abc and len(letra)==1:
            vof = True
        else:
            print("Letra incorrecta")

    return letra

def correcionletra(letra, setp2, palabra, intentos, aciertos, listacorrecto,listausado):
    finalizar = False

    if letra in palabra and letra not in listacorrecto:
        listacorrecto.append(letra)
        aciertos += 1
    elif letra in palabra and letra in listacorrecto:
        print("Ya uso esta letra")
    else:
        listausado.append(letra)
        intentos -= 1

    if intentos == 0:
        finalizar = True
        print(f"Perdiste. La palabra era {palabra}")
    elif aciertos == setp2:

        print("Felicidades. Has ganado")
        finalizar = True

    return finalizar, aciertos, intentos

setp2 ,palabra = azarpalabra(listap)
finalizar = False
while not finalizar:
    print('\n' + '*' * 20 + '\n')
    guiones_letras(palabra, listacorrecto)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(listausado))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir()

    finalizar, aciertos, intentos = correcionletra(letra,setp2,palabra,intentos,aciertos, listacorrecto, listausado)


