class MatrizDict:
  """
    O tipo `MatrizDict` demanda menos memória para armazenar e operar com matrizes
    esparsas que os tipos tradicionais, pois utiliza `dicts` em vez de `lists`.
  """
  def __init__(self, matriz_base=[], lins=1, cols=1, colunas=[]):
    """
      Para inicializar, é importante informar o tamanho da matriz para operações
      futuras. Elementos (TALVEZ) podem ser adicionados à posteriori, mas manter
      uma estrutura fixa é importante.
      Se desejado, é possível informar uma matriz no formato de lista para que
      seja feita a conversão através do parâmetro `matriz`. Caso seja passado um
      vetor, este será convertido para uma matriz coluna.
      Pode receber também uma lista de vetores colunas do tipo `MatrizDict` e os
      converte numa só matriz.
    """
    # define tamanho
    self.lins = lins
    self.cols = cols
    # onde é armazenada a matriz
    self.matriz = dict()
    # verifica se foi informada alguma matriz de base
    if len(matriz_base) > 0:
      # caso seja, é preciso verificar se foi passado um vetor ou uma matriz
      try: matriz_base[0][0]
      except:
        # caso seja um vetor, a quantidade de colunas é 1
        self.cols = 1
      else:
        # caso seja uma matriz, a quantidade de colunas é padrão
        self.cols = len(matriz_base[0])
      # a quantidade de linhas é essa daí mesmo
      self.lins = len(matriz_base)
      # e faz a conversão
      self.__converter(matriz_base, False if self.cols == 1 else True)
    # verifica se a lista de colunas tem algo
    elif len(colunas) > 0:
      # seta a quantidade de colunas da matriz
      self.cols = len(colunas)
      # percorre os vetores
      for col,v in enumerate(colunas):
        # percorre os componentes de cada coluna e vai adicionando
        # como a quantidade de linhas será a mesma de A, é necessário te-la passado
        for i in range(self.lins):
          if v[i,0] != 0: self.matriz[i, col] = v[i,0]

  def __converter(self, matrizBase, matriz=True):
    """
      Aqui pode ser feita a conversão de uma matriz da forma de lista para uma
      do tipo `MatrizDict` durante o instanciamento da classe.
    """
    if matriz:
      for i in range(self.lins):
        for j in range(self.cols):
          # se não for nulo, adiciona ao dict
          if matrizBase[i][j] != 0:
            self[i, j] = matrizBase[i][j]
    else:
      try:
        for i in range(self.lins):
            if matrizBase[i][0] != 0:
                self[i, 0] = matrizBase[i][0]
      except:
        for i in range(self.lins):
            if matrizBase[i] != 0:
                self[i, 0] = matrizBase[i]


  # exibição da matriz
  def __str__(self):
    """Função que deixa a matriz bonitinha na hora do print."""
    # onde vai ser armazenada a string
    str_final = ""
    # percorre as linhas
    for i in range(self.lins):
      str_final += "[   "
      # percorre as colunas
      for j in range(self.cols):       
        str_final += f"{self[i,j]}   "
      str_final += "]\n" if i < self.lins - 1 else "]"
    return str_final

  # funcionalidades básicas de uma matriz
  def __getitem__(self, indice):
    """Capturar elementos da matriz é o mínimo."""
    # verifica se o índice está na lista de chaves do dicionário
    if indice in self.matriz.keys():
      # se for o caso, retorna isso
      return self.matriz[indice]
    # se não for o caso mas o índice estiver no escopo da matriz, retorna 0
    elif 0 <= indice[0] < self.lins and 0 <= indice[1] < self.cols:
      return 0
    # se não for o caso novamente, então o índice não faz parte da matriz
    else:
      raise Exception("O índice informado não faz parte da matriz.")
  
  def __setitem__(self, indice, valor):
    """Ser capaz de alterar um valor da matriz também é básico."""
    # caso o valor seja nulo
    if valor == 0: 
      # verifica se tinha algo no lugar
      if indice in self.matriz.keys():
        self.matriz.pop(indice, None)
      return
    # verifica se o índice está compreendido na matriz
    if 0 <= indice[0] < self.lins and 0 <= indice[1] < self.cols:      
      # se for o caso, atribui
      self.matriz[indice] = valor
    # caso não, dá erro
    else:
      raise Exception("O índice informado não faz parte da matriz.")

  def __len__(self):
    return self.lins
      
  # algumas operações unárias a seguir
  def T(self):
    """
      Retorna a transposta da matriz.
    """
    # cria uma nova matriz
    transposta = MatrizDict(lins=self.cols, cols=self.lins)
    # a transposta vai ser a troca de índices
    for i in range(self.lins):
      for j in range(self.cols):
        if self[i,j] != 0:
          transposta[j,i] = self[i,j]
    return transposta

  # algumas operações binárias à seguir
  def __add__(self, m2):
    # verifica se elas tem o mesmo tamanho e dá erro se não tiverem
    if self.lins != m2.lins or self.cols != m2.cols:
      raise Exception("As matrizes não têm o mesmo tamanho.")
    
    # matriz onde será armazenado o resultado
    resultado_soma = MatrizDict(lins=self.lins, cols=self.cols)
    # percorre as linhas
    for i in range(self.lins):
      # percorre as colunas
      for j in range(self.cols):
        soma = self[i,j] + m2[i,j]
        # caso a soma não seja nula, adiciona
        if soma != 0: resultado_soma[i,j] = soma
    
    return resultado_soma

  def __sub__(self, m2):
    """
      Como a subtração é só uma soma com sinais invertidos, a m2 é multiplicada
      por -1 e é realizada a soma.
    """
    negativa = -1 * m2
    return self + negativa

  def prod(self, m2):
    """
      Aqui a multiplicação pode ser por uma matriz ou por um escalar. O primeiro
      caso é sempre mais complicado, mas será feito.
    """
    # se for um número
    if type(m2) in (int, float):
      # matriz de resultado
      resultado_produto = MatrizDict(lins=self.lins, cols=self.cols)
      # percorre as linhas
      for i in range(self.lins):
        # percorre as colunas
        for j in range(self.cols):
          resultado_produto[i,j] = self[i,j]*m2
      return resultado_produto
    # se não for
    else:
      # verifica se possuem as condições suficientes
      if self.cols != m2.lins:
        raise Exception("Não é possível fazer a multiplicação.")
      # cria uma nova matriz
      matriz_produto = MatrizDict(lins=self.lins, cols=m2.cols)

      for i in range(self.lins):
          for j in range(m2.cols):
            # soma dos produtos no elemento na linha i e coluna j
            soma = sum([
                        self[i,r]*m2[r,j] for r in range(m2.lins)
            ])
            matriz_produto[i,j] = soma
              
      return matriz_produto

  def __mul__(self, m2):
    """
      Aqui a multiplicação pode ser por uma matriz ou por um escalar. O primeiro
      caso é sempre mais complicado, mas será feito.
    """
    # se for um número
    if type(m2) in (int, float):
      # matriz de resultado
      resultado_produto = MatrizDict(lins=self.lins, cols=self.cols)
      # percorre as linhas
      for i in range(self.lins):
        # percorre as colunas
        for j in range(self.cols):
          resultado_produto[i,j] = self[i,j]*m2
      return resultado_produto
    # se não for
    else:
      # verifica se possuem as condições suficientes
      if self.cols != m2.lins:
        raise Exception("Não é possível fazer a multiplicação.")
      # cria uma nova matriz
      matriz_produto = MatrizDict(lins=self.lins, cols=m2.cols)

      # o r vai percorrer todas as colunas da linha i da self que não são nulas
      # inter as linhas da coluna j da m2 que não são nulas
      # separa num dict por linha
      dict1 = {}
      for x, y in self.matriz.keys(): dict1.setdefault(x, set()).add(y)

      dict2 = {}
      for x, y in m2.matriz.keys(): dict2.setdefault(y, set()).add(x)      

      for i in dict1:
          for j in dict2:
            # soma dos produtos no elemento na linha i e coluna j
            soma = sum([
                        self[i,r]*m2[r,j] for r in dict1[i].intersection(dict2[j])
            ])
            matriz_produto[i,j] = soma
              
      return matriz_produto

  def __rmul__(self, m2):
    """
      Como pode ocorrer de querer multiplicar um número por uma matriz e não o
      inverso, é preciso usar isso daqui, que na real só vai inverter a ordem e
      chamar a função certa.
      Como este só é chamado se `m2` não possuir uma multiplicação bem definida,
      não há interferência no caso de `m2` ser outra matriz.
    """
    return self * m2

  def __div__(self, escalar):
    """
      A divisão só pode ser feita por um escalar não nulo, e ela será o produto
      da matriz pelo inverso desse escalar.
    """
    return self * (1/escalar)

  # isso daqui pode ajudar
  def componentes(self):
    """
      Retorna os vetores (matrizes coluna) da matriz. Pode ocorrer de precisar
      deles e para não ficar sempre fazendo a mesma coisa seria conveniente um
      método que os fornecesse. 
      No entanto, para seguir a ideia de poupar espaço, seria útil conceber esses
      vetores também como dicts. Vejamos se funciona!
    """
    # vetores
    v = {}
    # percorre as colunas
    for j in range(self.cols):
      v[j] = MatrizDict([self[i,j] for i in range(self.lins)])
    return v   

  def setcol(self, col, vetor):
    """
      Permite substituir uma determinada coluna da matriz por um vetor-coluna passado.
    """
    for i in range(vetor.lins):
      if vetor[i,0] != 0:
        self[i,col] = vetor[i,0]

  def col(self, indice):
    """
      Captura uma coluna da matriz
    """
    return MatrizDict([self[i,indice] for i in range(self.lins)])

  def subM(self, int_lin:list, int_col:list):
    """
        Captura uma submatriz da matriz principal.
        Ambos os intervalos são do tipo [-,-).
    """
    subMatriz = []
    # linhas
    for lin in range(int_lin[0], int_lin[1]):
        subMatriz.append([])
        for col in range(int_col[0], int_col[1]):
            subMatriz[-1].append(self[lin,col])
    return MatrizDict(subMatriz)

  def substM(self, int_lin:list, int_col:list, M):
    """
      Substitui uma submatriz da matriz completa por outra submatriz de outra matriz completa.
    """
    for i in range(int_lin[1]-int_lin[0]):
      for j in range(int_col[1]-int_col[0]):
        self[int_lin[0]+i,int_col[0]+j] = M[i,j]

  def lista(self):
    """
      Retorna a matriz no formato de lista.
    """
    lista = [[
      self[i,j] for j in range(self.cols)
    ] for i in range(self.lins)]
    return lista