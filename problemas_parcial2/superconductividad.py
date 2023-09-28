#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:30:22 2023

@author: manuelbecerra
"""

from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sym




#PROBLEMA 19, SUPERCONDUCTORES


TD = 300
T = 300
deltaT = 0
deltaT_d = 0

f = lambda x: (np.tanh(np.sqrt(x**2 + deltaT_d**2)*(TD/(2*T))))/(np.sqrt(x**2 + deltaT_d**2))

N = 1000
x = np.linspace(1,20,N+1)