
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario SERIAL PRIMARY KEY,
    email varchar(100) UNIQUE NOT NULL,
    senha varchar(100) NOT NULL,
    data_cadastro TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente SERIAL PRIMARY KEY,
    id_usuario INTEGER UNIQUE NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    sexo CHAR(1) NOT NULL,
    data_nascimento DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS vendedor (
    id_vendedor SERIAL PRIMARY KEY,
    id_usuario INTEGER UNIQUE NOT NULL,
    nome_loja VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS endereco (
    id_endereco SERIAL PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    estado CHAR(2) NOT NULL,
    cidade VARCHAR(30) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    rua VARCHAR(100) NOT NULL,
    numero varchar(10),

);


CREATE TABLE IF NOT EXISTS telefone (
    id_telefone SERIAL PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    tipo tipo_telefone NOT NULL DEFAULT 'CELULAR',
    numero VARCHAR(15) NOT NULL
);


CREATE TABLE IF NOT EXISTS produto (
    id_produto SERIAL PRIMARY KEY,
    id_vendedor INTEGER NOT NULL,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    categoria categoria_nome NOT NULL DEFAULT 'ALIMENTOS',
    preco_atual DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS estoque (
    id_estoque SERIAL PRIMARY KEY,
    id_produto INTEGER NOT NULL,
    quantidade_atual INTEGER NOT NULL DEFAULT 0
);



CREATE TABLE IF NOT EXISTS pedido (
    id_pedido SERIAL PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    id_endereco_entrega INTEGER NOT NULL,
    data_hora TIMESTAMPTZ DEFAULT NOW(),
    status_geral status_pedido NOT NULL DEFAULT 'PENDENTE'

);


CREATE TABLE IF NOT EXISTS produto_pedido (
    id_produto_pedido SERIAL PRIMARY KEY,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario_pago DECIMAL(10,2) NOT NULL
);