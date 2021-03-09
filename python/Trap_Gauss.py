import numpy as np
import sympy as sym
import scipy.integrate as integrate

#Interval lenght
def h (a, b, n):
	return (b-a)/float(n)
#Trapezoidal rule function
def trap_rule (f, a, b, n):
	total = f(a)+f(b)
	dx = h(a, b, n)
	for k in range (1, n):
        	total = total + 2.0*f((a + (k*dx)))
	return dx/2.0*total
#Function to integrate
def f(x):
    return (np.cos(x))**5*np.exp(-x/2.0)
print("We are integrating the function cos(x)^5 exp(-x/2) in the interval [5,20]: \n")
print("Enter the order of the quadrature to evaluate: ")
num = int(input())
print("")
I_trap = trap_rule(f, 5.0, 20.0, num)
I_gauss = integrate.fixed_quad(f, 5.0, 20.0, n=num)

print("Trapezoidal method: ")
print(I_trap,"\n")
print("Gaussian quadrature: ")
print(I_gauss[0],"\n")
print("Exact: ")
y = sym.Symbol('y', real=True) 
g = (sym.cos(y))**5*sym.exp(-y/2.0)
I_exact = float(sym.integrate(g,(y,5.0,20.0)))
print(I_exact,"\n")
print("Errors: ")
print("Iexact-Itrapezoidal: ", I_exact-I_trap)
print("Iexact-Igauss_quad: ", I_exact-I_gauss[0])
