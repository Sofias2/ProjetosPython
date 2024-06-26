# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:31:18 2023

@author: Sofia
"""
# operador Xor
import numpy as np

def sigmoid(soma):
    return 1 / (1+ np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)


entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([[0], [1], [1], [0]])
# pesos do x1 e pesos x2
#pesos0 = np.array([[-0.424, -0.740, -0.961], [0.358, -0.577, -0.469]])
# pesos da camada oculta para a camada oculta
#pesos1 = np.array([[-0.017],[-0.893], [0.148]])

pesos0 = 2*np.random.random((2,3)) -1
pesos1 = 2*np.random.random((3,1)) -1

epocas = 1000000
taxaAprendizagem = 0.5
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada,pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSnapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSnapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Error: " + str(mediaAbsoluta))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    
    pesos1Transposta = pesos1.T
    
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)