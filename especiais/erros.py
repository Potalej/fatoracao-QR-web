from tabulate import tabulate
from normasMatriciais import *
from matrizes import MatrizDict

def tabelaMargens(A, Q, R):
  """
    Faz uma pequena tabela com comparações de margens de erro da ortogonalidade de `Q` e da precisão de `QR` através de algumas normas matriciais.
  """
  # cabeçalho
  cabecalho = ["Norma", "||A - QR||", "||I - QᵗQ||"]

  # calcula Q*R
  QR = Q*R
  # calcula A - QR
  dif_AQR = A - QR
  # gera a matriz identidade
  In = MatrizDict([[1 if i==j else 0 for j in range(Q.lins)] for i in range(Q.lins)])
  # calcula I - QᵗQ
  dif_IQ = In - Q.T()*Q

  # lista de normas que serão utilizadas
  normas = {
    "Norma 1": lambda M: norma_vetorial(M, p=1),
    "Frobenius": norma_Frobenius,
    "Norma Infinito": norma_infinito
  }

  # onde será armazenada a tabela
  tabela = []
  # percorre a lista de normas e vai aplicando
  for norma in normas:
    tabela.append([
      norma,
      normas[norma](dif_AQR),
      normas[norma](dif_IQ)
    ])
  # printa a tabela
  print(tabulate(
    tabela,
    cabecalho,
    tablefmt="presto"
  ))