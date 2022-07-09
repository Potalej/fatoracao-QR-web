from qr_gsclassico import GSClassico
from qr_gsmodificado import GSModificado
from qr_hh import QR_Householder
from matrizes_exemplos import magica, hilbert
from tabulate import tabulate
from erros import tabelaMargens
from time import time

import js
from pyodide import create_proxy

def capturarMatriz(x):
    # captura a matriz
    matriz = js.valores().to_py()
    # converte os valores para float
    matriz = [[
        float(coluna) for coluna in linha
    ] for linha in matriz]
    print(matriz)

evento = create_proxy(capturarMatriz)

js.document.getElementById('calcular').addEventListener("click", evento)


# divisor = 47*"="
# ######################################

# ############## ENTRADAS ##############
# #M = magica(5)
# M = hilbert(50)
# #for i in range(5): M[i,i] = 0
# ######################################

# print(f"-> Matriz original: \n{M}\n")

# ############# FATORAÇÕES #############

# fatoracoes = {
#   "Gram-Schmidt Clássico": GSClassico,
#   "Gram-Schmidt Modificado": GSModificado,
#   "Reflexões de Householder": QR_Householder
# }

# tempos = { fatoracao: 0 for fatoracao in fatoracoes }

# for fatoracao in fatoracoes:
#   print(f"{divisor}\n=> {fatoracao}\n{divisor}")
  
#   # inicia o cronômetro
#   t0 = time()  
#   # aplica a fatoração
#   Q,R = fatoracoes[fatoracao](M)
#   # para o cronômetro e salva o valor
#   t = time() - t0
#   tempos[fatoracao] = t
#   # faz a tabela com margens de erro
#   tabelaMargens(M, Q, R)
  
#   print(f"{divisor}\n")

# ####################################################
# """
#   Averiguar custos de processamento e de consumo de memória, além do tempo demandado para rodar cada função.
# """
# print(f"{divisor}{divisor}\n\n{divisor}\n=> Custos\n{divisor}\n")
# # monta a tabela de tempo gasto
# tabela = [
#   [fatoracao, tempos[fatoracao]] for fatoracao in tempos
# ]
# print(tabulate(
#     tabela,
#     ["Método", "Tempo (em segundos)"],
#     tablefmt="presto"
# ))