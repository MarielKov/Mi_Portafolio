import matplotlib.pyplot as plt
import numpy as np


# Definir la funcion
def f(x):
    #ej 6
    return np.cos(x)
    #return np.sin(x)/x

# Implementando biseccion
def biseccion(a,b,ep):
    n = 1
    print('\n\n*** Implementando biseccion ***')
    condicion = True
    while condicion:
        c = (a + b)/2
        print('N-%d, C = %0.6f y f(C) = %0.6f' % (n, c, f(c)))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        n = n + 1
        condicion = abs(f(c)) > ep

    print('\n C: %0.8f' % c)


# Introducir valores
a = float(input('Numero A: '))
b = float (input('Numero B: '))
ep = float(input('Error: '))


if f(a) * f(b) > 0.0:
    print('Los valores dados no estan en el dominio')
    print('Pruebe distintos valores')
else:
    biseccion(a,b,ep)


# Valores del eje X que toma el gráfico.
cordx = np.arange(-15, 15,0.01)
# Graficar ambas funciones.

plt.plot(cordx, [f(i) for i in cordx])
# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")
# Limitar los valores de los ejes.
plt.xlim(-15, 15)
plt.ylim(-15, 15)
# Guardar gráfico como imágen PNG.
plt.savefig("output.png")
# Mostrarlo.
plt.show()