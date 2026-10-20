const tabela = document.getElementById("tabela");
const botao_exibir = document.getElementById("mostrar_tabela");
const mostrar_mais = document.getElementById("mostrar_mais");
const anterior = document.getElementById("anterior");

// Paginação
let inicio = 0;
const registrosPorPagina = 20;
let paginaAtual = 1;

// Configurações das tabelas
const configuracoes = {
    usuarios: {
        corpo: "dados_usuarios",
        colunas: ["id_user_site", "username", "email"]
    },
    planos: {
        corpo: "dados_planos",
        colunas: [
            "id_plano",
            "nome_plano",
            "preco_mensal",
            "qualidade_video",
            "telas_simultaneas"
        ]
    },
    assinaturas: {
        corpo: "dados_assinaturas",
        colunas: [
            "id_assinatura",
            "id_user_site",
            "id_plano",
            "data_inicio",
            "data_fim",
            "status"
        ]
    },
    historico_planos: {
        corpo: "dados_historico_planos",
        colunas: [
            "id_historico",
            "id_plano",
            "mes_referencia",
            "preco_mensal",
            "quantidade_assinantes"
        ]
    }
};

// Tabelas HTML
const tabelas = [
    document.getElementById("usuarios_option"),
    document.getElementById("planos_option"),
    document.getElementById("assinaturas_option"),
    document.getElementById("historico_planos_option")
];

// Elemento que exibe a página atual
const textoPagina = document.querySelector("span");

// Controla os botões da paginação
function atualizarBotoes(quantidadeRegistros) {
    anterior.disabled = paginaAtual === 1;
    mostrar_mais.disabled = quantidadeRegistros < registrosPorPagina;
}

// Carrega os dados da tabela selecionada
async function carregarTabela() {
    const nomeTabela = tabela.value;
    const config = configuracoes[nomeTabela];

    if (!config) return;

    botao_exibir.disabled = true;

    try {
        const resposta = await fetch(
            `/${nomeTabela}?inicio=${inicio}&fim=${inicio + registrosPorPagina}`
        );

        if (!resposta.ok) {
            throw new Error("Erro ao buscar os dados da tabela.");
        }

        const dados = await resposta.json();
        const corpoTabela = document.getElementById(config.corpo);

        // Limpa os registros anteriores
        corpoTabela.innerHTML = "";

        // Cria as linhas e células
        dados.forEach(function (registro) {
            const linha = document.createElement("tr");

            config.colunas.forEach(function (coluna) {
                const celula = document.createElement("td");
                celula.textContent = registro[coluna] ?? "";
                linha.appendChild(celula);
            });

            corpoTabela.appendChild(linha);
        });

        // Atualiza a página e os botões
        textoPagina.textContent = `Página ${paginaAtual}`;
        atualizarBotoes(dados.length);

    } catch (erro) {
        console.error("Erro ao carregar a tabela:", erro);
    } finally {
        botao_exibir.disabled = false;
    }
}

// Mostra a tabela selecionada
tabela.addEventListener("change", function () {
    inicio = 0;
    paginaAtual = 1;

    tabelas.forEach(function (elemento) {
        elemento.hidden = true;
    });

    const selecionada = document.getElementById(
        tabela.value + "_option"
    );

    if (selecionada) {
        selecionada.hidden = false;
    }

    textoPagina.textContent = "Página 1";
    anterior.disabled = true;
    mostrar_mais.disabled = false;
});

// Botão para buscar os dados
botao_exibir.addEventListener("click", function () {
    inicio = 0;
    paginaAtual = 1;
    carregarTabela();
});

// Botão para avançar uma página
mostrar_mais.addEventListener("click", function () {
    inicio += registrosPorPagina;
    paginaAtual++;

    carregarTabela();
});

// Botão para voltar uma página
anterior.addEventListener("click", function () {
    if (paginaAtual === 1) return;

    inicio -= registrosPorPagina;
    paginaAtual--;

    carregarTabela();
});

// Estado inicial dos botões
anterior.disabled = true;
mostrar_mais.disabled = false;