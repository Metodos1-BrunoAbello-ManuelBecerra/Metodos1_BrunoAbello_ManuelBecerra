#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:56:08 2023

@author: manuelbecerra
"""

import numpy as np

def MetodoPotencia(H, V, k):
    W = V/np.sqrt(np.matmul(V.T, V))
    for i in range(k+1):
        V = np.matmul(H, W)
        W = V/np.sqrt(np.matmul(V.T, V))
    P1 = np.matmul(H, W)
    Niu = np.matmul(W.T, P1)
    return Niu, W

k = 500
V = np.array([1,0,0])

H = np.array([[1,2,-1],[1,0.,1],[4,-4,5]])

H_inv = np.linalg.inv(H)

Valor, vector = MetodoPotencia(H_inv, V, k)
print(Valor, vector)

