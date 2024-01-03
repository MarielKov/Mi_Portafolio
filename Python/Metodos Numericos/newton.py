import numpy as np
import matplotlib as plt


ep = 0.001

xn = 5
n = 0
dif = 0

def f():
# defining polynomial function
    var = np.poly1d([1, 0, 1])
    print("Polynomial function, f(x):\n", var)
    return var

def f1(var):
# calculating the derivative
    derivative = var.deriv()
    print("Derivative, f(x)'=", derivative)

    return derivative
  
# calculates the derivative of after 
# given value of x
#print("When x=5  f(x)'=", derivative(5))














