from os import path
from tkinter import Tk, ttk, filedialog

senha_gammon, senha_faculdade, pathcsv = "Gammon21#", "Fagammon21#", "c:/users/public/desktop/users.csv"

def viewplanilha(num_colunas, lerarq):
    num_colunas += 2
    colunas = []

    for x in range(1, num_colunas):
        colunas.append(str(x))

    janela = Tk()
    veja = ttk.Treeview(janela, selectmode="browse", columns=(colunas), show="headings")
    veja.column("1", width=30, minwidth=50, stretch=0)
    veja.heading("#1", text="")

    for x in range(2, num_colunas):
        veja.column(str(x), width=200, minwidth=50, stretch=0)
        veja.heading("#" + str(x), text=lerarq[0].split(",")[x - 2])

    for x in range(1, len(lerarq)):
        veja.insert("", "end", values=(str(x) + "," + lerarq[x]).split(","))

    veja.grid(row=0, column=0)

    janela.mainloop()
    
def removeracento(palavra):
    acento = "áàãâéèêíìîóòõôúùûç"
    palavra = palavra.lower()
    p = ""

    for x in palavra:
        i = acento.find(x)

        if i > -1 and i < 4:
            p += "a"
        elif i > 3 and i < 7:
            p += "e"
        elif i > 6 and i < 10:
            p += "i"
        elif i > 9 and i < 14:
            p += "o"
        elif i > 13 and i < 17:
            p += "u"
        elif i == 17:
            p += "c"
        else:
            p += x

    return p

def unidade(posicao):
    escolha = {
        1: "/Acadêmico/Colégio/Alunos/Lavras",
        2: "/Acadêmico/Colégio/Alunos/Guanhães",
        3: "/Acadêmico/Colégio/Alunos/MEDGAMMON",
        4: "/Acadêmico/Colégio/Professores/Lavras",
        5: "/Acadêmico/Colégio/Professores/Guanhães",
        6: "/Acadêmico/Faculdade/Alunos/Administração",
        7: "/Acadêmico/Faculdade/Alunos/EDUCAÇÃO FÍSICA - Bacharelado",
        8: "/Acadêmico/Faculdade/Alunos/EDUCAÇÃO FÍSICA - Licenciatura",
        9: "/Acadêmico/Faculdade/Alunos/PEDAGOGIA",
        10: "/Acadêmico/Faculdade/Alunos/SISTEMAS DE INFORMAÇÃO",
        11: "/Acadêmico/Faculdade/Alunos/Tecnologia em Redes de Computadores",
        12: "/Acadêmico/Faculdade/Professores",
        13: "/Corporativo"
    }

    return escolha[posicao]

def VF(mensagem):
    b = input(mensagem).upper()

    if not (b == "S" or b == "N"):
        b = "N"

    return b

def validarint(mensagem, erro, padrao, maxopcoes):
    i = 0
    print(mensagem)

    while i == 0:
        valor = input(":")

        try:
            valor = int(valor)
        except:
            valor = 0

        if valor > 0 and valor < maxopcoes:
            i = valor
            return valor
        else:
            if valor == 0:
                i = 1
                return padrao
            else:
                print(erro)
                print(mensagem)

def qualfunc(este):
    if este > 1 and este < 5:
        resposta = {
            1: "Primeira opção foi escolhida",
            2: "Segunda opção foi escolhida",
            3: "Terceira opção foi escolhida",
            4: "Quarta opção foi escolhida"
        }

        print(resposta[este])
    elif este == 1:
        print(priopc()),
    else:
        print("Nenhuma opção correta foi atingida")
   
