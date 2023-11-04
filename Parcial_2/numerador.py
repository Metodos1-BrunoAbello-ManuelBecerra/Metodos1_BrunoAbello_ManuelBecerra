#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:00:29 2023

@author: manuelbecerra
"""


import numpy as np

c=3*((10)**8)
h = 6.626*((10)**-34)
k = 1.3806*((10)**-23)
T = 5772

lamda0 =  1*((10)**-7)
lamda1 = 4*((10)**-7) #m

v0 = c/lamda0
v1 = c/lamda1


b = (h*v0)/(k*T)
a = (h*v1)/(k*T)

def funcion(x):
    f_x=(x**3)/(np.exp(x)-1)
    return f_x

n = 20
Roots, Weights = np.polynomial.legendre.leggauss(n)
t = 0.5*( (b-a)*Roots + a + b )
Integral_numerador = 0.5*(b-a)*np.sum(Weights*funcion(t))

print(Integral_numerador)

#ya se hizo


