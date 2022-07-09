// RODA POR PADRÃO COM 3X3
rodar(3,3)

// input pelo qual é inserido o tamanho da matriz
const inputTamanho = document.getElementById("tamanho_matriz")

// quando o botão for pressionado, faz alguma coisa
document.getElementById("rodar").onclick = () => {
    let tamanho = inputTamanho.value
    rodar(tamanho, tamanho)
}
document.getElementById("rodar_quadradoMagico").onclick = () => {
    let tamanho = inputTamanho.value
    rodar(tamanho, tamanho)
}
document.getElementById("rodar_hilbert").onclick = () => {
    let tamanho = inputTamanho.value
    rodar(tamanho, tamanho)
}

// função que faz os ziriguidum 
function rodar(qntd_linhas, qntd_colunas){
    // captura elemento tabela
    const tabela = document.getElementById("tabela_matriz")
    // limpa
    tabela.innerHTML = ""
    // adiciona a quantidade de inputs que for necessária
    for(let i = 0; i < qntd_linhas; i++){
        // cria o elemento tr
        let tr = document.createElement("tr")
        // percorre as colunas
        for(let j = 0; j < qntd_colunas; j++){
            // cria o elemento td
            let td = document.createElement("td")
            // cria o input
            let input = document.createElement("input")
            input.type = "number"
            input.classList.add("elemento_ij") // classe especial
            // cria um id para o input
            input.id = `matriz_${i}_${j}`
            // adiciona ao td
            td.appendChild(input)
            // adiciona o td ao tr
            tr.appendChild(td)
        }
        // adiciona o tr a table
        tabela.appendChild(tr)
    }  
}

// função que retorna os valores
function valores(){
    // instancia a lista de linhas
    let matriz = []
    // captura as trs
    let trs = document.getElementById("tabela_matriz").children;
    // percorre
    for(let i = 0; i < trs.length; i++){
        // instancia a lista de colunas
        let cols = []
        // lista de tds
        let tds = trs[i].children;
        // percorre
        for(let j = 0; j < tds.length; j++){
            // o input vai ser o 1º e único filho
            let valor = tds[j].firstChild.value;
            cols.push(valor)
        }
        matriz.push(cols)
    }   
    console.log(matriz)
    return matriz 
}

// função para criar tabelas como matrizes, só pra facilitar
function tabela(idTabela, matriz, arredondar=3){
    // cria uma div que vai ter a classe div_tabela
    let div = document.createElement("div")
    div.classList.add('div_tabela')
    // cria uma tabela
    let tabela = document.createElement("table")
    tabela.id = idTabela
    // percorre as linhas da matriz
    for(let i = 0; i < matriz.length; i++){
        // cria um tr para a linha
        let tr = document.createElement("tr")
        // percorre as colunas da linha da matriz
        for(let j = 0; j < matriz[i].length; j++){
            // cria um td para a coluna
            let td = document.createElement("td")
            // seta o valor
            td.innerText = `${Math.round(matriz[i][j]*Math.pow(10, arredondar))/Math.pow(10, arredondar)}`
            // adiciona o td ao tr
            tr.appendChild(td)
        }
        // adiciona o tr à table
        tabela.appendChild(tr)
    }
    // adiciona a tabela à div
    div.appendChild(tabela)
    // retorna a div
    return div
}

function exibirMatrizes(dict_info){
    // SEÇÃO GERAL
    let secao = document.getElementById("resultados")
    // PERCORRE OS RESULTADOS
    for (let [metodo, obj] of dict_info){
        // CRIA UM H3 PARA O TÍTULO
        let h3 = document.createElement("h3")
        h3.innerText = metodo
        secao.appendChild(h3)
        
        // TEREMOS UMA DIV COM 3 MATRIZES: A = QR
        let divMatrizes = document.createElement("div")
        divMatrizes.classList.add("divMatrizes")
        // CRIA UMA DIV PARA CADA UMA
        let divA = tabela(`${metodo}_A`, obj.get("matriz"))
        let divQ = tabela(`${metodo}_Q`, obj.get("Q"))
        let divR = tabela(`${metodo}_R`, obj.get("R"))
    
        // adiciona
        divMatrizes.appendChild(divA)
        divMatrizes.innerHTML += ' = '
        divMatrizes.appendChild(divQ)
        divMatrizes.innerHTML += ' * '
        divMatrizes.appendChild(divR)
    
        // adiciona a div_matriz à secao
        secao.appendChild(divMatrizes)
    }
}

function margens(idTabela, campo, dict_info){
    // captura a tabela
    let tabela = document.getElementById(idTabela)

    for (let [norma, val] of dict_info.get("Gram-Schmidt Clássico").get(campo)){
        // caso já exista, só copia
        if(document.getElementById(campo+norma)){
            tr = document.getElementById(campo+norma)
            tr.innerHTML = ""
        }
        // senão, cria um tr para a norma
        else{
            var tr = document.createElement("tr")
            tr.id = campo+norma
        }
        
        // td para o nome da norma
        // td para o nome da norma
        let td = document.createElement("td")
        td.innerText = norma
        tr.appendChild(td)

        // percorre os métodos
        for (let [metodo, obj] of dict_info){
            // td para o valor do método
            let td = document.createElement("td")
            // o valor que aparecerá será de "margem QR"
            let valor = obj.get(campo).get(norma)
            td.innerText = valor > 1 ? Math.round(valor * Math.pow(10,4))/Math.pow(10,4) : valor
            // adiciona à tr
            tr.appendChild(td)
        }
        // adiciona o tr à tabela
        tabela.appendChild(tr)
    }
}

function tabelaConsumo(dict_info){
    // tabela de consumo
    let tabela_consumo = document.getElementById("tabela_consumo")
    // percorre os métodos
    for (let [metodo, obj] of dict_info){
        // cada método tem uma tr
        var tr = document.createElement("tr")
        tr.id = "consumo_" + metodo

        // verifica se já existe
        if(document.getElementById("consumo_" + metodo)){
            tr = document.getElementById("consumo_" + metodo)
            tr.innerHTML = ""
        }
        
        // uma td será para o nome do método
        var td = document.createElement("td")
        td.innerText = metodo
        tr.appendChild(td)

        // a segunda será para o tempo gasto
        var td = document.createElement("td")
        td.innerText = Math.round(obj.get('tempo')*Math.pow(10,5))/Math.pow(10,5)
        tr.appendChild(td)

        // adiciona a tr à tabela
        tabela_consumo.appendChild(tr)
    }
}

// FUNÇÃO PARA EXIBIR OS RESULTADOS
function exibirResultados(dict_info){
    // exibe as matrizes
    exibirMatrizes(dict_info)

    // margens de erro para A - QR
    margens("tabela_AQR", "margem QR", dict_info)

    // margens de erro para I - QtQ
    margens("tabela_QtQ", "margem QtQ", dict_info)

    // consumo (tempo apenas, por enquanto)
    tabelaConsumo(dict_info)    
}