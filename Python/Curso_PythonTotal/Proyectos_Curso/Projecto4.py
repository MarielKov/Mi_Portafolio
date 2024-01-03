from random import *
repetir = "s"
intentos = 1
nombre = input(" Ingrese su nombre: ")
while (repetir=="s"):

  aleatorio = randint(1,100)
  print(f"Hola {nombre}, te reto a adivinar que numero he generado, tienes 8 intentos")

  while(intentos<8):

    numero = int(input("Ingresa un numero: "))
    if (aleatorio>numero):
        print("Muy chico, otra vez")
        intentos += 1
    elif (aleatorio<numero):
        print("Muy grande, otra vez")
        intentos += 1
    elif(aleatorio>100 or aleatorio<1):
        print("Fuera de rango, otra vez")
        intentos += 1
    else:
        print(f"Felicidades, Acertaste al {intentos} intento")
        break
  repetir = input("Se acabaron los intentos, quieres repetir? (s/n): ")
  if (repetir!="s"):
      print("Nos vemos :)")
  else:
      intentos = 0