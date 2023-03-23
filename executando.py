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
            print("INSIRA UMA OPÇÃO VÁLIDA.")

def menuAluno():
    while True:
        try:
            print("""
            1 - CADASTRAR ALUNO
            2 - ALTERAR CADASTRO DE ALUNO
            3 - BUSCAR DADOS DO ALUNO
            4 - REGISTRAR NOTA DE ALUNO
            5 - BUSCAR HISTÓRICO DE ALUNO
            6 - VOLTAR
            """)
            op = int(input("SELECIONA UMA OPÇÃO: "))
            if op < 1 or op > 6:
                raise ValueError
            if op == 1:
                cadastrar('ALUNO')
            if op == 2:
                alterarElemento('ALUNO')
            if op == 3:
                imprimirDados('ALUNO')
            if op == 4:
                registrarNota()
            if op == 5:
                historico()
            if op == 6:
                break
        except ValueError:
            print("INSIRA UMA OPÇÃO VÁLIDA.")

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
                cadastrar('PROFESSOR')
            if op == 2:
                alterarElemento('PROFESSOR')
            if op == 3:
                imprimirDados('PROFESSOR')
            if op == 4:
                break
        except ValueError:
            print("INSIRA UMA OPÇÃO VÁLIDA.")

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
            print("INSIRA UMA OPÇÃO VÁLIDA.")

def cadastrar(categoria):
    while True:
        try:
            nome = input("NOME: ").strip().upper()
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
            escola.adicaoElemento(categoria, nome, cpf)
            op = int(input(f"CADASTRAR MAIS {categoria.upper()}S? 1- SIM / 2- VOLTAR_"))
            if op < 1 or op > 2:
                raise ValueError
            elif op == 2:
                break
        except ValueError:
            print("INSIRA UM(A) DADO/OPÇÃO VÁLIDO(A)")

def alterarElemento(categoria):
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
                a = escola.buscarElemento(categoria)
            elif nome == "" and cpf != "":
                lista = []
                if escola.buscarElemento(categoria, id=cpf) != 0:
                    lista = escola.buscarElemento(categoria, id=cpf)
                    for i in range(len(lista)):
                        print(f"{i} - {lista[i][0]}")
                    op1 = int(input(f"ALTERAR DADOS PARA QUAL {categoria}? 0 a {len(lista) - 1} / {len(lista)} - VOLTAR_"))
                    if op1 < 0 or op1 > len(lista):
                        raise ValueError
                    elif op1 == len(lista):
                        break
                    else:
                        dado = True
                        for i in range(len(lista)):
                            if i == op1:
                                nome = lista[i][0]
            elif cpf == "" and nome != "":
                lista = []
                if escola.buscarElemento(categoria, n=nome) != 0:
                    lista = escola.buscarElemento(categoria, n=nome)
                    for i in range(len(lista)):
                        print(f"{i} - {lista[i][0]}")
                    op1 = int(input(f"ALTERAR DADOS PARA QUAL {categoria}? 0 a {len(lista) - 1} / {len(lista)} - VOLTAR_"))
                    if op1 < 0 or op1 > len(lista):
                        raise ValueError
                    elif op1 == len(lista):
                        break
                    else:
                        dado = True
                        for i in range(len(lista)):
                            if i == op1:
                                nome = lista[i][0]
                                cpf = lista[i][1]
            elif cpf != "" and nome != "":
                lista = []
                if escola.buscarElemento(categoria, id=cpf) != 0:
                    lista = escola.buscarElemento(categoria, id=cpf)
                    for i in range(len(lista)):
                        print(f"{i} - {lista[i][0]}")
                    op1 = int(input(f"ALTERAR DADOS PARA QUAL {categoria}? 0 a {len(lista) - 1} / {len(lista)} - VOLTAR_"))
                    if op1 < 0 or op1 > len(lista):
                        raise ValueError
                    elif op1 == len(lista):
                        break
                    else:
                        dado = True
                        for i in range(len(lista)):
                            if i == op1:
                                nome = lista[i][0]
                else:
                    lista = []
                    if escola.buscarElemento(categoria, nome) == 0:
                        lista = escola.buscarElemento(categoria, nome)
                    for i in range(len(lista)):
                        print(f"{i} - {lista[i][0]}")
                    op1 = int(input(f"ALTERAR DADOS PARA QUAL {categoria}? 0 a {len(lista) - 1} / {len(lista)} - VOLTAR_"))
                    if op1 < 0 or op > len(lista):
                        raise ValueError
                    elif op1 == len(lista):
                        break
                    else:
                        dado = True
                        for i in range(len(lista)):
                            if i == op1:
                                nome = lista[i][0]
                                cpf = lista[i][1]
            if dado:
                nome = nome.strip().upper()
                print(f"{categoria} ENCONTRADO: {nome} - {cpf}")
                novo_nome = input("CORRIGIR NOME: ").strip().upper()
                novo_cpf = input("CORRIGIR CPF: ")
                if categoria == "ALUNO":
                    escola.alterarDados('Alunos', 'nome', nome, novo_nome)
                    escola.alterarDados('Alunos', 'cpf', cpf, novo_cpf)
                elif categoria == "PROFESSOR":
                    escola.alterarDados('Professores', 'nome', nome, novo_nome)
                    escola.alterarDados('Professores', 'cpf', cpf, novo_cpf)
            else:
                print("DADOS NÃO ENCONTRADOS.")
            op = int(input("CONTINUAR ALTERANDO CADASTRO? 1- SIM / 2- VOLTAR_"))
            if op < 1 or op > 2:
                raise ValueError
            elif op == 2:
                break
        except ValueError:
            print("INSIRA UM(A) DADO/OPÇÃO VÁLIDO(A)")

def imprimirDados(categoria):
    while True:
        try:
            nome = input("NOME: ").lower().strip()
            cpf = input("CPF: ")
            ccpf = True
            for c in nome:
                if c.isdigit():
                    raise ValueError
            for c in cpf:
                if not c.isdigit():
                    ccpf = False
            if not ccpf:
                print("CPF INVÁLIDO.\n")
                raise ValueError
            if categoria == "ALUNO":
                tabela = 'Alunos'
            elif categoria == "PROFESSOR":
                tabela = 'Professores'
            if nome == "" and cpf == "":
                escola.mostrarDados(tabela, categoria)
            elif nome == "" and cpf != "":
                escola.mostrarDados(tabela, categoria, ide=cpf)
            elif cpf == "" and nome != "":
                escola.mostrarDados(tabela, categoria, no=nome)
            elif cpf != "" and nome != "":
                escola.mostrarDados(tabela, categoria, nome, cpf)
            op = int(input(f"BUSCAR MAIS ALGUM {categoria}? 1- SIM / 2- VOLTAR_"))
            if op < 1 or op > 2:
                raise ValueError
            elif op == 2:
                break
        except ValueError:
            print("INSIRA UM(A) DADO/OPÇÃO VÁLIDO(A)")
