from auxiliares.matrizes import MatrizDict
import numpy as np

def hilbert(n:int):
    """
        Retorna uma matriz de Hilbert de tamanho n.
        Como os índices no Python são usualmente i-1 do que usamos na notação matemática, é facil ver que:
            `H_ij = 1/(i+j-1)`
        precisa ser, na verdade:
            `H_ij = 1/(i+1+j+1-1) = 1/(i+j+1)`
    """
    M = [[
        1/(i+j+1) for j in range(n)
    ] for i in range(n)]
    return MatrizDict(M)


"""
    CÓDIGO ADAPTADO DE: 
    https://stackoverflow.com/questions/47834140/numpy-equivalent-of-matlabs-magic
"""
def magica(n):
  n = int(n)
  if n < 3:
    raise ValueError("O tamanho mínimo é 3.")
  if n % 2 == 1:
    p = np.arange(1, n+1)
    return MatrizDict((n*np.mod(p[:, None] + p - (n+3)//2, n) + np.mod(p[:, None] + 2*p-2, n) + 1).tolist())
  elif n % 4 == 0:
    J = np.mod(np.arange(1, n+1), 4) // 2
    K = J[:, None] == J
    M = np.arange(1, n*n+1, n)[:, None] + np.arange(n)
    M[K] = n*n + 1 - M[K]
  else:
    p = n//2
    M = np.matrix(magica(p).lista())
    M = np.block([[M, M+2*p*p], [M+3*p*p, M+p*p]])
    i = np.arange(p)
    k = (n-2)//4
    j = np.concatenate((np.arange(k), np.arange(n-k+1, n)))
    M[np.ix_(np.concatenate((i, i+p)), j)] = M[np.ix_(np.concatenate((i+p, i)), j)]
    M[np.ix_([k, k+p], [0, k])] = M[np.ix_([k+p, k], [0, k])]

  M = MatrizDict(M.tolist())
  return M