-- Crie uma tabela
-- "pedidos " com as colunas "id_pedido " , "id_cliente " e "data_pedido ". 
-- Adicione uma constraint de chave estrangeira na coluna "id_cliente "
-- para garantir que um pedido só possa ser feito por um cliente existente na tabela " clientes ".
CREATE DATABASE IF NOT EXISTS restaurante;
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(100) NOT NULL
);
CREATE TABLE pedidos(
  id_pedido INT PRIMARY KEY AUTO_INCREMENT,,
  id_cliente INT,
  data_pedido DATE,
  CHECK (id_cliente in clientes),

)
