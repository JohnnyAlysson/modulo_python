-- Crie um banco de dados chamado "escola" e as seguintes tabelas: 
-- Tabela "alunos" com colunas: 
-- id_aluno, nome, idade.
-- Tabela " cursos" 
-- com colunas: id_curso, nome_curso,carga_horaria. 
--Tabela "matriculas" com colunas:
-- id_matricula , id_aluno id_curso, data_matricula.

CREATE DATABASE IF NOT EXISTS  escola; --CRIANDO BANCO DE DADOS
USE escola; -- USAR BANCO DE DADOS "escola"
CREATE TABLE alunos( --Criar tabela alunos
  id_aluno int,
  nome varchar(40), -- definir quantidade maxima do var char
  idade int,
);
CREATE TABLE cursos( --criar tabela cursos
  id_curso int,
  nome_curso varchar(40),
)
CREATE TABLE matriculas(
  id_matricula int,
  id_aluno int,
  id_curso int,
  data_matricula date,
)