def priopc():
    global pathcsv
    cabecalho = ["First Name [Required]", "Last Name [Required]", "Email Address [Required]", "Password [Required]", "Org Unit Path [Required]", "Change Password at Next Sign-In", "New Status [UPLOAD ONLY]"]
    lista, sobrenome, email, senha, mudar_senha, org_unid = [], [], [], [], [], []
    # nome = ["LUIZ THADEU SERAFIM", "GUSTAVO BORGES", "ALFREDO DE MESQUITA BARBOSA", "PEDRO PABLO DA SILVA", "MARCO ANTÔNIO SILVEIRA", "PEDRO COIMBRA", "AMAURI DA COSTA SANTOS"]

    a = VF("Gostaria de abrir arquivo salvo com nomes? (S/N)")

    if a == "S":
        lerarq = filedialog.askopenfilename(filetypes=[("Arquivo Texto (.txt)", ".txt"), ("Arquivo CSV (.csv)", ".csv")], initialdir=path.dirname(pathcsv))
        lerarq = open(lerarq, mode="r", encoding="utf8")
        nome = lerarq.read().upper()
        lerarq.close()

        nome = nome.split("\n")

        # if nome[0].find(",") > -1:
        #     for x in range(len(nome)):
        #         lerarq = nome.split(",")[0]

    elif a == "N":
        nome = []
        print('Enquanto não for a palavra "EXIT", ou vazio, o loop continua')

        while True:
            continuar = input("Digite o nome: ").upper()

            if continuar == "EXIT" or continuar == "":
                break

            nome.append(continuar)

    for x in nome:
        lista.append(" ".join(x.split(" ")[:len(x.split(" ")) - 1]))
        sobrenome.append(x.split(" ")[len(x.split(" ")) - 1])

    nome = lista

    print("Digite uma das opções (padrão=1)")
    y = validarint("1 - Gammon\n2 - Fagammon\n3 - Corporativo", "Defina a unidade", 1, 4)

    s = VF("Mudar senha no próximo login?(S/N)")

    o1 = "N"

    for x in range(len(nome)):
        if s == "S":
            mudar_senha.append("TRUE")
        elif s == "N":
            mudar_senha.append("FALSE")

        if y == 1:
            if o1 == "N":
                print("Escolha a organização")
                o = validarint("1 - Alunos\n2 - Professores", "Escolha uma das opções a seguir", 1, 3)

                msgaluno = "Cidade"
                msgescolha = "1 - Lavras\n2 - Guanhães"

                if o == 1:# Escolher para onde aluno vai
                    msgaluno += " ou Cursinho?"
                    msgescolha += "\n3 - MEDGAMMON"
                    print(msgaluno)
                    a = validarint(msgescolha, "Escolha inválida", 1, 4)
                elif o == 2:# Escolher professor para qual cidade
                    print(msgaluno)
                    a = validarint(msgescolha, "Escolha inválida", 1, 3)
                    a += 3


            if o == 1:
                z = input("Digite o código do aluno: ")

                try:
                    z = int(z)
                    z = str(z)[-6:]
                except:
                    z = 999999

                email.append(removeracento(nome[x].split(" ")[0]) + "." + str(z).zfill(6) + "@gammon.br")
            elif o == 2:
                email.append(removeracento(nome[x].split(" ")[0]) + "." + removeracento(sobrenome[x]) + "@gammon.br")

            senha.append(senha_gammon)
        elif y == 2:
            if o1 == "N":
                print("Escolha a organização")
                o = validarint("1 - Alunos\n2 - Professores", "Escolha uma das opções a seguir", 1, 3)

                if o == 1:# Escolher curso do aluno
                    print("Escolha o curso do aluno")
                    a = validarint("1 - Administração\n2 - Educação Física - Bacharelado\n3 - Educação Física - Licenciatura\n4 - Pedagogia\n5 - Sistemas de Informação\n6 - Tecnologia em Redes de Computadores", "Escolha inválida", 1, 7)
                    a += 5
                elif o == 2:
                    a = 12

            email.append(removeracento(nome[x].split(" ")[0]) + "." + removeracento(sobrenome[x]) + "@fagammon.edu.br")
            senha.append(senha_faculdade)
        elif y == 3:
            if o1 == "N":
                print("Defina a unidade (padrão=1)")
                u = validarint("1 - Gammon\n2 - Fagammon", "Defina a unidade", 1, 3)

            if u == 1:
                email.append(removeracento(nome[x].split(" ")[0]) + "." + removeracento(sobrenome[x]) + "@gammon.br")
                senha.append(senha_gammon)
            elif u == 2:
                email.append(removeracento(nome[x].split(" ")[0]) + "." + removeracento(sobrenome[x]) + "@fagammon.edu.br")
                senha.append(senha_faculdade)

            a = 13

        org_unid.append(unidade(a))

        if len(nome) > 1 and o1 == "N":
            o1 = VF("Todos os usuários vão ser da mesma unidade organizacional?(S/N)")

    csv = filedialog.asksaveasfilename(initialdir=path.dirname(pathcsv), defaultextension=".csv", filetypes=[("Arquivos CSV", ".csv")], initialfile="users.csv")
    csv = open(csv, mode="w", encoding="utf8")
    pathcsv = csv.name
    csv.write(",".join(cabecalho) + "\n")

    for x in range(len(nome)):
        csv.write(nome[x] + "," + sobrenome[x] + "," + email[x] + "," + senha[x] + "," + org_unid[x] + "," + mudar_senha[x] + "\n")

    csv.close()

    return ""#nome + sobrenome + email + senha + mudar_senha + org_unid# + nome_minusc

opcao = validarint(
    "       Escolha uma das opções:\n"
    "1 - Criar planilha de novos e-mails\n"
    "2 - Criar planilha para inativar e-mails ou alterar unidade organizacional\n"
    "3 - Criar planilha de novos usuários Biblioteca Virtual\n"
    "4 - Criar planilha para inativar usuários Biblioteca Virtual\n",
    "Nenhuma opção correta foi atingida",
    1, 5
)

qualfunc(opcao)
lerarq = open(pathcsv, mode="r", encoding="utf8").readlines()
viewplanilha(6, lerarq)