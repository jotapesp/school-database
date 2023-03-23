import escola

def menu():
    while True:
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
                    menuAluno()
            elif op == 2:
                    menuProfessor()
            elif op == 3:
                    menuEscola()
            elif op == 4:
                break
        except ValueError:
            print("Insira uma opção válida.")

def menuAluno():
    while True:
        try:
            print("""
            1 - CADASTRAR ALUNO
            2 - ALTERAR CADASTRO DE ALUNO
            3 - BUSCAR DADOS DO ALUNO
            4 - BUSCAR HISTÓRICO DE ALUNO
            5 - VOLTAR
            """)
            op = int(input("SELECIONA UMA OPÇÃO: "))
            if op < 1 or op > 5:
                raise ValueError
            if op == 1:
                    cadastrarAluno()
            if op == 2:
                    alterarAluno()
            if op == 3:
                    buscarDados()
            if op == 4:
                    historico()
            if op == 5:
                break
        except ValueError:
            print("Insira uma opção válida.")

def menuProfessor():
    while True:
        try:
            print("""
            1 - CADASTRAR PROFESSOR
            2 - ALTERAR CADASTRO DE PROFESSOR
            3 - BUSCAR DADOS DO PROFESSOR
            4 - VOLTAR
            """)
            op = int(input("SELECIONA UMA OPÇÃO: "))
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
    while True:
        try:
            print("""
            1 - INFORMAÇÕES SOBRE A ESCOLA
            2 - VOLTAR
            """)
            op = int(input("SELECIONA UMA OPÇÃO: "))
            if op < 1 or op > 2:
                raise ValueError
            if op == 1:
                infoEscola()
            if op == 2:
                break
        except ValueError:
            print("Insira uma opção válida.")

def cadastrarAluno():
    while True:
        try:
            nome = input("NOME: ")
            cpf = input("CPF: ")
            ccpf = True
            for c in nome:
                if c.isdigit():
                    raise ValueError
            for c in cpf:
                if not c.isdigit():
                    ccpf = False
            if not ccpf:
                print("CPF inválido.")
                raise ValueError
            escola.adicaoAluno(nome.upper(), cpf)
            op = int(input("CADASTRAR MAIS ALUNOS? 1- SIM / 2- VOLTAR_"))
            if op < 1 or op > 2:
                raise ValueError
            elif op == 2:
                break
        except ValueError:
            print("Insira um dado/opção válido")

def alterarAluno():
    while True:
        try:
            nome = input("NOME: ")
            cpf = input("CPF: ")
            dado = False
            ccpf = True
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
                    print("ALUNO NÃO ENCONTRADO.")
                    dado = False
            elif cpf == "" and nome != "":
                if not escola.buscarAluno(n=nome.lower()):
                    print("ALUNO NÃO ENCONTRADO.")
                    dado = False
                else:
                    dado = True
            if dado:
                print("ALUNO ENCONTRADO.")
                nome = nome.strip().upper()
                novo_nome = input("CORRIGIR NOME: ").strip().upper()
                novo_cpf = input("CORRIGIR CPF: ")
                escola.alterarDados('Alunos', 'nome', nome, novo_nome)
                escola.alterarDados('Alunos', 'cpf', cpf, novo_cpf)
            op = int(input("ALTERAR MAIS ALGUM CADASTRO? 1- SIM / 2- VOLTAR_"))
            if op < 1 or op > 2:
                raise ValueError
            elif op == 2:
                break
        except ValueError:
            print("Insira um dado/opção válido")
