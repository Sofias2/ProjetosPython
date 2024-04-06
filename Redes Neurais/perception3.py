# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:05:18 2023

@author: Sofia
"""
# encontrar o melhor conjunto de pesos para minimizar os erros

import numpy as np
#operador E
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0,0,0,1])

# com o operador Or
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0,1,1,1])

# operador xor -> valores iguais é zero
entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0,1,1,0])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >=1):
        return 1
    return 0


def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro )
                print("Peso atualizado " + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))
        
treinar()
