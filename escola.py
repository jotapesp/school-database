import sqlite3
#inicializando banco de dados
db = sqlite3.connect("escola.db")
cursor = db.cursor()

#check if tables already exists before creating it:
def tableExists(tablename):
    cursor.execute("""SELECT name FROM sqlite_master WHERE type = 'table'""")
    tablist = cursor.fetchall()
    for table in tablist:
        if table[0] == tablename:
            return True
    return False

if not tableExists('Alunos'):
#tabela p/ dados dos alunos:
    comando = """CREATE TABLE Alunos (
    codAluno integer PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL
    )"""
    cursor.execute(comando)
    db.commit()

#tabela p/ dados dos professores:
if not tableExists('Professores'):
    comando = """
    CREATE TABLE Professores (
    codProfessor integer PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL
    )"""
    cursor.execute(comando)
    db.commit()

#tabelo para dados das disciplinas:
if not tableExists('Disciplinas'):
    comando = """
    CREATE TABLE Disciplinas (
    codDisciplina integer PRIMARY KEY NOT NULL,
    nome text NOT NULL,
    cargaH text NOT NULL
    )"""
    cursor.execute(comando)
    db.commit()

#tabela para dados das turmas:
if not tableExists('Turmas'):
    comando = """
    CREATE TABLE Turmas (
    codTurma integer PRIMARY KEY NOT NULL,
    titulo text NOT NULL,
    ano integer NOT NULL
    )"""
    cursor.execute(comando)
    db.commit()

#tabela de disciplina de cada turma:
if not tableExists('Disc_Turma'):
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
if not tableExists('Historico'):
    comando = """
    CREATE TABLE Historico (
    codHistorico integer PRIMARY KEY NOT NULL,
    codAluno integer NOT NULL
    )"""
    cursor.execute(comando)
    db.commit()

#tabela historico disciplinas:
if not tableExists('Hist_Disc'):
    comando = """
    CREATE TABLE Hist_Disc (
    codHist_Disc integer PRIMARY KEY NOT NULL,
    codHistorico integer NOT NULL,
    codDisciplina integer NOT NULL,
    nota REAL NOT NULL
    )"""
    cursor.execute(comando)
    db.commit()

def adicaoAluno(n, id):
    cursor.execute(f"""INSERT INTO Alunos (nome, cpf) VALUES ('{n}', '{id}')""")
    db.commit()

def buscarAluno(n=None, id=None):
    if n == None and id == None:
        print("Algum dado para busca deve ser inserido.")
    elif n != None and id == None:
        cursor.execute(f"SELECT nome FROM Alunos WHERE nome LIKE '%{n}%'")
        if len(cursor.fetchall()) > 0:
            return True
        else:
            return False
    elif n == None and id != None:
        cursor.execute(f"SELECT nome FROM Alunos WHERE cpf = '{id}'")
        if len(cursor.fetchall()) > 0:
            return True
        else:
            return False

def alterarDados(tabela, dado, dado_antigo, dado_novo):
    if isinstance(dado_antigo, str):
        cursor.execute(f"""
        UPDATE {tabela}
        SET {dado} = '{dado_novo}'
        WHERE {dado} = '{dado_antigo}'""")
        db.commit()
    else:
        cursor.execute(f"""
        UPDATE {tabela}
        SET {dado} = {dado_novo}
        WHERE {dado} = {dado_antigo}""")
        db.commit()
