import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

print("TP Metodo de Jacobi. Integrantes: Mariel Kovinchich, Damian Lescano")

print("\nSe toman los siguientes datos:")

A = np.array([[3,1,-1], 
	      	[1,4,1],
			[2,1,6]],float)

b = np.array([[5],[3],[-2]], float) 

x = np.array([[0],[0],[0]],float)

print ("\nMatriz A:\n", A)

print ("\nVector b:\n", b)

print("\nVector x:\n", x)

def verificarInversivilidadDeD(D):
	print("\nSe comprueba si la matriz diagonal puede ser inversibles\n")
	print("---------------------------\n")
	determinante = np.linalg.det(D)
	if(determinante == 0):
		print(f"El determinante de la matriz D es {determinante}, por lo tanto no es inversible y no se puede usar el metodo de Jacobi")
		return False
	else:
		print(f"El determinante de la matriz D es distinto de 0 ({determinante}), por lo tanto es inversible y se puede usar el metodo de Jacobi")
		return True


def diagonal(A):
	print("A partir de la matriz A, se saca la diagonal y R o (L + U)")
	D = np.diag(np.diag(A)) 
	R = A - D 
		
	print("\nMatriz Diagonal:\n",D)
	print("\nMatriz L+U:\n",R)
		
	return D , R 
			
def jacobi(b,x,D,R): 
    
	n = len(x)
	copiaX = x.copy()
	print("Calculo de Jacobi\n")
	for i in range(n):
		
		x[i] = -(D[i, i]**-1) * np.dot(R[i, :], copiaX) + (D[i, i]**-1) * b[i]
		print("Metodo de Jacobi para X[", i,"] = ", x[i].round(3))

	return x

def imprimir(b,x,D,R): 
  
	e = 0.0001
	copiaX = x.copy()
	n = len(x)
	x1 = []
	x2 = []
	x3 = []

	print("Valores definidos de: ")
	print("\n- Numéro de iteraciones = ", max )
	print("\n- Criterio de parada = ", e)
	print("\n- Columnas de matriz = ", n)

	print("\nEmpieza el bucle para hacer el metodo")
	for k in range(1,max): 
		print("\nSe guardan los resultados de las variables x de cada interacion para los graficos\n")
		
		for i in range(n):
			if(i==0):
				x1.append(float(x[i]))
			elif(i==1):
				x2.append(float(x[i]))	
			else:
				x3.append(float(x[i]))	

		x = jacobi(b,x,D,R)
		print("\nCalculo de la norma\n")
		norma = np.linalg.norm(x - copiaX)
		
		print("---------------------------\n")
		print ("Numero de iteración: ", k )
		print("\n X : \n", x.round(3))
		print("\nNorma = ", abs(norma).round(6))
		print("\n---------------------------\n")

		print("Se comprueba si converge o no, si no converge, se copia el vector x actual y vuelve a empezar el ciclo")
		if norma<e:

			return x,k,x1,x2,x3
		
		else:

			copiaX = np.copy(x)

	return [[],max]

print("Se ejecuta la funcion Diagonal\n")

D, R = diagonal(A)

dInversible = verificarInversivilidadDeD(D)
print("Si es inversible, el algoritmo continua con el algoritmo con normalidad\n")
if(dInversible):

	max = 100

	x,k,x1,x2,x3 = imprimir(b,x,D,R)
	print("Se toman las listas x guardadas en cada iteracion y se hace un grafico de aproximacion\n")
	plt.plot(range(k), x1)
	plt.plot(range(k), x2)
	plt.plot(range(k), x3)
	
	print("Se ponen nombre a los ejes\n")
	plt.xlabel('Iteracion')
	plt.ylabel('X')
	plt.title('Solución aproximada mediante Jacobi')

	print("Se definen las funciones y sus colores para diferenciarlos\n")
	f1 = mpatches.Patch(label='X1')
	f2 = mpatches.Patch(color='orange', label="X2")
	f3 = mpatches.Patch(color='green', label="X3")
	
	print("Se agrega una leyenda para cada funcion\n")
	plt.legend(handles= [f1,f2,f3])

	print("Se agrega una grilla para mejor vizualizacion\n")
	plt.grid(True)

	print("Muestra el grafico\n")
	plt.show()

	print("Si el numero de iteraciones hechas es el mismo que el maximo de iteraciones, la matriz no converge\n ")
	if(k == max):
		print("\nEl método diverge o no converge para la cota de error pedido")

	else: 
		print("\nEl vector 'x' es:")
		print(x.round(3))

		print("\nEl numero de iteraciones es: ", k)
		print("\n")




