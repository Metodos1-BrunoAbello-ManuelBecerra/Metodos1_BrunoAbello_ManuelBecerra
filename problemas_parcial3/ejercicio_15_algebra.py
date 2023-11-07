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

def epsilon(i,j,k):
    i += 1
    j += 1
    k += 1
    e = int()
    lis = [i,j,k]
    
    if lis == [1,2,3] or lis == [2,3,1] or lis == [3,1,2]:
        e=1
    
    if lis == [3,2,1] or lis == [1,3,2] or lis == [2,1,3]:
        e=-1
    
    if i==j or j==k or k==i:
        e=0
    
    return e

matrices = [ox,oy,oz]
no_sirve = list()
sirve = list()

for m in range(0,3):
    for n in range(0,3):
        for o in range(0,3):
            lis = [m,n,o]
            
            m1 = matrices[m]
            m2 = matrices[n]
            m3 = matrices[o]
            e = epsilon(m, n, o)

            a = m1*m2 - m2*m1
            b = 2*i*e*m3
            
            if a ==b:
                #print(a)
                #print(b)
                sirve.append(lis)
            else: 
                no_sirve.append(lis)
            
print("los que NO sirven son "+ str(no_sirve) + " y hay " +str(len(no_sirve)))
print("los que sirven son "+ str(sirve) + " y hay " +str(len(sirve)))
c = ox*oy - oy*ox
print(c)