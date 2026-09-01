CREATE DATABASE webSite_testes;

CREATE TABLE USER (
    id_user INT NOT NULL,
    nome VARCHAR(150),
    dt_nascimento DATE,
    sexo CHAR(1)
);

ALTER TABLE USER ADD CONSTRAINT pk_id_user PRIMARY KEY (id_user);