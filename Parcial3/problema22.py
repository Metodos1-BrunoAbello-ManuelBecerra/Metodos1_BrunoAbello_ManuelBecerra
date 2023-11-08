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



#c

seno = sym.sin(x_radianes)
print("el seno del angulo de equilibrio de este sistema es "+str(seno))