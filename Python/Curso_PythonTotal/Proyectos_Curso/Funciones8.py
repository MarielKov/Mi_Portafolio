def num_perfumeria():
    for n in range(1, 100):
        yield f"Perfumeria - {n}"


def num_farmacia():
    for n in range(1, 100):
        yield f"Farmacia - {n}"


def num_cosmeticos():
    for n in range(1, 100):
        yield f"Cosmeticos - {n}"


p = num_perfumeria()
f = num_farmacia()
c = num_cosmeticos()


def decorador(seccion):

    print("-------------------")
    print("Su número es: ")

    if seccion == "P":
        print(next(p))

    elif seccion == "F":
        print(next(f))

    else:
        print(next(c))

    print("Espere su turno")

