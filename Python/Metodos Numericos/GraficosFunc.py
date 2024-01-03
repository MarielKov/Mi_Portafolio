import matplotlib.pyplot as plt
import numpy as np
import math

ep = 0.001

xn = 1
n = 0
dif = 100

# Función cuadrática.
def f1(x):
    
    #return x**n
    #return np.log(x)
    #return np.sqrt(x)
    #return np.cos(x)
    #return 1/x
    return np.sin(x)/x

print(f1(xn))

# Función lineal.
def f2(x):
    #return n*x**(n-1)
    #return 1/x
    #return 1/(2*(np.sqrt(x)))
    #return -(np.sin(x))
    #return 1/(x**2)
    return (np.cos(x)/x-(np.sin(x)/x**2))

print(f2(xn))

def newton(x):

     return x - f1(x)/f2(x)
    



while (dif > ep):
   
    xn = newton(xn)
    dif = np.abs(xn - newton(xn))
    n += 1
    print("xn: ", xn)
    print("dif: ", dif)
    print("n: ", n)
    print("---------------------")


print("\n El resultado es: ", xn)

# Valores del eje X que toma el gráfico.
cordx = np.arange(-15, 15,0.01)
# Graficar ambas funciones.

plt.plot(cordx, [f1(i) for i in cordx])
plt.plot(cordx, [f2(i) for i in cordx])
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

