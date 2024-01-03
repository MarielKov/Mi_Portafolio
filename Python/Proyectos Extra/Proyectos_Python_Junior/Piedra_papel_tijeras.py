import random

print("Piedra, papel o tijeras\n")

def elegir():

    eleccion = int(input("Juguemos piedra, papel o tijeras, ¿cual es su eleccion?:\n 0- Piedra / 1- Papel / 2- Tijeras :  "))
    print("\n")
    listaJuego = ["Piedra", "Papel", "Tijeras"]
    eleccionCPU = random.choice(listaJuego)

    if((eleccion >= 0) and (eleccion <= 2)):
       return eleccion,eleccionCPU,listaJuego
    else:
        print("Valor no valido, Vuelva a intentar\n")
        return elegir()


puntosCPU = 0
puntosUsuario = 0
rondas = 1

while((puntosCPU != 5) and (puntosUsuario != 5)):


    eleccion, eleccionCPU, listaJuego = elegir()

    if(eleccionCPU == listaJuego[eleccion]):

        print("Es un empate, No suma puntos\n")

    elif((eleccionCPU == "Piedra")):
        if(eleccion == 1):
            print(f"CPU : {eleccionCPU} - {listaJuego[eleccion]} : Tu\n")
            puntosUsuario += 1
            print(f"Usted gana la ronda {rondas}\n Puntuacion:\n Tu: {puntosUsuario}\n CPU: {puntosCPU} \n")
            rondas += 1
        
        else:
            print(f"CPU : {eleccionCPU} - {listaJuego[eleccion]} : Tu\n")
            puntosCPU += 1
            print(f"El CPU gana la ronda {rondas}\n Puntuacion:\n Tu: {puntosUsuario}\n CPU: {puntosCPU} \n")
            rondas += 1

    elif((eleccionCPU == "Papel")):
        if(eleccion == 2):
            print(f"CPU : {eleccionCPU} - {listaJuego[eleccion]} : Tu\n")
            puntosUsuario += 1
            print(f"Usted gana la ronda {rondas}\n Puntuacion:\n Tu: {puntosUsuario}\n CPU: {puntosCPU} \n")
            rondas += 1
        
        else:
            print(f"CPU : {eleccionCPU} - {listaJuego[eleccion]} : Tu\n")
            puntosCPU += 1
            print(f"El CPU gana la ronda {rondas}\n Puntuacion:\n Tu: {puntosUsuario}\n CPU: {puntosCPU} \n")
            rondas += 1
    else:
    
        if(eleccion == 0):
            print(f"CPU : {eleccionCPU} - {listaJuego[eleccion]} : Tu\n")
            puntosUsuario += 1
            print(f"Usted gana la ronda {rondas}\n Puntuacion:\n Tu: {puntosUsuario}\n CPU: {puntosCPU} \n")
            rondas += 1
        
        else:
            print(f"CPU : {eleccionCPU} - {listaJuego[eleccion]} : Tu\n")
            puntosCPU += 1
            print(f"El CPU gana la ronda {rondas}\n Puntuacion:\n Tu: {puntosUsuario}\n CPU: {puntosCPU} \n")
            rondas += 1   

if(puntosUsuario == 5):
    print("Felicidades, ha ganado el juego!!!")

elif(puntosCPU == 5):
    print("La CPU gana. Suerte la proxima :)")