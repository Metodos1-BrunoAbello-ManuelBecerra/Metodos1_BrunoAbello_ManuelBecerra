import numpy as np
import sympy as sym
import math as m
from scipy import integrate

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
n = 2
def GetLaguerre(n, x):
    if n == 0:
        poly = sym.Number(1)
    elif n==1:
        poly = 1-x
    else:
        poly = ((2*(n-1)+1-x)*GetLaguerre(n-1,x)-(n-1)*GetLaguerre(n-2,x))/n
    return sym.expand(poly,x)
print(GetLaguerre(2, x))
def GetDLaguerre(n,x):
    Pn = GetLaguerre(n,x)
    return sym.diff(Pn,x,1)
def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots
def GetAllRootsGLag (n):
    xn = np.linspace(0,n+(n-1)*np.sqrt(n),100)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerre(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots
def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)

    Laguerre = []
    
    for i in range(n+2):
        Laguerre.append(GetLaguerre(i,x))
    
    poly = sym.lambdify([x],Laguerre[n+1],'numpy')
    Weights = Roots/((n+1)*2*poly(Roots)*2)
    
    return Weights
R = GetAllRootsGLag(2)
print(R)
f1 = lambda t: (t-R[1])/(R[0]-R[1])
Weight1 = integrate.quad(f1, 0, np.inf)
f2 = lambda t: (t-R[0])/(R[1]-R[0])
Weight2 = integrate.quad(f2, 0, np.inf)
GetWeightsGLag(2)
f = lambda t: t**3
I = sum(f(GetAllRootsGLag(3))*GetWeightsGLag(3))
print(I)