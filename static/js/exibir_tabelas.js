const tabela = document.getElementById("tabela");
const botao_exibir = document.getElementById("mostrar_tabela");

const tabelas = [
    document.getElementById("usuarios_option"),
    document.getElementById("planos_option"),
    document.getElementById("assinaturas_option"),
    document.getElementById("historico_planos_option")
];

tabela.addEventListener("change", function() {
    tabelas.forEach(function(elemento) {
        elemento.hidden = true;
    });

    const selecionada = document.getElementById(tabela.value + "_option");
    selecionada.hidden = false;
});

botao_exibir.addEventListener("click", function(event){
    const data = {tabela: tabela.value}
})