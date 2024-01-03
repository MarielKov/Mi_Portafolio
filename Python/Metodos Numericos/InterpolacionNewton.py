# Polinomio interpolación
# Diferencias Divididas de Newton
# Tarea: Verificar tamaño de vectores,
#        verificar puntos equidistantes en x

# INGRESO , Datos de prueba
from random import randint
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

print("TP Interseccion - Integrantes: Mariel Kovinchich, Damian Lescano")
def lista_random():

    lista = set()
    print("Se usa un set para impedir numeros repetidos y un ciclo que para al recopilar 20 numeros distintos")
    while (len(lista) != 20):

        num = randint(-10,10)
        lista.add(num)
   
    return lista    

print("Se recopilan los datos aleatoriamente para x e y")
xi = list(lista_random())
yi = list(lista_random())

print(xi)
print(yi)

# PROCEDIMIENTO
def coeficientes_diferencias_divididas(x, y):
    n = len(x)
    coeficientes = [y[0]]
    for i in range(1, n):
        coef = y[i]
        print("Iteracion = ", i)
        for j in range(i):
            print("xi = ",x[i])
            print("xj = ",x[j])
            print("(",coef ," - " , coeficientes[j], " / ", {x[i]}, "-" ,{x[j]})
            coef = (coef - coeficientes[j]) / (x[i] - x[j])
            print(" = ", round(coef,3) )

        coeficientes.append(coef)
        
    return coeficientes

def interpolacion_newton(x, y, valor):
    coeficientes = coeficientes_diferencias_divididas(x, y)
    n = len(x)
    polinomio = []
    polinomio_str = ''
    for i in range(n):
        termino = str(coeficientes[i])
        for j in range(i):
            termino += f' * (x - {x[j]})'
        polinomio.append(termino)
        if i > 0:
            polinomio_str += ' + '
        polinomio_str += termino
    return polinomio, polinomio_str, coeficientes


def evaluar_polinomio(coeficientes, x):
    n = len(coeficientes)
    resultado = coeficientes[n-1]
    for i in range(n-2, -1, -1):
        resultado = resultado * (x - x[i]) + coeficientes[i]
    return resultado

# Ejemplo de uso
valor = 5
polinomio, polinomio_str, coeficientes = interpolacion_newton(xi, yi, valor)

polinomio_simplificado = sym.simplify(polinomio)

pol = np.polyfit(xi,yi,len(xi)-1)  # coeficientes del polinomio

xx = np.linspace(min(xi),max(xi))
yy = np.polyval(pol,xx)


n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)

for i in range(0,n,1):
    
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*yi[i]

    divisorL[i] = denominador

# simplifica el polinomio
polilagrange = polinomio.expand()

polinomio_lagrange = sym.simplify(polilagrange)

pxl = sym.lambdify(x,polilagrange)


muestras = 100
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = pxl(pxi)


# Graficar los puntos de datos y el polinomio de interpolación
plt.plot(xx, yy, '-',xi, yi, 'ro')
plt.axis([min(xx)-1, max(xx)+1, min(yy)-1, max(yy)+1]);

#plt.scatter(xi, yi, color='red', label='Datos')
#plt.plot(pxi, pfi, label='Polinomio de interpolación')
#plt.scatter(valor, resultado, color='green', label='Valor evaluado')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Newton')
plt.show()

#print(f"El resultado de evaluar el polinomio en x = {valor} es: {round(resultado, 3)}\n")

print("Polinomio con Lagrange: ", polinomio_lagrange)

coeficientes_polinomio = [coeficientes[-1]]
for i in range(len(coeficientes)-2, -1, -1):
    coeficientes_polinomio.insert(0, coeficientes[i] - coeficientes_polinomio[0] * xi[i])

raices = np.roots(coeficientes_polinomio)    

# Imprimir el polinomio completo y las raíces
print('Polinomio de interpolación de Newton:')
print(f'P(x) = {polinomio_str}')
print('Raíces del polinomio:')
for raiz in raices:
    print(f'x = {raiz.round(3)}')