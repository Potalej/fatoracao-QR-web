from normas import norma2
from math import sqrt
from matrizes import MatrizDict
 
def householder(X):
  """
    Gera uma reflexão de householder. Encontra aquele vetor `v` que usamos em:
      `H = I - uu'`
    com
      `Hx = -+ nu e_1`
    A função `sign` no MATLAB recebe um vetor e retorna outro vetor de mesmo tamanho, mas no lugar dos índices do recebido ela retorna 1, caso seja positivo, 0, caso seja 0 e -1, caso seja negativo.
    Como Clever faz, também aqui foi feito: retorna 1 também caso seja 0.
  """
  # função sinal
  nu = norma2(X)
  if nu != 0:
    u = X * (1/nu)
    u[0,0] = u[0,0] + (1 if u[0,0]>=0 else -1)
    u = u * (1/sqrt(abs(u[0,0])))
  else:
    u = X
    u[0,0] = sqrt(2)
  
  return u

# função que aplica Householder sobre um vetor a partir de outro
H = lambda u,x: x - u*(u.T()*x)

def reflexoes(U,X):
  """
    Aplica as reflexões de Householder  
  """
  Z = MatrizDict([[X[i,j] for j in range(X.cols)] for i in range(X.lins)])
  n = U.cols
  for j in range(n-1, -1, -1):
    Z = H(U.col(j), Z)
  return Z