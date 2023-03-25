import escola
import os

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
                cadastrar("NOTA")
            if op == 5:
                escola.historico()
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
            4 - ATRIBUIR PROFESSOR A UMA DISCIPLINA
            5 - VOLTAR
            """)
            op = int(input("SELECIONA UMA OPÇÃO: "))
            if op < 1 or op > 5:
                raise ValueError
            if op == 1:
                cadastrar('PROFESSOR')
            if op == 2:
                alterarElemento('PROFESSOR')
            if op == 3:
                imprimirDados('PROFESSOR')
            if op == 4:
                cadastrar("DISC_T")
            if op == 5:
                break
        except ValueError:
            print("INSIRA UMA OPÇÃO VÁLIDA.")

def menuEscola():
    while True:
        try:
            print("""
            1 - INFORMAÇÕES SOBRE A ESCOLA
            2 - REGISTRAR DISCIPLINA
            3 - ALTERAR DADOS DE DISCIPLINA
            4 - BUSCAR INFORMAÇÕES SOBRE DISCIPLINA
            5 - CONFIGURAÇÕES DE TURMAS
            6 - VOLTAR
            """)
            op = int(input("SELECIONA UMA OPÇÃO: "))
            if op < 1 or op > 7:
                raise ValueError
            if op == 1:
                infoEscola()
            if op == 2:
                cadastrar('DISCIPLINA')
            if op == 3:
                alterarElemento('DISCIPLINA')
            if op == 4:
                imprimirDados('DISCIPLINA')
            if op == 5:
                configTurma()
            if op == 6:
                break
        except ValueError:
            print("INSIRA UMA OPÇÃO VÁLIDA.")

def cadastrar(categoria):
    while True:
        cod_erro = 0
        try:
            # nome = ""
            # cpf = ""
            # cha = ""
            # anot = ""
            if categoria == "ALUNO" or categoria == "PROFESSOR":
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
                escola.adicaoElemento(categoria, n=nome, id=cpf)
                if categoria == "ALUNO":
                    l = escola.buscarElemento("ALUNO", n=nome, id=cpf, todos=True)
                    cod_aluno = l[0][0]
                    escola.adicaoElemento("HISTORICOS", n=cod_aluno)

            elif categoria == "DISCIPLINA":
                nome = input("DISCIPLINA: ").strip().upper()
                cha = input("CARGA HORÁRIA: ").strip().upper()
                escola.adicaoElemento(categoria, n=nome, ch=cha)
            elif categoria == "TURMA":
                titulo = input("INFORME O TÍTULO DA TURMA: ").strip().upper()
                anot = int(input("INFORME O ANO DA TURMA: "))
                escola.adicaoElemento("TURMA", n=titulo, ano=anot)
            elif categoria == "DISC_T":
                hora = input("INFORME O HORÁRIO: ")
                cod_disci = escola.buscarCodigo("DISCIPLINA")
                cod_turma = escola.buscarCodigo("TURMA")
                cod_prof = escola.buscarCodigo("PROFESSOR")
                L = [cod_disci, cod_prof, cod_turma, hora]
                escola.adicaoElemento("DISC_T", cod_disci, cod_prof, cod_turma, hora)
            elif categoria == "NOTA":
                cod_aluno = escola.buscarCodigo("ALUNO")
                l = escola.buscarElemento("HISTORICOS", n=cod_aluno)
                cod_hist = 0
                if l != 0:
                    cod_hist = l[0][0]
                else:
                    raise ValueError
                cod_turma = escola.buscarCodigo("TURMA")
                cod_disci1 = escola.buscarCodigo("DISCIPLINA")
                cod_disci2 = escola.buscarElemento("DISC_T", n=cod_disci1, id=cod_turma)   ###OLHAR AQUI
                cod_disci = 0
                if cod_disci2 != 0:
                    print("a busca funcionou, é != 0")
                    cod_disci = cod_disci2[0][0]
                else:
                    cod_erro = 2
                    raise ValueError("VERIFIQUE SE A DISCIPLINA FOI CADASTRADA PARA ESSA TURMA.")
                nota = float(input("INFORME A NOTA A REGISTRAR: "))
                escola.adicaoElemento("HIST_D", cod_hist, cod_disci, nota)

            op = int(input(f"CADASTRAR MAIS {categoria.upper()}S? 1- SIM / 2- VOLTAR_"))
            if op < 1 or op > 2:
                raise ValueError
            elif op == 2:
                break
        except ValueError as e:
            if cod_erro == 2:
                print(f"ERRO: {e}")
                break
            else:
                print("INSIRA UM(A) DADO/OPÇÃO VÁLIDO(A)")

def alterarElemento(categoria):
    while True:
        try:
            if categoria == "ALUNO" or categoria == "PROFESSOR":
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

            if categoria == "DISCIPLINA":
                nome = input("DISCIPLINA: ")
                ch = ""
                lista = escola.buscarElemento(categoria, n=nome)
                if len(lista) > 0:
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
                                ch = lista[i][1]
                if dado:
                    nome = nome.strip().upper()
                    print(f"{categoria} ENCONTRADO: {nome}")
                    novo_nome = input("CORRIGIR NOME: ").strip().upper()
                    novo_ch = input("CORRIGIR CARGA HORÁRIA: ")
                    escola.alterarDados('Disciplinas', 'nome', nome, novo_nome)
                    escola.alterarDados('Disciplinas', 'cargaH', ch, novo_ch)
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
            nome = ""
            cpf = ""
            ch = ""
            tabela = ""
            if categoria == "ALUNO" or categoria == "PROFESSOR":
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
            if categoria == "DISCIPLINA":
                nome = input("DISCIPLINA: ").lower().strip()
                tabela = 'Disciplinas'
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

def infoEscola():
    if not os.path.exists("info.txt"):
        print("""\nPRIMEIRA VEZ ACESSANDO ESSE MENU, VAMOS FAZER
