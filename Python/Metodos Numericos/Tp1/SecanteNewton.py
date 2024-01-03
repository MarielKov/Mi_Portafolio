import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


print("TP Newton + Secante\n")

print("Intergrantes: Mariel Kovinchich, Damian Lescano")
ep = 0.0001
print("Epsilon = ", ep)

print("El intervalo de trabajo es [0,3]")
x0 = 3
print("X0 = ", x0)
x1 = 0
print("X1 = ", x1)

n = 0
print("Numero de iteraciones = ", n)
dif = 1000
print("Diferencial = ", dif)


print("Se ingresa la funcion f(x) = x^3+4x^2-10")
def f(x):
    
    return x**3+4*x**2-10

print(f(x0))


print("Se hace la derivada f'(x) = 3x^2+8x")
def f1(x):
    
    return 3*x**2+8*x

print(f1(x0))

print("Funcion del Metodo de Newton\n")
def newton(x):
    
     return x - f(x)/f1(x)


print("Funcion del método de la secante\n")
def secante(x0, x1):
    

    if(f(x0) * f(x1) >= 0):
        print('El método de la secante no se puede aplicar f(x0) por f(x1) es menor a 0\n')
        print("------------------------")
        
    
    else:
        print("Se calcula el Metodo secante\n")
        c = x1 - f(x1)*(x0 - x1)/(f(x0) - f(x1))
        
        if (f(c) == 0):
            print("c es igual a 0")
            return c
        
        elif(f(x1) * f(c) < 0):
            print("c por f(x1) es negativo\n")
            x0 = c
            return x0
        
        else:
            print("c por f(x1) es positivo\n")
            x1 = c
            return x1


print("Para el grafico: Tomamos un rango de [-15,15] en ambos ejes\n")
cordx = np.arange(-15, 15,0.01)

print("Se grafica f(x) y f'(x) con las x en el rango mencionado\n ")
plt.plot(cordx, [f(i) for i in cordx])
plt.plot(cordx, [f1(i) for i in cordx])
derivada = mpatches.Patch(color='orange', label="F'(x)")
funcion = mpatches.Patch(label='F(x)')
plt.legend(handles= [derivada,funcion])

print("Color: f(x) es la funcion azul y la naranja la derivada\n")
plt.axhline(0, color="black")
plt.axvline(0, color="black")

print("Se Limitar los valores de los ejes\n")
plt.xlim(-15, 15)
plt.ylim(-15, 15)

print("Titulo del grafico\n")
plt.title("Grafico de F(x) y F'(x)")

print("Guarda el grafico en un archivo aparte\n")
plt.savefig("output.png")
print("Muestra el grafico\n")
plt.show()

print("En este ciclo se ejecuctan las funciones con los metodos secante y newton\n Si n es impar usa el metodo de Newton, si es par usa metodo secante\n")
print("Si el diferencial es menor al epsilon, se detiene el ciclo\n") 
print("Se calcular un nuevo diferencial en cada vuelta, esto limita cuantas veces se hacen la iteraciones\n")
while (dif > ep):

    if(n % 2 == 0):
        print("Metodo de Newton\n")
        x0 = newton(x0)
       
        dif = np.abs(x0 - newton(x0))
        print("Se calcula el nuevo ddiferencial con Newton:", np.round(dif,7))
        n += 1
       
    else:
       print("Metodo Secante\n")
       x0 = secante(x1,x0)
       dif = (f(x1) - f(x0))/ (x1-x0)
       print("Se calcula el nuevo ddiferencial con Secante:", np.round(dif,7))
      #El diferencial esta redondeado en 7 decimales para que imprima bien en la ultima iteracion, si se redondea con menos, imprime cero
       n += 1

    resta = x1-x0  
    print("Calculo el margen de error de la aproximacion\n")
    error = np.log2(np.abs(resta)/ep)
    print("------------------------")
    
    print("Imprimiendo los resultados de la iteracion nº", n)
    print("------------------------")
    print("Error de aproximacion: ", error.round(3))
    print("Xn: ", np.round(x0, 3))
    print("Diferencial: ", np.round(dif,7))
    print("---------------------")


print("\nLa raiz aproximada es: ", np.round(x0, 3) ,", con un error de aproximacion de: ", error.round(3))

resultado = f(x0)

print("Se comprueba si la raiz obtenida (Xn) se acerca a y = 0\n F(Xn) = ", np.round(resultado,8), "\n")


