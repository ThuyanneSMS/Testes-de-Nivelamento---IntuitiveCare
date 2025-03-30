CREATE DATABASE Teste_Banco;
USE Teste_Banco;

-- Tabela de operadoras ativas (com base no header do arquivo operadoras_ativas.csv)

CREATE TABLE operadoras_ativas (
    registro_ans               INTEGER,
    cnpj                       VARCHAR(18),
    razao_social               TEXT,
    nome_fantasia              TEXT,
    modalidade                 TEXT,
    logradouro                 TEXT,
    numero                     TEXT,
    complemento                TEXT,
    bairro                     TEXT,
    cidade                     TEXT,
    uf                         CHAR(2),
    cep                        VARCHAR(10),
    ddd                        VARCHAR(5),
    telefone                   VARCHAR(20),
    fax                        VARCHAR(20),
    endereco_eletronico        TEXT,
    representante              TEXT,
    cargo_representante        TEXT,
    regiao_de_comercializacao  TEXT,
    data_registro_ans          DATE
);

-- Tabela de demonstrações contábeis (com base nos arquivos CSV dos trimestres)

CREATE TABLE demonstracoes_contabeis (
    data                 DATE,
    registro_ans         VARCHAR(10),
    cod_conta            VARCHAR(20),
    descricao            TEXT,
    valor_saldo_inicial  TEXT,
    valor_saldo_final    TEXT
);