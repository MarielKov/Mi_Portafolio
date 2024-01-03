from Dia1 import Funciones8


def turnos():

    print("----- Bienvenido -----\n")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmeticos\n")

        try:
            seccion = input("Elija una seccion: ").upper()
            print("\n")
            ["P", "F", "C"].index(seccion)

        except ValueError:
            print("Invalido, Vuelva a intentar\n")

        else:
            break

    Funciones8.decorador(seccion)


def empezar():

    while True:
        turnos()
        try:
            otro = input("Desea sacar otro turno? [S] [N]: ").upper()
            print("\n")
            ["S", "N"].index(otro)

        except ValueError:

            print("Invalido, Vuelva a intentar\n")

        else:

            if otro == "N":
                print("Gracias por Venir :) \n")
                break


empezar()


