CREATE DATABASE webSite_testes;

USE webSite_testes;

CREATE TABLE USER (
    id_user INT NOT NULL,
    nome VARCHAR(150),
    data_nascimento DATE,
    sexo CHAR(1)
);

ALTER TABLE USER ADD CONSTRAINT pk_id_user PRIMARY KEY (id_user);
ALTER TABLE USER MODIFY id_user INT NOT NULL AUTO_INCREMENT;

CREATE TABLE USER_SITE (
    id_user_site INT NOT NULL,
    username VARCHAR(20) NOT NULL,
    email VARCHAR(50),
    password VARCHAR(20) NOT NULL
);

ALTER TABLE USER_SITE ADD CONSTRAINT pk_id_user_site PRIMARY KEY (id_user_site);
ALTER TABLE USER_SITE MODIFY id_user_site INT NOT NULL AUTO_INCREMENT;
ALTER TABLE USER_SITE ADD CONSTRAINT uq_username UNIQUE (username);


CREATE TABLE planos (
    id_plano INT AUTO_INCREMENT PRIMARY KEY,
    nome_plano VARCHAR(30) NOT NULL UNIQUE,
    preco_mensal DECIMAL(10,2) NOT NULL,
    qualidade_video VARCHAR(20),
    telas_simultaneas INT NOT NULL
);

CREATE TABLE assinaturas (
    id_assinatura INT AUTO_INCREMENT PRIMARY KEY,
    id_user_site INT NOT NULL,
    id_plano INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ativa',

    FOREIGN KEY (id_user_site)
        REFERENCES user_site(id_user_site),

    FOREIGN KEY (id_plano)
        REFERENCES planos(id_plano)
);