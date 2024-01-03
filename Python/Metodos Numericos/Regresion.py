import math
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

print("TP Cuadrados minimos y regresion lineal\n")
print("Integrantes: Mariel Kovinchich, Damian Lescano\n")

print("Se lee el archivo Excel usando la libreria pandas\n")
df = pd.read_excel('ACUMULADOS vs DIAS.xlsx', sheet_name='Hoja1', header=None, skiprows=4)

print("Se obtienen los titulos de las columnas\n")
titulo_x = df.iloc[0, 2]  
titulo_y = df.iloc[0, 3]  

print("Se obtienen los datos de las columnas\n")
datos_x = df.iloc[5:, 2].values.astype(float)  
datos_y = df.iloc[5:, 3].values.astype(float)  

def coeficiente_de_correlacion(x,y):

    print("Se calcula la media de los datos x e y\n")
    media_x = np.mean(x)
    media_y = np.mean(y)

    print("Se calcula la suma de los productos de las desviaciones\n")
    suma_productos_desviaciones = np.sum((x - media_x) * (y - media_y))

    print("Se calculan las sumas de los cuadrados de las desviaciones x e y \n")
    suma_cuadrados_desviaciones_x = np.sum((x - media_x) ** 2)
    suma_cuadrados_desviaciones_y = np.sum((y - media_y) ** 2)

    print("Se calcula el coeficiente de correlación\n")
    corr_coef = suma_productos_desviaciones / np.sqrt(suma_cuadrados_desviaciones_x * suma_cuadrados_desviaciones_y)

    return corr_coef

print("Se hacen las funciones y sus derivadas primera y segunda\n")

def funcion_lineal(a,b,x):
    return a*x+b

def derivada_lineal_primera(a):
    return a

def derivada_lineal_segunda():
    return 0

def funcion_potencial(a, b, x):
    return b* x**a

def derivada_primera_potencial(a, b, x):
    
    return a*b*x**(a-1)

def derivada_segunda_potencial(a, b, x):
    return (a-1)*a*b*x**(a-2)

def funcion_exponencial(a, b, x):
    return b *math.exp(a * x)

def derivada_primera_exponencial(a, b, x):
    return a*b * math.exp(a * x)

def derivada_segunda_exponencial(a, b, x):
    return (a**2)*b*math.exp(a * x)


def cuadrados_minimos(x, y):

    n = len(x)

    print("Se calculan las sumas de los productos\n")

    sum_x = x.sum()
    sum_y = y.sum()
    sum_xy = (x * y).sum()
    sum_x2 = (x * x).sum()

    print("Se calcula la pendiente y la intersección\n")

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    b = (sum_y - a * sum_x) / n

    return a, b

def calcular_funciones(a,b,ap,bp,ae,be,x):

    print("En estas listas se guardaran los valores y de los calculos de las derivadas\n ")
    y_lineal = []
    y_primera_lineal = []
    y_segunda_lineal = []

    y_potencial = []
    y_primera_potencial = []
    y_segunda_potencial = []

    y_exponencial = []
    y_primera_exponencial = []
    y_segunda_exponencial = []

    print("Se usan los primeros 10 valores de x para calcular las funciones, esto para mejorar los graficos de las derivadas\n")
    for i in x[:10]:

        y_lineal.append(funcion_lineal(a,b,i))
        y_primera_lineal.append(derivada_lineal_primera(a))
        y_segunda_lineal.append(derivada_lineal_segunda())

        y_potencial.append(funcion_potencial(ap,bp,i))
        y_primera_potencial.append(derivada_primera_potencial(ap,bp,i))
        y_segunda_potencial.append(derivada_segunda_potencial(ap,bp,i))

        y_exponencial.append(funcion_exponencial(ae,be,i))
        y_primera_exponencial.append(derivada_primera_exponencial(ae,be,i))
        y_segunda_exponencial.append(derivada_segunda_exponencial(ae,be,i))

    print("Al terminar se devuelven los valores de y\n")
    return  (y_lineal,y_primera_lineal,
             y_segunda_lineal,y_potencial,
             y_primera_potencial,y_segunda_potencial,
             y_exponencial,y_primera_exponencial,y_segunda_exponencial)

