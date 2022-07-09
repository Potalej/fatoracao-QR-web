"""
    Este arquivo faz funcionar toda a parte de Python.
"""

from calculos import calculos # função que faz os cálculos necessários
import matrizes_prontas # só de importar já faz funcionar
import js # módulo de JS
from pyodide import create_proxy, to_js # módulo de JS

def rodando(_):
    """
        Esta função é chamada quando o botão de "rodar" é pressionado. Ela limpa os resultados anteriores, captura a matriz e chama os novos cálculos.
    """
    # limpa a área de matrizes para caso haja alguma rodada anterior
    js.document.getElementById("resultados").innerHTML = ""
    
    # captura a matriz
    matriz = js.valores().to_py()
    # converte os valores para float
    matriz = [[ float(coluna) if coluna != "" else 0 for coluna in linha] for linha in matriz]
    
    # faz os cálculos
    dict_info = calculos(matriz)

    # agora é preciso passar as informações para o js dar conta
    js.exibirResultados(to_js(dict_info))

# a função create_proxy permite adicionar como um evento a ser chamado uma função do python
proxy_rodando = create_proxy(rodando)
# quando o botão de calcular é pressionado, a função `rodando` é chamada.
js.document.getElementById('calcular').addEventListener("click", proxy_rodando)