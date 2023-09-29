#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:30:22 2023

@author: manuelbecerra
"""
import numpy as np





#PROBLEMA 19, SUPERCONDUCTORES


TD = 300
T = 300
deltaT = 0
deltaT_d = 0

f = lambda x: (np.tanh(np.sqrt(x**2 + deltaT_d**2)*(TD/(2*T))))/(np.sqrt(x**2 + deltaT_d**2))

N = 1000
x = np.linspace(1,20,N+1)