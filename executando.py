import escola

ListaAlunos = []

def menu():
    try:
        print("""
        1 - MENU ALUNO
        2 - MENU PROFESSOR
        3 - MENU ESCOLA
        4 - ENCERRAR
        """)
        op = int(input("SELECIONE UMA OPÇÃO: "))
        if op < 1 or op > 4:
            raise ValueError
        if op == 1:
            while True:
                menuAluno()
        elif op == 2:
            while True:
                menuProfessor()
        elif op == 3:
            while True:
                menuEscola()
        elif op == 4:
            break
    except ValueError:
        print("Insira uma opção válida.")

def menuAluno():
    try:
        print("""
        1 - CADASTRAR ALUNO
        2 - ALTERAR CADASTRO DE ALUNO
        3 - BUSCAR DADOS DO ALUNO
        4 - BUSCAR HISTÓRICO DE ALUNO
        5 - VOLTAR
        """)
        op = int(integer("SELECIONA UMA OPÇÃO: "))
        if op < 1 or op > 5:
            raise ValueError
        if op == 1:
            while True:
                cadastrarAluno()
        if op == 2:
            while True:
                alterarAluno()
        if op == 3:
            while True:
                buscarDados()
        if op == 4:
            while True:
                historico()
        if op == 5:
            break
    except ValueError:
        print("Insira uma opção válida.")

def menuProfessor():
try:
    print("""
    1 - CADASTRAR PROFESSOR
    2 - ALTERAR CADASTRO DE PROFESSOR
    3 - BUSCAR DADOS DO PROFESSOR
    4 - VOLTAR
    """)
    op = int(integer("SELECIONA UMA OPÇÃO: "))
    if op < 1 or op > 4:
        raise ValueError
    if op == 1:
        cadastrarProfessor()
    if op == 2:
        alterarProfessor()
    if op == 3:
        buscarDadosProf()
    if op == 4:
        break
except ValueError:
    print("Insira uma opção válida.")

def menuEscola():
try:
    print("""
    1 - INFORMAÇÕES SOBRE A ESCOLA
    2 - VOLTAR
    """)
    op = int(integer("SELECIONA UMA OPÇÃO: "))
    if op < 1 or op > 2:
        raise ValueError
    if op == 1:
        infoEscola()
    if op == 2:
        break
except ValueError:
    print("Insira uma opção válida.")

def cadastrarAluno():
    try:
        nome = input("NOME: ")
        cpf = input("CPF: ")
        for c in nome:
            if c.isdigit():
                raise ValueError
        for c in cpf:
            if not c.isdigit():
                ccpf = False
        if not ccpf:
            print("CPF inválido.")
            raise ValueError
        escola.adicaoAluno(nome, cpf)
        op == input("CADASTRAR MAIS ALUNOS? 1 - SIM 2 - VOLTAR")
        if op < 1 or op > 2:
            raise ValueError
        elif op == 2:
            break
    except ValueError:
        print("Insira um dado/opção válido")

def alterarAluno():
    try:
        nome = input("NOME: ")
        cpf = int(input("CPF: ")
        dado = False
        for c in nome:
            if c.isdigit():
                raise ValueError
        for c in cpf:
            if not c.isdigit():
                    ccpf = False
        if not ccpf:
            print("CPF inválido.")
            raise ValueError
        if nome == "" and cpf == "":
            escola.buscarAluno()
        elif nome == "" and cpf != "":
            if not escola.buscarAluno(id=cpf):
                dado = False
                print("ALUNO NÃO ENCONTRADO.")
            else:
                dado = True
        elif cpf == "" and nome != "":
            if not escola.buscarAluno(n=nome.lower()):
                dado = False
                print("ALUNO NÃO ENCONTRADO.")
            else:
                dado = True
        if dado:
            print("ALUNO ENCONTRADO.")
                novo_nome = input("CORRIGIR NOME: ")
                novo_cpf = int(input("CORRIGIR CPF: "))
            escola.alterarDados('Alunos', 'nome', nome.strip(), novo_nome.strip())
            escola.alterarDados('Alunos', 'cpf', cpf, novo_cpf)
        op == input("ALTERAR MAIS ALGUM CADASTRO? 1 - SIM 2 - VOLTAR")
        if op < 1 or op > 2:
            raise ValueError
        elif op == 2:
            break
        except ValueError:
            print("Insira um dado/opção válido")
