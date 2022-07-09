### Matrizes "prontas" do tipo quadrado mágico e de Hilbert que podem ser geradas na hora

# suas geradores estão no arquivo matrizes_exemplos
from matrizes_exemplos import magica, hilbert
# módulos de JS
import js
from pyodide import create_proxy, to_js

# para utilizar novamente o create_proxy, pode-se criar uma função auxiliar
def auxiliar_matrizPronta(gerador):
    """ 
        Esta função monta uma matriz do tipo `quadrado mágico` ou `hilbert` de tamanho informado no input da web e substitui nos outros inputs, bastando então pressionar o botão de "rodar".
    """
    # captura o tamanho
    n = int(js.document.getElementById("tamanho_matriz").value)
    # faz a matriz
    M = gerador(n)
    # substitui nos inputs
    for i in range(M.lins):
        for j in range(M.cols):
            js.document.getElementById(f"matriz_{i}_{j}").value = M[i,j]

# configura o evento a ser chamado quando se pressiona o botão de gerar matriz do tipo quadrado mágico
rodar_quadradoMagico = create_proxy(lambda _: auxiliar_matrizPronta(magica))
js.document.getElementById('rodar_quadradoMagico').addEventListener("click", rodar_quadradoMagico)

# configura o evento a ser chamado quando se pressiona o botão de gerar matriz do tipo Hilbert   
rodar_hilbert = create_proxy(lambda _: auxiliar_matrizPronta(hilbert))
js.document.getElementById('rodar_hilbert').addEventListener("click", rodar_hilbert)