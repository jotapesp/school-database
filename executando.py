import escola

def menu():
    try:
        print(""" 1 - CADASTRAMENTO DE ALUNOS,
        2 - CADASTRAMENTO DE PROFESSORES,
        3 - REGISTRAR NOTA DE ALUNO,
        4 - ENCERRAR)
        op = input("SELECIONE UMA OPÇÃO: ")
        if op < 1 or op > 4:
            raise ValueError
    except ValueError:
        print("Insira uma opção válida.")
