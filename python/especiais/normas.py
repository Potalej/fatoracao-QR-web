from math import sqrt

def norma2(v)->float:
  """
      Recebe um vetor do tipo `MatrizDict` e retorna sua norma euclidiana.
  """
  return sqrt(sum([v[i,0]**2 for i in range(v.lins)]))

