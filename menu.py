from desafioo.ValidaEstado import *
#Aqui fica o pacote final do projeto, este é provisório

nome = []
cpf =[]
estado = []
curso = []
aluno = [nome, cpf, estado, curso]
codigo = ["A01", "A02", "A03","A04"]
todos = ["AC","AL","AP", "AM","BA","CE","DF","ES","GO","MA","MT","MS", "MG","PA","PB","PR","PE","PI","RJ", "RN","RS","RO","RR","SC",'SP',"SE",'TO']
nordeste = ["AL","BA","CE","MA","PB","PE","PI","RN","SE"]
centroOeste = ["DF","GO","MT","MS","RR"]
nss = ["RR","AM","AC","RO","PA","AP","TO","SP","MG","ES","RJ","PR","SC","RS"]
sudeste = ["SP","MG","ES"]
estados = [todos, nordeste, centroOeste,nss, sudeste]
nomeCurso = ["Al e Machine Learning", "Business Inteligence", "Governança em TI","Programação Python", "Programação JAVA"]
cursos = [codigo, nomeCurso, estados ]
sair = 0
while(sair != 4):
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("Para realizar a inscrição informe os seguintes dados: ")
        _nome = input("Digite o nome do aluno: ")
        _cpf = input("Digite o CPF do aluno: ")

        estado = input("Escolha o estado que deseja fazer o curso: ").upper()
        while validar_estado(_estado) is not True:
            _estado = input("Escolha o estado que deseja fazer o curso: ").upper()

        _curso = input("Cursos:", cursos,"Escolha um dos cursos disponíveis: ")
        nome.append(_nome)
        cpf.append(_cpf)
        estado.append(_estado)
        curso.append(_curso)
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
        break
    else:
        print("Opção Inválida")
