#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:30:22 2023

@author: manuelbecerra
"""
import numpy as np
import sympy as sym

#PROBLEMA 19, SUPERCONDUCTORES
N0V = 0.3

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def funcion(T,deltaT_d):
    return (np.tanh(np.sqrt(x**2 + deltaT_d**2)*(300/(2*T))))/(np.sqrt(x**2 + deltaT_d**2))

n = 20

def GetLegendre(n,x,y):
    
    y = (x**2 - 1)**n
    
    poly = sym.diff( y,x,n )/(2**n*np.math.factorial(n))
    
    return poly

Legendre = []
DLegendre = []

for i in range(n+1):
    Poly = GetLegendre(i,x,y)
    Legendre.append(Poly)
    DLegendre.append(sym.diff(Poly,x,1))
    

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
    
def GetRoots(f,df,x,tolerancia = 14):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRoots(n,xn,Legendre,DLegendre):
    
    poly = sym.lambdify([x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)
    
    return Roots

dT = 0.001
intervalo = 20-1
pasos = intervalo / dT

xn = np.linspace(1,20,int(pasos))
Roots1 = GetAllRoots(n,xn,Legendre,DLegendre)

def GetWeights(Roots,DLegendre):
    
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights

weights = GetWeights(Roots1,DLegendre)
print(weights)
print(Roots1)

a=1
b=20

integral = 0
Tc = 0

for i in range(len(Roots1)):
    Tc = 0.5 * (b - a) * Roots1[i] + 0.5 * (a + b)
    integral += weights[i] * funcion(Tc,0)
    integral *= 0.5 * (b - a)
    if np.abs(integral-1/(N0V)) < dT: 
        break

print(Tc)

