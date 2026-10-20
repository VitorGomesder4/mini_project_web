const botaologin = document.getElementById("login");
const janelaModalLogin = document.getElementById("modallogin"); 
const botaofecharLogin = document.getElementById("fecharLogin");
const formulario = document.getElementById("formlogin");

botaologin.addEventListener("click", function(event){
    if(janelaModalLogin.hidden){
        janelaModalLogin.hidden = false
    }else{
        janelaModalLogin.hidden = true
    }
})

botaofecharLogin.addEventListener("click", function(event){
    janelaModalLogin.hidden = true
})

janelaModalLogin.addEventListener("submit", function(event){
    event.preventDefault();

    logar(formulario);
})

function logar(formulario){
    const loginCredential = formulario.querySelector("#logininput").value.trim();
    const passwordCredential = formulario.querySelector("#password").value.trim();

    console.log(loginCredential, passwordCredential);
    console.log(typeof(loginCredential), typeof(passwordCredential));

    const data = {
        loginCredential: loginCredential,
        passwordCredential: passwordCredential
    };

    fetch("login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    .then(response => response.json())
    .then(data => {
        console.log(data.message, data.redirect);

        if(data.redirect){
            window.location.href = data.redirect;
        }
    })

    .catch(error => {
        console.error("Erro de requisição", error);
    })
}