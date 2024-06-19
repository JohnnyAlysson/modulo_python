-- DESAFIO PRÁTICO
-- Sistema de uma escola
-- Crie um banco de dados para um sistema de uma escola,
-- esse banco de dados ficará responsável por persistir os
-- dados sobre alunos, professores, turmas e disciplinas.

-- Para os alunos é importante que contenha um número de
-- matrícula, o nome, a idade, e o endereço.

-- Para os professores, deverá conter um número de
-- matrícula, nome, especialidade e endereço.

-- Para a turma deverá conter um identificador, horário de
-- início e dia de semana.

-- Para disciplina é importante que contenha um
-- identificador, nome e quantidade de aulas.

CREATE DATABASE IF NOT EXISTS escola;
USE escola;
CREATE TABLE alunos(
  id_matricula int,
  nome varchar(40),
  idade smallint,
  endereço varchar(80)
);

CREATE TABLE professores( 
  id_matricula int,
  nome varchar(40),
  especialidade varchar(20),
  endereço varchar(80)
);

CREATE TABLE turmas( 
  id_turma int,
  inicio smallint,
  dia_da_semana varchar(20)
);

CREATE TABLE disciplinas(
  id_disciplina int,
  nome varchar(40),
  n_de_aulas smallint
)