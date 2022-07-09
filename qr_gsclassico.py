from matrizes import MatrizDict
from normas import norma2

def GSClassico(X)->list:
    """
        Método de Gram-Schmidt Clássico para o cálculo da forma reduzida QR de uma matriz X.
    """
    # número de linhas e de colunas
    m,n = X.lins, X.cols
    # instancia as matrizes
    Q = MatrizDict([[0 for i in range(n)] for j in range(m)]) # Q_{m x n}
    R = MatrizDict([[0 for i in range(n)] for j in range(n)]) # R_{n x n}
    # percorre as colunas
    for k in range(n):
        # torna a coluna k de Q igual a coluna k de X
        Q.setcol(k, X.col(k))

        if k != 0:
            # produto Q[:,k-1]'*Q[:,k]
            qtq = (Q.col(k-1).T() * Q.col(k))[0,0]
            
            for j in range(k-1):
                # substitui na matriz R
                R[j,k] = qtq    

            # nova coluna de Q
            novaCol = Q.col(k) - Q.subM([0,Q.lins],[0,k-1])*R.subM([0,k-1],[k,k+1])
            # altera a coluna de Q
            Q.setcol(k, novaCol)

        # calcula a norma
        nQ_k = norma2(Q.col(k))
        # substitui em R
        R[k,k] = nQ_k
        # substitui a coluna de Q
        Q.setcol(k, Q.col(k)*(1/nQ_k))

    return Q, R