print("Se convirten los datos de x e y en un DataFrame de Pandas\n")

df = pd.DataFrame({titulo_x: datos_x, titulo_y: datos_y})

print("Se eliminan los valores nulos y se toman los datos limpios\n")
df.dropna(inplace=True)

x = df[titulo_x]
y = df[titulo_y]

print(f"X:\n{x}\n")
print(f"Y:\n{y}\n")

print("Se utiliza la funcion de cuadrados minimos\n")
a, b = cuadrados_minimos(x, y)

print("Convertimos los valores de x a un arreglo 2D para usar el metodo de regresion lineal\n")
X = x.values.reshape(-1, 1)

print("Se crea un objeto de regresión lineal y ajustarlo a los datos\n")
reg = LinearRegression()
reg.fit(X, y)

print("Tomamos la pendiente y la interseccion del objeto de regresion lineal\n")
pendiente = reg.coef_[0]
interseccion = reg.intercept_

print(f"Hecho con cuadrados minimos : y = {round(a,2)}x + {round(b,2)}")
print(f"Hecho con funciones de librerias : y = {pendiente.round(2)}x + {interseccion.round(2)}")

print("Grafico De Regresion lineal\n")
fig, ax = plt.subplots()

ax.scatter(x, y, color='blue', label='Datos')
x_line = np.linspace(min(x), max(x), 100)
y_line = reg.predict(x_line.reshape(-1, 1))

ax.plot(x_line, y_line, color='red', label='Regresión lineal')

ax.set_xlabel(titulo_x)
ax.set_ylabel(titulo_y)
ax.set_title('Regresión lineal')
ax.legend()

plt.show()

print("Hacemos logaritmo natural de todos los datos x e y para graficar la funcion potencial y exponencial\n")
ln_x = [math.log(xi) for xi in x]
ln_y = [math.log(yi) for yi in y]

ln_x2 = np.array(ln_x)
ln_y2 = np.array(ln_y)

print("Cuadrados minimos de y = bx^a\n")
ap_c, bp_c = cuadrados_minimos(ln_x2,ln_y2)

print("Se crea la funcion y = bx^a que usara el grafico y usan funciones para saber a y b\n")
coefficients = np.polyfit(ln_x, ln_y, 1)
bp = math.exp(coefficients[1])
ap = coefficients[0]

print(f"A: {round(ap,2)}")
print(f"B: {round(bp,2)}")
print(f"ln(b): {round(bp_c,2)}\n")

print(f"Hecho con cuadrados minimos : ln(y) = {round(bp_c,2)} + {round(ap_c,2)}ln(x)")
print(f"Hecho con funciones de librerias : y = {round(bp,2)}x^{round(ap,2)}\n")

x_fit = np.linspace(datos_x.min(), datos_x.max(), 100)
y_fit = [bp * xi ** ap for xi in x_fit]

plt.scatter(x, y,color='blue', label='Datos')
plt.plot(x_fit, y_fit, 'r', label='Regresión exponencial')
ax.set_xlabel(titulo_x)
ax.set_ylabel(titulo_y)
ax.set_title('Regresión polinomial')
plt.legend()
plt.show()

print("Cuadrados minimos de y = be^ax\n")
ae_c, be_c = cuadrados_minimos(datos_x,ln_y2)

print("Se crea la funcion y = be^ax que usara el grafico y usan funciones para saber a y b\n")
coefficients = np.polyfit(datos_x, ln_y, 1)
be = math.exp(coefficients[1])
ae = coefficients[0]

print(f"A: {round(ae,2)}")
print(f"B: {round(be,2)}")
print(f"ln(b): {round(be_c,2)}\n")

print(f"Hecho con cuadrados minimos : ln(y) = {round(be_c,2)} + {round(ae_c,2)}x ")
print(f"Hecho con funciones de librerias : y = {round(be,2)}e^{round(ae,2)}x\n")

