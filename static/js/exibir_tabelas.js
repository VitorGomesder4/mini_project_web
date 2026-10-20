const tabela = document.getElementById("tabela");
const botao_exibir = document.getElementById("mostrar_tabela");
let inicio = 0
let fim = 20

const tabelas = [
    document.getElementById("usuarios_option"),
    document.getElementById("planos_option"),
    document.getElementById("assinaturas_option"),
    document.getElementById("historico_planos_option")
];

tabela.addEventListener("change", function() {
    inicio = 0;
    fim = 20;

    tabelas.forEach(function(elemento) {
        elemento.hidden = true;
    });

    const selecionada = document.getElementById(tabela.value + "_option");
    selecionada.hidden = false;
});


botao_exibir.addEventListener("click", function() {
    const nomeTabela = tabela.value;

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

    const config = configuracoes[nomeTabela];

    if (!config) return;

    const corpoTabela = document.getElementById(config.corpo);

    fetch(`/${nomeTabela}?inicio=${inicio}&fim=${fim}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao buscar dados");
            }
            return response.json();
        })
        .then(data => {
            corpoTabela.innerHTML = "";

            data.forEach(function(registro) {
                const linha = document.createElement("tr");

                config.colunas.forEach(function(coluna) {
                    const celula = document.createElement("td");
                    celula.textContent = registro[coluna] ?? "";
                    linha.appendChild(celula);
                });

                corpoTabela.appendChild(linha);
            });
        })
        .catch(error => {
            console.error("Erro ao buscar dados:", error);
        });
});
