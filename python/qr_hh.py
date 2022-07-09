from matrizes import MatrizDict
from householder import householder, H, reflexoes

def QR_Householder(M):
  """
    Encontra a fatoração QR de uma matriz `M` através de reflexões de Householder.
  """
  # tamanho
  m,n = M.lins, M.cols
  # instanciamento das matrizes U e R
  U = MatrizDict([[0 for j in range(n)] for i in range(m)])
  R = MatrizDict([[M[i,j] for j in range(n)] for i in range(m)])

  for j in range(min(m,n)):
    # monta o vetor para aplicar Householder
    u = householder(R.subM([j,m],[j,j+1]))
    U.substM([j,m],[j,j+1],u)
    R.substM([j,m],[j,n], H(u, R.subM([j,m],[j,n])))
    # determina os elementos abaixo como nulo
    for i in range(j+1, m):
      R[i,j] = 0

  # matriz identidade
  I = MatrizDict([[1 if i==j else 0 for j in range(U.lins)] for i in range(U.lins)]) 
  # aplica a reflexão
  Q = reflexoes(U, I) # 
  
  return Q,R