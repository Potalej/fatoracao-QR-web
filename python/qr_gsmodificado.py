from normas import norma2
from matrizes import MatrizDict

def GSModificado(X):
  """
    Método de Gram-Schmidt Modificado para o cálculo da fatoração QR de uma matriz X informada.
  """
  # tamanhos
  m,n = X.lins, X.cols
  # instancia as matrizes
  Q = MatrizDict([[0 for j in range(n)] for i in range(m)]) # Q_{m x n}
  R = MatrizDict([[0 for j in range(n)] for i in range(n)]) # R_{n x n}

  for k in range(n):
    # altera a coluna k de Q
    Q.setcol(k, X.col(k))  

    for i in range(k-1):
      # R_{ik} = q_{i}' q_{k}
      R[i,k] = (Q.col(i).T() * Q.col(k))[0,0]
      # nova coluna k de Q
      novaCol = Q.col(k) - R[i,k]*Q.col(i)
      Q.setcol(k, novaCol)

    # define o elemento k diagonal de R, que é a norma de q_k
    R[k,k] = norma2(Q.col(k))
    # normaliza
    Q.setcol(k, Q.col(k)*(1/R[k,k]))

  return Q,R