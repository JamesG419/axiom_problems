#Given the differential equation f'(x) = x^x, write a function that uses Euler's 
#method to approximate the value of f(x1) given an initial condition (x0, f(x0)) and the value of x1.

def fprime(x):
    return x**x

def euler_method(x0,fx0,x1):
    
    dx = 0.00001
    x = x0
    fx = fx0

    while (x <= x1):
       fx += fprime(x) * dx
       x += dx 
    
    return fx


#test
print(euler_method(0,0,2))