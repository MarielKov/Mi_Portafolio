class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre del cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.num_cuenta}: ${self.balance}"

    def deposito(self, depositar):
        self.balance += depositar
        print("Deposito aceptado")

    def retiro(self, retirar):
        if self.balance >= retirar:
            self.balance -= retirar
            print("Retiro Exitoso\n ")
        else:
            print("Fondo insuficiente\n")


def crear_cliente():
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    num_cuenta = input("Ingresar numero de cuenta: ")
    cliente = Cliente(nombre, apellido, num_cuenta)
    return cliente


def inicio():
    cliente = crear_cliente()
    print(cliente)
    opcion = 0

    while (opcion != 'S') and (opcion != 's'):

        opcion = input("Elije: Depositar (D), Retirar (R), o Salir (S)\n")

        if opcion == 'D' or opcion == 'd':
            depositar = int(input("Monto a depositar: "))
            cliente.deposito(depositar)
        elif opcion == 'R'or opcion == 'r':
            retirar = int(input("Monto a retirar: "))
            cliente.retiro(retirar)
        print(cliente)

    print("Nos vemos\n")


inicio()



