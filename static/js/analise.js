const selectPlano = document.getElementById("select_plano");

async function carregarPlanos() {
    try {
        const resposta = await fetch("/planos?inicio=0&fim=100");
        const planos = await resposta.json();

        planos.forEach(function (plano) {
            const opcao = document.createElement("option");
            opcao.value = plano.id_plano;
            opcao.textContent = `${plano.id_plano} - ${plano.nome_plano}`;
            selectPlano.appendChild(opcao);
        });
    } catch (erro) {
        console.error("Erro ao carregar os planos:", erro);
    }
}

async function carregarGrafico(url, divId, botao) {
    const div = document.getElementById(divId);

    if (!selectPlano.value) {
        div.textContent = "Selecione um plano antes de gerar o gráfico.";
        return;
    }

    botao.disabled = true;

    try {
        const resposta = await fetch(`${url}?id_plano=${selectPlano.value}`);
        const dados = await resposta.json();

        if (!resposta.ok) {
            throw new Error(dados.message || "Erro ao buscar o gráfico.");
        }

        Plotly.newPlot(div, dados.data, dados.layout);

    } catch (erro) {
        console.error("Erro ao carregar o gráfico:", erro);
        div.textContent = erro.message;
    } finally {
        botao.disabled = false;
    }
}

const botaoRegressao = document.getElementById("mostrar_grafico");
botaoRegressao.addEventListener("click", function () {
    carregarGrafico("/analise_regressiva", "grafico_regressao", botaoRegressao);
});

const botaoMultipla = document.getElementById("mostrar_grafico_multipla");
botaoMultipla.addEventListener("click", function () {
    carregarGrafico("/analise_multipla", "grafico_multipla", botaoMultipla);
});

selectPlano.addEventListener("change", async function () {
    await carregarGrafico("/analise_regressiva", "grafico_regressao", botaoRegressao);
    await carregarGrafico("/analise_multipla", "grafico_multipla", botaoMultipla);
});

carregarPlanos();