import numpy as np

print("Tp Factorizacion LU por Mariel Kovinchich\n")

A = np.array([[2,-1,1], [3,3,9],[3,3,5]],float)
b = np.array([[-1],[0],[4]], float) 

print("Matrices a resolver:\nA: \n", A, "\n----------------\nb: \n", b)
print("----------------\n")

def lu(A):
    
    n = A.shape[0]
    print("Obtenemos el numero de filas: \n n =",n)
    print("----------------\n")
    
    U = A.copy()
    print ("Se copia la matriz A en U para hacer las operaciones \n",U)
    print("----------------\n")

    L = np.eye(n, dtype=np.double)
    print("L empieza como una matriz identidad\n", L)
    print("----------------\n")
    
    print("Este loop se eliminan las entradas debajo de i con operaciones de fila en U e invertir las operaciones de fila para manipular L \n")
    for i in range(n):
            
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]

        print("Proceso de transformacion de L:\n",L)
        print("----------------\n")
        print("Proceso de transformacion de U:\n",U)
        print("----------------\n")
        
    return L, U

def primera_sustitucion(L, b):
    
    n = L.shape[0]
    print("Numero de filas en L: \n n =",n)
    print("----------------\n")
    
    y = np.zeros_like(b, dtype=np.double);
    print("Se crea el vector de solución y:\n" ,y)
    print("----------------\n")
    
    y[0] = b[0] / L[0, 0]
    
    print("Recorremos las filas de abajo hacia arriba, comenzando con la penúltima fila, porque la última fila se completó en el paso anterior\n")
    print("y: \n", y)
    print("----------------\n")

    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
        print("Proceso de transformacion de y:\n",y)
        print("----------------\n")
        
    return y
  
def segunda_sustitucion(U, y):
    
    n = U.shape[0]
    print("Numero de filas en U: \n n =",n)
    print("----------------\n")
    
    x = np.zeros_like(y, dtype=np.double);
    print("Se crea el vector de solución x:\n" ,x)
    print("----------------\n")

    x[-1] = y[-1] / U[-1, -1]
    print("Aquí realizamos la sustitución hacia atrás")
    print("Inicializando con la última fila \n x:\n", x)
    print("----------------\n")
    
    print("Recorremos las filas de abajo hacia arriba, comenzando con la penúltima fila, porque la última fila se completó en el paso anterior")
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
        print("Proceso de transformacion de x:\n",x)
        print("----------------\n")
        
    return x


print("Llamando a las funciones y resultados: ")
L , U =lu(A)
print("L: \n",L ,"\n----------------\n")
print("U: \n",U,"\n----------------\n")

y = primera_sustitucion(L , b)
print("y: \n",y , "\n----------------\n")

x = segunda_sustitucion(U , y)
print("x: \n",x, "\n----------------\n")

print("Resultado comparativo: \n",np.linalg.solve(A, b))
print("----------------\n")


