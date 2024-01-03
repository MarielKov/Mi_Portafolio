nombre = input("Nombre: ")
ventas= int(input("ventas:"))

x = (ventas*13)/100
comision = round(x,2)
print( f"Hola {nombre},su comision es de: {comision}")