const formulario = document.getElementById("cadastro");  //pegando o formulario como objeto

formulario.addEventListener("submit", function(event) { //Adicionando listener para executar registro
    event.preventDefault();

    registrar(formulario);
});

function cadastrar(formulario){ //Cadastro onde é checado se o formulario foi preenchido
    const username = formulario.querySelector("#username").value.trim();
    const email = formulario.querySelector("#email").value.trim();
    const password = formulario.querySelector("#password").value.trim();
    
    let valido = false; //Validade para ser usado o fetch no futuro

    console.log(username, email, password);
    console.log(typeof(username), typeof(email), typeof(password));

    if (username !== "" && password !== ""){
        valido = true;
        console.log("Valido", true);

        const data = {      //juntando dados para envio no formato json
            username: username,
            email: email,
            password: password
        };

        fetch("/cadastrar", {    //fetch para rota registrar
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })

        .then(response => response.json())
        .then(data => {
            console.log(data.message);
        })

        .catch(error => {
            console.error("Erro de requisição:", error);
        });

    } else {
        console.log("Não Valido", false);
    }
}