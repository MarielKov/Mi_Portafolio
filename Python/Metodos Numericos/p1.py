import matplotlib as plt
import numpy as np
import sys

ep = sys.float_info.epsilon

a = 1
b = 7
n = 5

def func(x):
     return np.sqrt(x)
     
def biseccion(a,b,ep,n):
    i = 1
    #lim = np.log2(np.absolute(b-a)/ep) 
    lim = b-a  
    
    while((lim>=ep)and(i != n)):
        c = (a+b)/2 
        print(c)
        print("-----")
        if(c==0):
             return c
        elif(signo(func(c))!= signo(func(a))<0):
            i = i + 1
            b=c
            #lim = np.log2(np.absolute(b-a)/ep) 
            lim = b-a
       
        else:
            i = i + 1
            a=c   
            #lim = np.log2(np.absolute(b-a)/ep) 
            lim = b-a
        
    return c  
         
def signo(z):
     if(z==0): return 0
     elif(z<0): return -1
     else: return 1  


resp = biseccion(a,b,ep,n)   
print(resp)    
       







