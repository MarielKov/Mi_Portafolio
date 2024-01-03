import matplotlib.pyplot as plt
import numpy as np

ep = 0.001

a = 1
b = 9
n = 3

def func(x):
     #return np.sqrt(x) (No se puede)
     #return x**3+1 #(a = -2 , b = 2)
     #return x**3-x+1 #(a = -2 , b = 2)
     #return ep**(-x)-np.sin(x) #(a = -5 , b = -2)
     #return np.absolute(x+5) (No se puede)
     #return 2*x+3 #(a = -3 , b = 2)
     #6)
     return np.log(x)

     
def biseccion(a,b,ep,n):
    i = 0
    #lim = np.log2(np.absolute(b-a)/ep) 
    lim = b-a  
    err = ((0.5)**n)*lim
    
    while((lim>=ep)):
        c = (a+b)/2 
        print(c)
        print("-----")
        if(c==0):
             err = np.log2(np.absolute(b-a)/ep) 
             return c
        elif((signo(func(c))!= signo(func(a)))and(signo(func(a)))<0):
            i = i + 1
            b=c
            err = np.log2(np.absolute(b-a)/ep) 
            lim = b-a
       
        else:
            i = i + 1
            a=c   
            err = np.log2(np.absolute(b-a)/ep) 
            lim = b-a
    print("Error: ",err)
    return c  
         
def signo(z):
     if(z==0): return 0
     elif(z<0): return -1
     else: return 1  

print(func(a))

print(func(b))

resp = biseccion(a,b,ep,n)   
print("La respuesta es: ", resp)   

# Valores del eje X que toma el gráfico.
cordx = np.arange(-15, 15,0.01)
# Graficar ambas funciones.

plt.plot(cordx, [func(i) for i in cordx])
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
       







