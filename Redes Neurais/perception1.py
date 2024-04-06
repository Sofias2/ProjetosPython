# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:35:35 2023

@author: Sofia
"""

entradas =[1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i]*p[i]
          
    return s

s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >=1):
        return 1
    return 0

r = stepFunction(s)

print(r)