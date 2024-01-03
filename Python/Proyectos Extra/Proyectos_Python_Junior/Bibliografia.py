def obtener_informacion():
    informacion = {}

    nombre = input("¿Cuál es su nombre? ")
    informacion['Nombre'] = validar_nombre(nombre)

    dia = input("¿Cuál es su dia de nacimiento? ")
    mes = input("¿Cuál es su mes de nacimiento? ")
    anio = input("¿Cuál es su año de nacimiento? ")
    informacion['Fecha de nacimiento'] = validar_fecha(dia,mes,anio)
    
    direccion = input("¿Cuál es su dirección? ")
    informacion['Dirección'] = validar_direccion(direccion)

    metas_personales = input("¿Cuáles son sus metas personales? ")
    informacion['Metas personales'] = validar_metas(metas_personales)

    return informacion


def validar_nombre(nombre):

    while not nombre.isalpha():
        print("Entrada incorrecta. Por favor, ingrese un nombre válido.\n")
        nombre = input("¿Cuál es su nombre? ")
    return nombre

def validar_fecha(dia,mes,anio):

    while not ((dia.isnumeric())or(mes.isnumeric())or(anio.isnumeric())): 
        print("Entrada incorrecta. Por favor, ingrese un nombre válido.\n")
        dia = input("¿Cuál es su dia de nacimiento? ")
        mes = input("¿Cuál es su mes de nacimiento? ")
        anio = input("¿Cuál es su año de nacimiento? ")
    fecha_nacimiento = f"{dia}/{mes}/{anio}"    
    return fecha_nacimiento

def validar_direccion(direccion):

    while not direccion.isalnum():
        print("Entrada incorrecta. Por favor, ingrese un nombre válido.\n")
        direccion = input("¿Cuál es su dirección? ")
    return direccion

def validar_metas(metas_personales):

    while not metas_personales.isalpha():
        print("Entrada incorrecta. Por favor, ingrese un nombre válido.\n")
        metas_personales = input("¿Cuáles son sus metas personales? ")
    return metas_personales

def mostrar_resumen(informacion):
    print("\nResumen de la información:")
    for clave, valor in informacion.items():
        print(f"- {clave}: {valor}")

informacion_personal = obtener_informacion()

mostrar_resumen(informacion_personal)