UMAS CONFIGURAÇÕES INICIAIS.""")
        nescola = input("DIGITE O NOME DA ESCOLA: ").strip().upper()
        cnpj = ""
        missao = ""
        while True:
            cnpj = input("INFORME O CNPJ DA ESCOLA: ")
            ccnpj = True
            for c in cnpj:
                if not c.isdigit():
                    ccnpj = False
            if not ccnpj:
                print("CNPJ INVÁLIDO.")
            else:
                break
        missao = input("DIGITE A MISSÃO DA ESCOLA: ").strip().upper()
        # escola.configurarEscola(nescola, cnpj, missao)
        total_alunos = 0
        total_prof = 0
        lista_prof = escola.gerarLista("Professores")
        lista_materias = escola.gerarLista("Disciplinas")
        total_alunos = escola.contarElementos('ALUNO', 'Alunos')
        total_prof = len(lista_prof)
        with open("info.txt", "w") as arquivo:
            arquivo.write(f"{nescola}-{cnpj}\n")
            arquivo.write(f"{missao}\n")
            arquivo.write("-".center(80, "-"))
            arquivo.write("\n")
            arquivo.write(f"DADOS:\n")
            arquivo.write("\n")
            arquivo.write(f"TOTAL DE ALUNOS: {total_alunos}\n")
            arquivo.write("\n")
            arquivo.write(f"PROFESSORES:\n")
            for nome in lista_prof:
                arquivo.write(f"{nome}\n")
            arquivo.write(f"TOTAL DE PROFESSORES: {total_prof}\n")
            arquivo.write("\n")
            arquivo.write(f"DISCIPLINAS OFERTADAS:\n")
            for nome in lista_materias:
                arquivo.write(f"{nome}\n")
            arquivo.write("\n")
        print("CONFIGURAÇÕES INICIAIS REALIZADAS COM SUCESSO.")

    if os.path.exists("info.txt"):
        while True:
            try:
                print("""MENU ESCOLA:
            1 - SINCRONIZAR INFORMAÇÕES NOVAS
            2 - EXIBIR INFORMAÇÕES SOBRE A ESCOLA
            3 - RESETAR CONFIGURAÇÕES INICIAIS
            4 - VOLTAR
            """)
                op = int(input("ESCOLHA UMA OPÇÃO: "))
                if op < 1 and op > 3:
                    raise ValueError
                elif op == 4:
                    break
                elif op == 1:
                    nome_escola = ""
                    cnpj_escola = ""
                    missao_escola = ""
                    with open("info.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                        l = linhas[0].split("-")
                        nome_escola = l[0]
                        cnpj_escola = l[1]
                        missao_escola = linhas[1]
                    total_alunos = 0
                    total_prof = 0
                    lista_prof = escola.gerarLista("Professores")
                    lista_materias = escola.gerarLista("Disciplinas")
                    total_alunos = escola.contarElementos('ALUNO', 'Alunos')
                    total_prof = len(lista_prof)
                    with open("info.txt", "w") as arquivo:
                        arquivo.write(f"{nome_escola}-{cnpj_escola}\n")
                        arquivo.write(f"{missao_escola}\n")
                        arquivo.write("-".center(80, "-"))
                        arquivo.write("\n")
                        arquivo.write(f"DADOS:\n")
                        arquivo.write("\n")
                        arquivo.write(f"TOTAL DE ALUNOS: {total_alunos}\n")
                        arquivo.write("\n")
                        arquivo.write(f"PROFESSORES:\n")
                        for nome in lista_prof:
                            arquivo.write(f"{nome}\n")
                        arquivo.write(f"TOTAL DE PROFESSORES: {total_prof}\n")
                        arquivo.write("\n")
                        arquivo.write(f"DISCIPLINAS OFERTADAS:\n")
                        for nome in lista_materias:
                            arquivo.write(f"{nome}\n")
                        arquivo.write("\n")
                    print("SINCRONIZAÇÃO CONCLUÍDA.")
                elif op == 2:
                    with open("info.txt", "r") as arquivo:
                        linhas = arquivo.readlines()
                        l = linhas[0].split("-")
                        nome_escola = l[0]
                        cnpj_escola = l[1]
                        print(f"NOME: {nome_escola} - CNPJ: {cnpj_escola}", end="")
                        print(f"MISSÃO: {linhas[1]}")
                        for i in range(2, len(linhas)):
                            print(linhas[i], end="")
                elif op == 3:
                    os.remove("info.txt")
                    break
            except ValueError:
                print("OPÇÃO INVÁLIDA.")

def configTurma():
    while True:
        try:
            print("""CONFIGURAÇÕES DE TURMA:
            1 - CADASTRAR TURMA
            2 - ATRIBUIR DISCIPLINA A UMA TURMA
            3 - VOLTAR
            """)
            op = int(input("ESCOLHA UMA OPÇÃO: "))
            if op < 1 or op > 4:
                raise ValueError
            if op == 1:
                cadastrar("TURMA")
            if op == 2:
                cadastrar("DISC_T")
            if op == 3:
                break
        except ValueError:
            print("INSIRA UMA OPÇÃO VÁLIDA.")

# def historico():
#     cod_aluno = escola.buscarCodigo("ALUNO")
