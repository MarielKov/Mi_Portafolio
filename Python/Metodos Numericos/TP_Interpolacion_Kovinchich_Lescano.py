from random import randint
from sympy import simplify, symbols, diff
import matplotlib.pyplot as plt
import numpy as np
import os

print("TP Interpolacion - Integrantes: Mariel Kovinchich y Damian Lescano\n")

print("(El programa tiene sistema de pausas por cada parte del ejercicio por temas de que se pieden datos por la longitud del mismo y no se aprecia por completo)\n")
def lista_random():

    lista = set()
    print("\nSe usa un set para impedir numeros repetidos y un ciclo que para al recopilar 20 numeros distintos en un rango de [-15,15]\n")
    while (len(lista) != 20):

        num = randint(-15,15)
        lista.add(num)
   
    return lista     

print("Se buscan los valores X e Y para la interpolacion\n")
xi = list(lista_random())
yi = list(lista_random())
xr = list(reversed(xi))
yr = list(reversed(yi))
xs = sorted(xi)
ys = sorted(yi)


print("Valores de X = ", xi)
print("Valores de Y = ", yi)
print("Valores de X invertidos = ", xr)
print("Valores de Y invertidos = ", yr)
print("Valores de X desordenados = ", xs)
print("Valores de Y desordenados = ", ys)

("\n----------------------------------------\n") 
os.system("pause")

def interpolacion_newton(x,y):
    
    print("Interpolacion de Newton\n")

    x_sym = symbols('x')
    polinomio = y[0]
    producto = 1
    n = len(x)
    i = 1

    diferencias_divididas = []
    diferencias_divididas.append(y)
    print("Se hace una lista aparte con los valores de Y para hacer los calculos\n")
    print("Se usa notacion cientifica para imprimir los resultados redondeados \n")
    for i in range(1, n):
        diferencias_divididas.append([])
        
        for j in range(n - i):
            numerador = diferencias_divididas[i - 1][j + 1] - diferencias_divididas[i - 1][j]
            denominador = x[j + i] - x[j]
            diferencias_divididas[i].append(numerador / denominador)
            print(f"Calculo: {format(diferencias_divididas[i - 1][j + 1], '.2e' )} - {format(diferencias_divididas[i - 1][j], '.2e' )} / {format(x[j + i], '.2e' )} - {format(x[j], '.2e' )} = ")
            print(f"{format(numerador, '.2e' )} / {format(denominador, '.2e')} = {format(numerador/denominador, '.2e' )} \n")

    os.system("pause")
    print("\nSe amar el polinomio usando los valores anteriormente dados y el simbolo x\n ")        
    
    for i in range(1, n):
        producto *= (x_sym - x[i - 1])
        polinomio += diferencias_divididas[i][0] * producto
         
    print("Polinomio interpolado con Newton sin simplificar: \n P(x) = " , polinomio.evalf(3))


    return polinomio

def graficar_polinomio(polinomio, x_datos, y_datos , nombre):

    
    x = np.linspace(min(x_datos), max(x_datos), 300)

    y = [polinomio.evalf(subs={'x': xi}) for xi in x]
    
    plt.plot(x_datos, y_datos, 'ro', label='Datos')
    plt.plot(x, y, label= nombre)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(nombre)
    plt.legend()
    plt.show()

def imprimir_raices(raices):
    print("(Se usa un set para evitar numeros repetidos, todos los numeros impresos deben ser distintos)")
    for raiz in raices:
         if(type(raiz) is int):
            print(f"Raíz: {raiz}") 
         elif(type(raiz) is float): 
             print(f"Raíz: {round(raiz, 5)}")
         else: 
             print(f"Raíz: {raiz.evalf(5)}")         

def obtener_raices_con_newton(polinomio ,x):

    print("Se usa Metodo de Newton para aproximar las raices del polinomio y se guardan en una lista\n")
    raices = []

    print("Metodo de Newton\n" )
    for i in x:

        raiz = metodo_newton(polinomio, derivada, i)
        if raiz is not None:
           raices.append(raiz)

    print("\nRaíces aproximadas encontradas con Metodo de Newton:\n")
    imprimir_raices(set(raices))
    

def metodo_newton(polinomio, derivada, x):
    epsilon=0.00000001
    max_iter=100
    iteracion = 0
    
    print("Calculando raices, espere.....\n")

    while abs(polinomio.subs('x', x)) > epsilon and iteracion < max_iter:

        x = x - polinomio.subs('x', x) / derivada.subs('x', x)
        iteracion += 1

    if abs(polinomio.subs('x', x)) <= epsilon:
        return x
    else:
        return None
    
