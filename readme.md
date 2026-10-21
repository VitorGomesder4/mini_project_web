
# 🚀 Mini web project

> Um repositório para praticar desenvolvimento web

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## Demonstração do projeto

[https://youtu.be/vneP5_3VjDg](https://youtu.be/vneP5_3VjDg)

## ✨ Funcionalidades

- Visualizar banco de dados
- Analise de dados (Ainda não implementado)
- Cadastro e login

## 🛠️ Tecnologias utilizadas

- **Flask** — [Protocolo HTTP]
- **Mariadb** — [Banco de dados]
- **JavaScript** — Interatividade e Fetch

## ⚙️ Como executar

Clone o repositório:

```bash
git clone git@github.com:VitorGomesder4/mini_project_web.git
cd /caminho/projeto
```

Instale o Python:

```bash
https://www.python.org/
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale e configure MariaDB:

```bash
https://mariadb.org/

tutorial windows: https://www.youtube.com/watch?v=zcS3tZCLf7U
```

Criar banco:

```bash
Inicie o serviço de mariadb
mariadb -u root -p
Crie um novo banco chamado website_testes
use website_testes
Rode o ddl de database/create_ddl.sql
```

Execute o projeto:

```bash
python app.py
```

## 📁 Estrutura do projeto

```text
mini_project_web/
├── database/
├── models/
├── routes/tabelas/
├── static/css/
├── static/js/
├── templates/
├── app.py
├── .env
├── database.py
├── README.md
├── .gitignore
└── requirements.txt
```

## 🧠 Aprendizados

- Programação orientada a eventos
- Uso de Blueprints no Flask

## 👨‍💻 Autor

**Vitor Gomes**

[GitHub](https://github.com/vitorgomesder4)

---

Desenvolvido como projeto pessoal.
