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

def adicaoElemento(categoria, n, id=None, ch=None, ano=None):
    if categoria == "ALUNO":
        cursor.execute(f"""INSERT INTO Alunos (nome, cpf) VALUES ('{n}', '{id}')""")
    elif categoria == "PROFESSOR":
        cursor.execute(f"""INSERT INTO Professores (nome, cpf) VALUES ('{n}', '{id}')""")
    elif categoria == "DISCIPLINA":
        cursor.execute(f"""INSERT INTO Disciplinas (nome, cargaH) VALUES ('{n}', '{ch}')""")
    elif categoria == "TURMA":
        cursor.execute(f"""INSERT INTO Turmas (titulo, ano) VALUES ('{n}', {ano})""")
    db.commit()

def buscarElemento(categoria, n=None, id=None):
    tabela = ""
    dado1 = ""
    dado2 = ""
    if categoria == "ALUNO":
        tabela = 'Alunos'
        dado1 = 'nome'
        dado2 = 'cpf'
    if categoria == "PROFESSOR":
        tabela = 'Professores'
        dado1 = 'nome'
        dado2 = 'cpf'
    if categoria == "DISCIPLINA":
        tabela = 'Disciplinas'
        dado1 = 'nome'
        dado2 = 'cargaH'
    if n == None and id == None:
        return 0
    elif n != None and id == None:
        cursor.execute(f"SELECT {dado1}, {dado2} FROM {tabela} WHERE nome LIKE '%{n}%'")
        lista = cursor.fetchall()
        if len(lista) > 0:
            return lista
        else:
            return 0
    elif n == None and id != None:
        cursor.execute(f"SELECT {dado1}, {dado2} FROM {tabela} WHERE cpf = '{id}'")
        lista = cursor.fetchall()
        if len(lista) > 0:
            return lista
        else:
            return 0
    elif n != None and id != None:
        cursor.execute(f"SELECT {dado1}, {dado2} FROM {tabela} WHERE cpf = '{id}'")
        lista = cursor.fetchall()
        if len(lista) > 0:
            return lista
        else:
            return 0

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

def mostrarDados(tabela, categoria, no=None, ide=None):
    sql = ""
    if no == None and ide == None:
        buscarElemento(categoria)
    elif no == None and ide != None:
        if buscarElemento(categoria, id=ide) != 0:
            sql = f"""SELECT *
            FROM {tabela}
            WHERE cpf = '{ide}'"""
    elif no != None and ide == None:
        if buscarElemento(categoria, n=no) != 0:
            sql = f"""SELECT * FROM {tabela}
            WHERE nome LIKE '%{no}%'"""
    elif no != None and ide != None:
        if buscarElemento(categoria, no.upper(), ide) != 0:
            sql = f"""SELECT *
            FROM {tabela}
            WHERE nome LIKE '%{no.upper()}%' AND cpf = '{ide}'"""

    cursor.execute(sql)
    lista = cursor.fetchall()
    if len(lista) == 1:
        print(f"\nCOD. IDENTIFICADOR: {lista[0][0]}")
        for i in range(1, len(lista[0])):
            print(f"{lista[0][i]}")
        print()
#caso o usuário tenha digitado apenas uma parte do nome ...
# ...tenha encontrado mais de um resultado
    elif len(lista) > 1:
        print("\nDADOS ENCONTRADOS: ")
        for i in range(len(lista)):
            print(f"{i} - {lista[i][1]}")
        print(f"{len(lista)} - VOLTAR")
        op = int(input("DIGITE O NUMERO REFERENTE AO NOME: "))
        if op < 0 or op > (len(lista) + 1):
            raise ValueError
        elif op == len(lista):
            print("NENHUM NOME SELECIONADO.")
        elif op >= 0 or op < len(lista):
            print(f"\nCOD. IDENTIFICADOR: {lista[0][0]}")
            for i in range(1, len(lista[0])):
                print(f"{lista[op][i]}")
            print()

def contarElementos(categoria, tabela):
    if categoria == "ALUNO" or categoria == "PROFESSOR" or categoria == "DISCIPLINA":
        sql = f"""SELECT COUNT(nome) FROM {tabela}"""
    cursor.execute(sql)
    total = cursor.fetchall()[0][0]
    return total

def gerarLista(tabela):
    cursor.execute(f"""SELECT nome FROM {tabela}""")
    lista = cursor.fetchall()
    lista_final = []
    for nom in lista:
        lista_final.append(nom[0])
    return lista_final

# def configurarEscola(escola, cnpj, missao):
#     total_alunos = 0
#     total_prof = 0
#     lista_prof = gerarLista("Professores")
#     lista_materias = gerarLista("Disciplinas")
#     total_alunos = contarElementos('ALUNO', 'Alunos')
#     total_prof = len(lista_prof)
#     with open("info.txt", "w") as arquivo:
#         arquivo.write(f"{escola}-{cnpj}\n")
#         arquivo.write(f"{missao}\n")
#         arquivo.write("-".center(80, "-"))
#         arquivo.write(f"DADOS:\n")
#         arquivo.write(f"TOTAL DE ALUNOS: {total_alunos}\n")
#         arquivo.write(f"PROFESSORES:\n")
#         for nome in lista_prof:
#             print("nome\n")
#         arquivo.write(f"TOTAL DE PROFESSORES: {total_prof}\n")
#         arquivo.write(f"DISCIPLINAS OFERTADAS:\n")
#         for nome in lista_materias:
#             print("nome\n")
#     print("CONFIGURAÇÕES INICIAIS REALIZADAS COM SUCESSO.")
