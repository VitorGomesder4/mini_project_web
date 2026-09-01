const formulario = document.getElementById("registro");  //pegando o formulario como objeto

formulario.addEventListener("submit", function(event) { //Adicionando listener para executar registro
    event.preventDefault();

    registrar(formulario);
});

function registrar(formulario){ //Registro onde é checado se o formulario foi preenchido
    const nome = formulario.querySelector("#nome").value.trim();
    const data_nascimento = formulario.querySelector("#data_nascimento").value;
    let sexo;

    try{
        sexo = formulario.querySelector("input[name='sexo']:checked").value;
    } catch(TypeError){
        sexo = "";
    }
    
    let valido = false; //Validade para ser usado o fetch no futuro

    console.log(nome, data_nascimento, sexo);
    console.log(typeof(nome), typeof(data_nascimento), typeof(sexo));

    if (nome !== ""){
        valido = true;
        console.log("Valido", true);

        const data = {      //juntando dados para envio no formato json
            nome: nome,
            data_nascimento: data_nascimento,
            sexo: sexo
        };

        fetch("/registrar", {    //fetch para rota registrar
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

    } else {
        console.log("Não Valido", false);
    }
}