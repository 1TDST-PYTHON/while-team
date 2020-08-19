sair = 0
while(sair != 4):
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        nome_aluno = input("Nome do aluno: ")
        cpf_aluno = input("CPF: ")
        estado = input("Estado que deseja fazer o curso: ")
        curso = input("Escolha um dos cursos possíveis")

    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo cpf\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
        elif opcao1 ==  2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        print("nada")
    elif menu == 4:
        continue
    else:
        print("Opção Inválida")