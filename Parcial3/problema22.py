#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:05:10 2023

@author: manuelbecerra
"""
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
import numpy as np
import sympy as sym

#a
#el angulo de equilibrio sacamos en nuestro pre parcial y es 0.6435011087932845 radianes 

x_radianes = 0.6435011087932845

c = 729/10000

f1 = (sym.sin(x_radianes))**6 + c*(sym.sin(x_radianes)**2) - c

print("como pueden ver f1 es practicamente cero" +str(f1))

#b
def Function(x):
    c = 729/10000
    return (np.sin(x))**6 + c*(np.sin(x)**2) - c

x = np.linspace(0,np.pi,50)
y = Function(x)

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            # Criterio de parada
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
    
root = GetNewtonMethod(Function,Derivative,1.)

def GetAllRoots(x, tolerancia=10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(Function,Derivative,i)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

Roots = GetAllRoots(x)
print(Roots)


#c

seno = sym.sin(x_radianes)
print("el seno del angulo de equilibrio de este sistema es "+str(seno))