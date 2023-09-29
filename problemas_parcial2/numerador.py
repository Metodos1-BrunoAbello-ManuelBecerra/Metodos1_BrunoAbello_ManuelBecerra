#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:00:29 2023

@author: manuelbecerra
"""

import numpy as np

#numerador
c=3*((10)**8)
h = 6.626*((10)**-34)
k = 1.3806*((10)**-23)
T = 5772

lamda0 =  1*((10)**-7)
lamda1 = 4*((10)**-7) #m

v0 = c/lamda0
v1 = c/lamda1


a = (h*v0)/(k*T)
b = (h*v1)/(k*T)
f = lambda x: (x**3)/(np.exp(-x)-1)

n = 20
Roots, Weights = np.polynomial.legendre.leggauss(n)
print(Roots,Weights)

t = 0.5*( (b-a)*Roots + a + b ) #ese b-a es donde se define el intervalo
Integral_numerador = 0.5*(b-a)*np.sum(Weights*f(t))
print(Integral_numerador)