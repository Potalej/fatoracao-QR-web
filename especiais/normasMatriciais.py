# NORMAS ESTILO VETORIAIS
def norma_vetorial(A, p:int)->float:
  """
    Seja `A` uma matriz `m`x`n`. Consideraremos como se `A` fosse um vetor com `mn` componentes e definiremos:

  ||A||^p = Σ Σ |a_ij|^p

  A norma de Frobenius é o caso particular `p = 2`, enquanto que para `p = ∞` tem-se a norma máxima.
  """
  # soma geral
  soma = 0
  for i in range(A.lins):
    for j in range(A.cols):
      soma += abs(A[i,j])**p
  return soma**(1/p)
  

# NORMA DE FROBENIUS
def norma_Frobenius(A)->float:
  """
    A norma de Frobenius é o caso particular da `norma_vetorial` no qual `p = 2`.
  """
  return norma_vetorial(A, p=2)

# NORMA DO MÁXIMO (INFINITO)
def norma_infinito(A):
  """
    A Norma Infinito ou Norma do Máximo é a maior soma absoluta das linhas da matriz `A`.
  """
  return max(
    sum(abs(A[i,j]) for j in range(A.cols)) for i in range(A.lins)
  )

# NORMA 1 
