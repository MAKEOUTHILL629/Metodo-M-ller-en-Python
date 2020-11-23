from numpy import sign #se importa para el signo
from numpy.lib.scimath import sqrt#se importa la raiz cuadrada, y me permite sacar raices de numeros negativos

#Se define la funcion
def muller(f, x0, x1, x2, tol):
    error = 1e3
    x3 = 0
    while error > tol:
        c = f(x2)
        b = ((x0 - x2)**2 * (f(x1) - f(x2)) - (x1 - x2)**2 *
             (f(x0) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) *
             (f(x1) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        x3 = x2 - (2 * c) / (b + sign(b) * sqrt(b**2 - 4 * a * c))
        error = abs(x3 - x2)
        x0 = x1
        x1 = x2
        x2 = x3
    return x3

# 16*x**4+40*x**3+5*x**2+20*x+6     x0= -3, x1=-2    y x0=-1 , x1=-2
# x**3-x**2+3*x-2   x0=0, x1=1
# x**4-2*x**3+6*x**2-8*x+8      x0=0, x1=1
f = lambda x: x**4-2*x**3+6*x**2-8*x+8  

print(muller(f,0,1,0.5,1e-5))
