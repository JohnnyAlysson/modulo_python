-- ATIVIDADE PRÁTICA 2
-- Usando o comando TRUNCATE TABLE, exclua todos os
-- dados da tabela "matriculas"
-- sem excluir a estrutura da
-- tabela.

CREATE DATABASE IF NOT EXISTS  escola; --CRIANDO BANCO DE DADOS
USE escola; -- USAR BANCO DE DADOS "escola"
CREATE TABLE alunos( --Criar tabela alunos
  id_aluno int,
  nome varchar(40), -- definir quantidade maxima do var char
  idade int
);
CREATE TABLE cursos( --criar tabela cursos
  id_curso int,
  nome_curso varchar(40)
)
CREATE TABLE matriculas(
  id_matricula int,
  id_aluno int,
  id_curso int,
  data_matricula date
);
TRUNCATE TABLE matriculas