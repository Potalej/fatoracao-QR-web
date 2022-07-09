"""
    PRIMEIRAMENTE, É PRECISO CONFIGURAR O AMBIENTE DO JAVASCRIPT E DEFINIR A FUNÇÃO QUE CAPTURAR OS VALORES DA MATRIZ.
"""

import js
from pyodide import create_proxy, to_js

def capturarMatriz(x):
    # precisa limpar tudo antes
    js.document.getElementById("resultados").innerHTML = ""
    # captura a matriz
    matriz = js.valores().to_py()
    # converte os valores para float
    matriz = [[
        float(coluna) if coluna != "" else 0 for coluna in linha
    ] for linha in matriz]
    
    # faz os cálculos
    dict_info = calculos(matriz)

    # agora é preciso passar as informações para o js dar conta
    js.exibirResultados(to_js(dict_info))
    
evento = create_proxy(capturarMatriz)

js.document.getElementById('calcular').addEventListener("click", evento)

from matrizes_exemplos import magica, hilbert
def fun_rodar_quadradoMagico(x):
    # captura o tamanho
    n = int(js.document.getElementById("tamanho_matriz").value)
    # faz a matriz
    M = magica(n)
    # substitui nos inputs
    for i in range(M.lins):
        for j in range(M.cols):
            js.document.getElementById(f"matriz_{i}_{j}").value = M[i,j]
    
rodar_quadradoMagico = create_proxy(fun_rodar_quadradoMagico)
js.document.getElementById('rodar_quadradoMagico').addEventListener("click", rodar_quadradoMagico)

def fun_rodar_hilbert(x):
    # captura o tamanho
    n = int(js.document.getElementById("tamanho_matriz").value)
    # faz a matriz
    M = hilbert(n)
    # substitui nos inputs
    for i in range(M.lins):
        for j in range(M.cols):
            js.document.getElementById(f"matriz_{i}_{j}").value = M[i,j]
    
rodar_hilbert = create_proxy(fun_rodar_hilbert)
js.document.getElementById('rodar_hilbert').addEventListener("click", rodar_hilbert)

# FEITA ESSA PARTE, AGORA É PRECISO TRABALHAR COM A MATRIZ

from matrizes import MatrizDict
from qr_gsclassico import GSClassico
from qr_gsmodificado import GSModificado
from qr_hh import QR_Householder
from time import time
from normasMatriciais import *

def calculos(matriz):
    """VAI RECEBER A MATRIZ E FAZER TODO O PARANAUÊ"""
    # transforma no tipo MatrizDict
    M = MatrizDict(matriz)
    # funções e nomes
    funcoes = {
        "Gram-Schmidt Clássico": GSClassico,
        "Gram-Schdmit Modificado": GSModificado,
        "Reflexões de Householder": QR_Householder
    }
    # em um dict ficará armazenado todas as informações necessárias
    dict_info = {
        nome: {
            "função": funcoes[nome],
            "matriz": M.lista(),
            "Q": 0, # vai receber uma MatrizDict
            "R": 0, # vai receber uma MatrizDict
            "margem QtQ": {}, # vai receber um dict de normas
            "margem QR": {}, # vai receber um dict de normas
            "tempo": 0, # vai receber um float de tempo
        }
        for nome in funcoes
    }
    # lista de normas
    normas = {
        "Norma 1": lambda M: norma_vetorial(M, p=1),
        "Frobenius": norma_Frobenius,
        "Norma Infinito": norma_infinito
    }

    # percorre as funções, aplicando a transformação em todas
    for nome in funcoes:
        # função de fato
        func = funcoes[nome]    
        
        ### Cálculos
        # começa o cronômetro
        t0 = time()
        # aplica
        Q,R = func(M)
        # encerra o timer
        t = time() - t0
        
        ### FAZER A PARTE DE ERROS
        # matrizes que serão averiguadas
        AQR = M - Q*R
        IQtQ = MatrizDict([[1 if i == j else 0 for j in range(M.cols)] for i in range(M.lins)]) - Q.T() * Q
        
        # aplica as normas para medir os erros
        for norma in normas:
            norma_func = normas[norma]
            dict_info[nome]["margem QtQ"][norma] = norma_func(IQtQ)
            dict_info[nome]["margem QR"][norma] = norma_func(AQR)

        ### Adicionando ao dict_info
        dict_info[nome]["Q"] = Q.lista()
        dict_info[nome]["R"] = R.lista()
        dict_info[nome]["tempo"] = t

    return dict_info
