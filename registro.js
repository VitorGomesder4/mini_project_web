const formulario = document.getElementById("registro");  //pegando o formulaio como objeto

formulario.addEventListener("submit", function(event) { //Adicionando listener para executar registro
    event.preventDefault();

    registrar(formulario);
});

function registrar(formulario){ //Registro onde é checado se o formulario foi preenchido
    const nome = formulario.querySelector("#nome").value.trim();
    const data_nascimento = formulario.querySelector("#data_nascimento").value;
    const sexo = formulario.querySelector("input[name='sexo']:checked").value;
    
    let valido = false; //Validade para ser usado o fetch no futuro

    console.log(nome, data_nascimento, sexo);
    console.log(typeof(nome), typeof(data_nascimento), typeof(sexo));

    if (nome !== "" && data_nascimento !== "" && sexo !== ""){
        valido = true;
        console.log("Valido", true);
    } else {
        console.log("Não Valido", false);
    }
}