nome = []
cpf = []
estado = []
curso = []
aluno = [nome, cpf, estado, curso]
sair = 0
while (sair != 4):
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("Para realizar a inscrição informe os seguintes dados: ")
        _nome = input("Digite o nome do aluno: ")
        _cpf = input("Digite o CPF do aluno: ")
        _estado = input("Escolha o estado que deseja fazer o curso: ")
        _curso = input("Escolha um dos cursos disponíveis: ")
        nome.append(_nome)
        cpf.append(_cpf)
        estado.append(_estado)
        curso.append(_curso)
        print(aluno)
    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo cpf\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
            cpf.index(alteraInscricaoCpf)

        elif opcao1 == 2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        print("nada")
    elif menu == 4:
        continue
    else:
        print("Opção Inválida")