import sqlite3
#inicializando banco de dados
db = sqlite3.connect("escola.db")
cursor = banco.cursor()

#tabela p/ dados dos alunos:
comando = """CREATE TABLE Alunos (
codAluno integer PRIMARY KEY NOT NULL
nome text NOT NULL
cpf integer NOT NULL
)"""
cursor.execute(comando)
db.commit()

#tabela p/ dados dos professores:
comando = """
CREATE TABLE Professores (
codProfessor integer PRIMARY KEY NOT NULL,
nome text NOT NULL,
cpf integer NOT NULL
)"""
cursor.execute(comando)
db.commit()

#tabelo para dados das disciplinas:
comando = """
CREATE TABLE Disciplinas (
codDisciplina integer PRIMARY KEY NOT NULL,
nome text NOT NULL,
cargaH text NOT NULL
)"""
cursor.execute(comando)
db.commit()

#tabela para dados das turmas:
comando = """
CREATE TABLE Turmas (
codTurma integer PRIMARY KEY NOT NULL,
titulo text NOT NULL,
ano integer NOT NULL
)"""
cursor.execute(comando)
db.commit()

#tabela de disciplina de cada turma:
comando = """
CREATE TABLE Disc_Turma (
codDisc_Turma integer PRIMARY KEY NOT NULL,
codDisciplina integer NOT NULL,
codProfessor integer NOT NULL,
codTurma integer NOT NULL
)"""
cursor.execute(comando)
db.commit()

#tabela dos históricos:
comando = """
CREATE TABLE Historico (
codHistorico integer PRIMARY KEY NOT NULL,
codAluno integer NOT NULL
)"""
cursor.execute(comando)
db.commit()

#tabela historico disciplinas:
comando = """
CREATE TABLE Hist_Disc (
codHist_Disc integer PRIMARY KEY NOT NULL,
codHistorico integer NOT NULL,
codDisciplina integer NOT NULL,
nota REAL NOT NULL
)"""
cursor.execute(comando)
db.commit()
