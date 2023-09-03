-- criação do banco --
drop database ecommerce;
create database ecommerce;
use ecommerce;

-- criação das tabelas
create table cliente(
	idCliente int auto_increment primary key,
    nomeCliente varchar(10),
    snomeCliente varchar(20),
    CPF char(11) not null,
    constraint unique_cpf_client unique(CPF)
);

alter table cliente auto_increment = 1;

create table produto(
	idProd int auto_increment primary key,
    nomeProd varchar(10) not null,
    categoriaProd enum('Eletrônico', 'Roupas', 'Brinquedos','Alimentos') not null,
    avaliacaoProd float default 0
);

alter table produto auto_increment = 1;

create table pedido(
	idPed int auto_increment primary key,
    idPedCliente int,
    statusPed enum('Cancelado','Confirmado','Em processamento') default 'Em processamento',
    descricaoPed varchar(255),
    valorFrete float default 10,
    constraint fk_pedCliente foreign key(idPedCliente) references cliente(idCliente)
);

alter table pedido auto_increment = 1;

create table estoque(
		idEst int auto_increment primary key,
        localEst varchar(255),
        qtdEst int default 0
);

alter table estoque auto_increment = 1;

create table fornecedor(
	idForn int auto_increment primary key,
    razaoForn varchar(255) not null,
    CNPJ char(15) not null,
    contatoForn char(11) not null,
    constraint unique_fornecedor unique(CNPJ)
);

alter table fornecedor auto_increment = 1;

create table vendedor(
	idVend int auto_increment primary key,
    nomeVend varchar(255) not null,
    nomeFantVend varchar(255),
    CNPJ char(15) not null,
    CPF char(11) not null,
    localVend varchar(255),
    contatoFor char(11) not null,
    constraint unique_CNPJ_vend unique(CNPJ),
    constraint unique_CPF_vend unique(CPF)
);

alter table vendedor auto_increment = 1;

create table vendProd(
	idVendProd int,
    idProd int,
    qtdProd int default 1,
    primary key (idVendProd, idProd),
    constraint fk_vendProd_vend foreign key (idVendProd) references vendedor(idVend),
    constraint fk_vendProd_prod foreign key (idProd) references produto(idProd)
);

create table pedProd(
	idPedProd int,
    idPed int,
    qtdPed int default 1,
    statusPedProd enum('Disponível','Sem estoque') default 'Disponível',
    primary key (idPedProd, idPed),
    constraint fk_pedProd_prod foreign key (idPedProd) references produto(idProd),
    constraint fk_pedProd_ped foreign key (idPed) references pedido(idPed)
);

create table localEst(
	idLocalEst int,
    idLocalProd int,
    location varchar(255) not null,
    primary key (idLocalEst, idLocalProd),
    constraint fk_localEst_prod foreign key (idLocalProd) references produto(idProd),
    constraint fk_localEst_est foreign key (idLocalEst) references estoque(idEst)
);

CREATE TABLE prodForn (
    idProdForn INT,
    idProd INT,
    qtdProd INT NOT NULL,
    PRIMARY KEY (idProdForn , idProd),
    CONSTRAINT fk_prodForn_forn FOREIGN KEY (idProdForn)
        REFERENCES fornecedor (idForn),
    CONSTRAINT fk_idProdForn_prod FOREIGN KEY (idProd)
        REFERENCES produto (idProd)
);

show tables;