print("Ajuste de datos para el grafico\n")
x_fit = np.linspace(datos_x.min(), datos_x.max(), 100)
y_fit = [be * math.e ** (ae*xi) for xi in x_fit]

plt.scatter(x, y, color='blue',label='Datos')
plt.plot(x_fit, y_fit, 'r', label='Regresión exponencial')

ax.set_xlabel(titulo_x)
ax.set_ylabel(titulo_y)
ax.set_title('Regresión exponencial')
plt.legend()
plt.show()

(y_lineal,y_primera_lineal,y_segunda_lineal,
 y_potencial,y_primera_potencial,y_segunda_potencial,
 y_exponencial,y_primera_exponencial,
 y_segunda_exponencial) = calcular_funciones(a,b,ap,bp,ae,be,datos_x)

print("Se grafican las derivadas de las funciones acotadas con los primeros 10 valores de x e y para mejor apreciacion\n")
print("Derivadas de funcion lineal\n")
fig, ax = plt.subplots()

ax.plot(x[:10], y_primera_lineal, color='blue', label='Primera derivada lineal')
ax.plot(x[:10], y_segunda_lineal, color='green', label='Segunda derivada lineal')

ax.set_xlabel(titulo_x)
ax.set_ylabel(titulo_y)
ax.set_title('Derivadas de funcion lineal')
ax.legend()

plt.show()

print("Derivadas de funcion potencial \n")
fig, ax = plt.subplots()

ax.plot(x[:10], y_primera_potencial, color='blue', label='Primera derivada potencial')
ax.plot(x[:10], y_segunda_potencial, color='green', label='Segunda derivada potencial')

ax.set_xlabel(titulo_x)
ax.set_ylabel(titulo_y)
ax.set_title('Derivadas de funcion potencial')
ax.legend()

plt.show()

print("Derivadas de funcion exponencial\n")
fig, ax = plt.subplots()

ax.plot(x[:10], y_primera_exponencial, color='blue', label='Primera derivada exponencial')
ax.plot(x[:10], y_segunda_exponencial, color='green', label='Segunda derivada exponencial')

ax.set_xlabel(titulo_x)
ax.set_ylabel(titulo_y)
ax.set_title('Derivadas de funcion exponencial')
ax.legend()

plt.show()

print("Resultados de coeficientes de coorrelacion:\n")

corr_lineal = coeficiente_de_correlacion(x, y)

corr_potencial = coeficiente_de_correlacion(ln_x,ln_y)

corr_exponencial = coeficiente_de_correlacion(x, ln_y)

print(f"Coeficiente de correlación entre las variables de funcion lineal: {round(corr_lineal,2)}")

print(f"Coeficiente de correlación entre las variables de funcion potencial: {round(corr_potencial,2)}")

print(f"Coeficiente de correlación entre las variables de funcion exponencial: {round(corr_exponencial,2)}\n")

print("Se calculan los tiempos de duplicacion y ley de Moore:\n")
tiempo_de_duplicacion_lineal = np.log(2) / a
ley_de_moore_lineal = np.log(2) / (a * 2)

tiempo_de_duplicacion_potencial = np.log(2) / ap
ley_de_moore_potencial = np.log(2) / (ap * 2)

tiempo_de_duplicacion_exponencial= np.log(2) / ae
ley_de_moore_exponencial = np.log(2) / (ae * 2)

print(f"-Lineal:\n\tTiempo de duplicacion: {round(tiempo_de_duplicacion_lineal,5)} dias\n\tLey de Moore: {round(ley_de_moore_lineal,5)} dias\n")
print(f"-Potencial:\n\tTiempo de duplicacion: {round(tiempo_de_duplicacion_potencial,3)} dias\n\tLey de Moore: {round(ley_de_moore_potencial,3)} dias\n")
print(f"-Exponencial:\n\tTiempo de duplicacion: {round(tiempo_de_duplicacion_exponencial,3)} dias\n\tLey de Moore: {round(ley_de_moore_exponencial,3)} dias\n")


