
def tomar_numero():
    num = int(input("Ingrese un numero:  "))
    return num

def comprobar():

    letra = input("Desea probar otro numero? (Y/N) :  ")

    if((letra == "y") or (letra == "Y") ):
        num = tomar_numero()
        par_o_impar(num)
        
    elif((letra == "n") or (letra == "N")):
        print("Gracias por probar nuestro servicio\n")

    else:
        print("Entrada no valida, intente de nuevo\n")  
        comprobar()

def par_o_impar(num):
    if(num % 2 == 0):

        print(f"Su numero es el {num} y es par\n")
        comprobar()
    

    else: 
        print(f"Su numero es el {num} y es impar\n")
        comprobar()

num = tomar_numero()

par_o_impar(num)