def polinomio_lagrange(xi,yi):

    print("Interpolacion de Lagrange\n")
    n = len(xi)
    y_interp = []
    x_sym = symbols('x')
    p = 0
    L = 0
    for j in range(n):
        p = p + 1
        numerador = 1
        denominador = 1
        print(f"Calculo para P{p}(x):")
        for k in range(n):
            
            if k != j:
                numerador *= (x_sym - xi[k])
                denominador *= (xi[j] - xi[k])
                print(f"{yi[j]}({x_sym} - {xi[k]} /  {xi[j]} - {xi[k]})")

        print("\n----------------------------------------\n")     
        L += yi[j] * numerador / denominador
        print(f"P{p}(x)= {yi[j]}({numerador}/{denominador}) = \n {yi[j] * numerador / denominador}\n")
    
    print("Se suman los polinomios\n")
    for i in range(n):
        y_i = L.subs(x_sym, xi[i])
        y_interp.append(round(y_i, 3))
    print(f"Polinomio interpolado con Lagrange sin simplificar: \n P(x) =  {L} \n",)
    
    return  L
    
print("----------------------------------------\n") 

print("Se llama a la funcion de interpolacion de Newton\n")

print("Se hace el polinomio con los valores X e Y originales\n")
polinomio_interpolante = interpolacion_newton(xi,yi)
os.system("pause")
print("Se hace el polinomio con los valores X e Y invertidos\n")
polinomio_interpolante_invertido = interpolacion_newton(xr,yr)
os.system("pause")
print("Se hace el polinomio con los valores X e Y desordenados\n")
polinomio_interpolante_desordenado = interpolacion_newton(xs,ys)

print("\nLos polinomios resultantes son todos de grado 19\n")

print("----------------------------------------\n") 

print("Se simplifica el polinomio de Newton original, la inversa y el desordenado \n")
polinewton = simplify(polinomio_interpolante).evalf(3)
polinewtoninv = simplify(polinomio_interpolante_invertido).evalf(3)
polinewtondes= simplify(polinomio_interpolante_desordenado).evalf(3)

print("\nPolinomio interpolado con Newton simplificado: \n P(x) = ", polinewton)
print("\nPolinomio interpolado con Newton invertido simplificado: \n P(x) = ", polinewtoninv)
print("\nPolinomio interpolado con Newton desordenado simplificado: \n P(x) = ", polinewtondes)

print("\nCon el método de interpolación de Newton, el orden de los puntos X e Y no afecta al polinomio interpolante resultante ")
print("El polinomio de Newton se construye utilizando diferencias divididas que dependen únicamente de los valores de Y.")
print("Esto en el caso de invertir los datos, para los pares desordenados no se garantiza que vaya a dar el mismo polinomio. ")
print("La construcción del polinomio dependen del orden de los puntos de datos y no producirá el mismo polinomio que si se hubieran utilizado los valores de X e Y en el orden original o invertido\n")

print("----------------------------------------\n") 

print("\nSe llama a la funcion para mostrar los 3 graficos (original, invertido y desordenado)\n")
print("Espere un momento....\n")
graficar_polinomio(polinomio_interpolante, xi, yi, 'Polinomio Interpolante con Newton')
graficar_polinomio(polinomio_interpolante_invertido, xr, yr, 'Polinomio Interpolante invertido con Newton')
graficar_polinomio(polinomio_interpolante_desordenado, xs, ys, 'Polinomio Interpolante desordenado con Newton')

print("\n----------------------------------------\n") 
os.system("pause")
print("Se llama a la funcion de interpolacion de Lagrange \n")
polinomio_interpolante_lagrange = polinomio_lagrange(xi,yi)

print("\n----------------------------------------\n") 
os.system("pause")
print("Se simplifica el polinomio de Lagrange\n")
polilagrange = simplify(polinomio_interpolante_lagrange).evalf(3)

print("\nPolinomio interpolado con Lagrange simplificado: \n P(x) = ", polilagrange)



print("\n----------------------------------------\n") 
os.system("pause")
print("Se Hace la derivada para obtener las raices por Metodo de Newton\n")
derivada = diff(polinomio_interpolante)

print("\n----------------------------------------\n") 
print("Se llama a la funcion del metodo de Newton para obtener las raices\n")
obtener_raices_con_newton(polinomio_interpolante, xi)











