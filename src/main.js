// quando o botão for pressionado, faz alguma coisa
document.getElementById("rodar").onclick = () => {
    rodar(document.getElementById("tamanho_matriz").value, document.getElementById("tamanho_matriz").value)
}

document.getElementById("rodar_quadradoMagico").onclick = () => {
    rodar(document.getElementById("tamanho_matriz").value, document.getElementById("tamanho_matriz").value)
}
document.getElementById("rodar_hilbert").onclick = () => {
    rodar(document.getElementById("tamanho_matriz").value, document.getElementById("tamanho_matriz").value)
}

rodar(3,3)

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