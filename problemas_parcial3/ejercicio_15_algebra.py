#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 19:25:04 2023

@author: manuelbecerra
"""
import sympy as sp

i = 1j

ox = sp.Matrix([[0, 1],
              [1, 0]
              ])

oy = sp.Matrix([[0, -i],
              [i, 0]
              ])

oz = sp.Matrix([[1, 0],
              [0, -1]
              ])

#esta funcion determina el valor de epsilon segun el problema 14
def epsilon(i,j):
    i += 1
    j += 1
    e = int()
    lis = [i,j]
    
    if lis == [1,2] or lis == [2,3] or lis == [3,1]:
        e=1
    
    elif lis == [3,2] or lis == [1,3] or lis == [2,1]:
        e=-1
    
    else:
        e=0
    
    return e

matrices = [ox,oy,oz]
no_sirve = list()
sirve = list()

for m in range(0,3):
    for n in range(0,3):
        
        #aqui se asegura que cada matriz sea diferente y que haya una combinacion diferente cada vez
        if (m == 0 and n == 1) or (m == 1 and n == 0):o = 2
        elif (m == 1 and n == 2) or (m == 2 and n == 1):o = 0
        elif (m == 0 and n == 2) or (m == 2 and n == 0):o = 1
        #en los otros casos, o sea donde una de las matrices para conmutar sean iguales, va a cero entonces la tercer matriz puede ser cualquiera ya que epsilon sera 0 
        else: o = 0
        
        lis = [m,n,o]
            
        m1 = matrices[m]
        m2 = matrices[n]
        m3 = matrices[o]
        e = epsilon(m, n)

        a = m1*m2 - m2*m1
        b = 2*i*e*m3
            
        if a == b:
            print(a)
            print(b)
            sirve.append(lis)
        else: 
            no_sirve.append(lis)
            
print("los que NO sirven son "+ str(no_sirve) + " y hay " +str(len(no_sirve)))
print("los que sirven son "+ str(sirve) + " y hay " +str(len(sirve)))

#como se puede ver, todos aplican a la regla