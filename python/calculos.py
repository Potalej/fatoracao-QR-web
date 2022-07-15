# módulos utilizados, como no programa original
from matrizes import MatrizDict
from qr_gsclassico import GSClassico
from qr_gsmodificado import GSModificado
from qr_hh import QR_Householder
from time import time
from normasMatriciais import *

def calculos(matriz):
    """ 
        Recebe a matriz e faz a fatoração QR utilizando:
       
        - Gram-Schmidt Clássico;
        - Gram-Schmidt Modificado;
        - Reflexões de Householder.

        Retorna um dicionário com as matrizes e informações obtidas.
    """
    # transforma no tipo MatrizDict
    M = MatrizDict(matriz)
    # funções e nomes
    funcoes = {
        "Gram-Schmidt Clássico": GSClassico,
        "Gram-Schmidt Modificado": GSModificado,
        "Reflexões de Householder": QR_Householder
    }
    # em um dict ficará armazenado todas as informações necessárias
    dict_info = {
        nome: {
            "função": funcoes[nome],
            "matriz": M.lista(),
            "margem QtQ": {},
            "margem QR": {}
        } for nome in funcoes
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
