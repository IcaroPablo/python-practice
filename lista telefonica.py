# programa da lista telefonica

import os
agenda = []  # vetor agenda, onde ficarao os contatos
dig = 1  # pra funcao 'menu' nao ficar bugada

class contato(object):  # criando a class do contato
    def __init__(self, nome, email, ddd, telefone, rua, numero, complemento, bairro, cep, cidade, estado, pais, dia, mes, ano, anotacao):
        self.nome = nome
        self.ddd = ddd
        self.telefone = telefone
        self.email = email
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def func_nome(self):
        print "nome: ", self.nome

    def func_telefone(self):
        print "telefone: (%s) %s" %(self.ddd, self.telefone)

    def func_email(self):  # funcao para o email
        print "email: ", self.email

    def func_endereco(self):  # funcao para o endereco
        print "endereco:"
        print "  rua: ", self.rua
        print "  numero: ", self.numero
        print "  complemento: ", self.complemento
        print "  bairro: ", self.bairro
        print "  cep: ", self.cep
        print "  cidade: ", self.cidade
        print "  estado: ", self.estado
        print "  pais: ", self.pais

    def func_aniversario(self):
        print "aniversario: %s/%s/%s" % (self.dia, self.mes, self.ano)

    def func_note(self):
        print "anotacao:\n   ", self.anotacao

def cadastro(): # funcao para cadastro de novo contato
    # abrir um arquivo q diz o numero de contatos registrados
    # os.system(alguma coisa)# criar um arquivo para cada conta
    # ler o numero de contas q ja foram criadas (agenda.len)
    # usar .append em agenda para criar uma nova conta --> agenda.append(len(agenda))
    # novo valor da lista --> "p[len(agenda)]"
    if len(agenda) <= 100:  # contador de contas, quantidade maxima = 100
        tam = len(agenda)  # tam e igual ao numero de contatos na agenda
        print("DADOS BASICOS")
        nome = str(raw_input("\ndigite o nome da pessoa: "))
        telefone = str(raw_input("digite o telefone da pessoa: "))
        ddd = str(raw_input("digite o ddd da pessoa: "))
        email = str(raw_input("digite o email da pessoa: "))
        print("\nENDERECO")
        rua = str(raw_input("\ndigite o nome da rua da pessoa: "))
        numero = str(raw_input("digite o numero da casa da pessoa: "))
        complemento = str(raw_input("digite o complemento do endereco da pessoa: "))
        bairro = str(raw_input("digite o bairro da pessoa: "))
        cep = str(raw_input("digite o cep da pessoa: "))
        cidade = str(raw_input("digite o nome da cidade da pessoa: "))
        estado = str(raw_input("digite o nome  do estado da pessoa: "))
        pais = str(raw_input("digite o nome do pais da pessoa: "))
        print("\nDADOS PESSOAIS")
        dia = str(raw_input("\ndigite o dia do aniversario da pessoa: "))
        mes = str(raw_input("digite o mes do aniversario da pessoa: "))
        ano = str(raw_input("digite o ano do aniversario da pessoa: "))
        anotacao = str(raw_input("digite alguma anotacao sobre a pessoa: "))
        agenda.append(tam)
        agenda[tam] = contato(nome, email, ddd, telefone, rua, numero, complemento, bairro, cep, cidade, estado, pais, dia, mes, ano, anotacao)  # o novo termo de agenda eh classe contato

    else:
        print "numero maximo de contas atingido"

    if len(agenda) >= 2:
        organizar()

def menu():
    os.system("cls")
    print "iniciando lista telefonica"
    print "digite o q vc deseja:"
    print "\n1 - cadastrar novo contato"
    print "2 - excluir contato"
    print "3 - buscar contato"
    print "4 - exibir agenda"
    print "5 - sair"

    global dig

    dig = input("\n>>>")
    if dig == 1:
        os.system("cls")
        cadastro()

    if dig == 2:
        os.system("cls")
        excluir()

    if dig == 3:
        os.system("cls")
        buscar()

    if dig == 4:
        os.system("cls")
        exibir()

    os.system("pause")

def excluir():  # bugada
    a = 0
    var = 0
    print "agenda:\n"
    for x in ordem2:
        print x, "\n"

    resp = raw_input("digite o nome do contato q vc quer excluir\n>>>")
    for x in range(0, len(agenda)):
        if agenda[x].nome == resp:
            aux = agenda[x]
            agenda[x] = agenda[len(agenda) - 1]
            agenda[len(agenda) - 1] = aux
            var = agenda[x]
            a = x  # recebe o valor da atual posicao da class q deve voltar para ultimo lugar na lista
            break

    b = a + 1  # recebe o valor da posicao posterior a de 'a'
    agenda.pop()  # retira o elemento desejado da lista
    while b != len(agenda):  # organizar os elementos da agenda
        agenda[a] = agenda[b]  # valores a partir de 'a' vao recebendo valores posteriores ate o final
        a += 1
        b += 1

    agenda[len(agenda) - 1] = var  # o ultimo elemento de agenda recebe seu verdadeiro valor

def buscar():
    opt = input("escolha o tipo de pesquisa:\n\n1 - nome\n2 - dia e mes de aniversario\n3 - mes de aniversario\n\n>>>")
    if opt == 1:  # busca por nome
        busca = raw_input("digite o nome do contato que vc esta procurando: ")
        for c in range(0, len(agenda)):
            if agenda[c].nome == busca:
                print "exibindo cadastro(s) procurados(s)"
                agenda[c].func_nome()
                agenda[c].func_telefone()
                agenda[c].func_email()
                resp = input("\nexibir tudo?\n1 - sim\n2 - nao\n>>>")
                if resp == 1:
                    os.system("cls")
                    agenda[c].func_nome()
                    agenda[c].func_telefone()
                    agenda[c].func_email()
                    agenda[c].func_endereco()
                    agenda[c].func_aniversario()
                    agenda[c].func_note()

    if opt == 2:  # busca por dia e mes de aniversario
        busca = raw_input("digite apenas o dia do aniversario do contato que vc esta procurando: ")
        busca1 = raw_input("digite o mes do aniversario do contato que vc esta procurando: ")
        for c in range(0, len(agenda)):
            if agenda[c].dia == busca and agenda[c].mes == busca1:
                print "exibindo cadastro(s) procurado(s)"
                agenda[c].func_nome()
                agenda[c].func_telefone()
                agenda[c].func_email()
                resp = input("\nexibir tudo?\n1 - sim\n2 - nao\n>>>")
                if resp == 1:
                    os.system("cls")
                    agenda[c].func_nome()
                    agenda[c].func_telefone()
                    agenda[c].func_email()
                    agenda[c].func_endereco()
                    agenda[c].func_aniversario()
                    agenda[c].func_note()

    if opt == 3:  # busca por mes de aniversario
        busca = raw_input("digite o mes de aniversario do contato que vc esta procurando: ")
        for c in range(0, len(agenda)):
            if agenda[c].mes == busca:
                print "exibindo cadastro(s) procurado(s)"
                agenda[c].func_nome()
                agenda[c].func_telefone()
                agenda[c].func_email()
                resp = input("\nexibir tudo?\n1 - sim\n2 - nao\n>>>")
                if resp == 1:
                    os.system("cls")
                    agenda[c].func_nome()
                    agenda[c].func_telefone()
                    agenda[c].func_email()
                    agenda[c].func_endereco()
                    agenda[c].func_aniversario()
                    agenda[c].func_note()

def exibir():
    print "agenda:\n"
    for x in ordem2:
        print x, "\n"

    resp = raw_input("escolha o contato:\n>>>")
    os.system("cls")
    print "exibindo cadastro de ", resp, "\n"
    for x in agenda:
        if x.nome == resp:
            x.func_nome()
            x.func_telefone()
            x.func_email()
            resp2 = input("\nexibir tudo?\n1 - sim\n2 - nao\n>>>")
            if resp2 == 1:
                os.system("cls")
                x.func_nome()
                x.func_telefone()
                x.func_email()
                x.func_endereco()
                x.func_aniversario()
                x.func_note()

def organizar():
    letra1 = []  # vetor com a primeira letra de cada nome
    letra1ordem = [] # vetor com as letrsa de letra1 organizadas
    ordemden = []  # vetor com os numeros das primeiras letras de cada nome
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ordem = []  # vetor com os nomes de agenda
    global ordem2
    ordem2 = []  # vetor com os elementos de 'ordem' organizados
    n = 0
    while len(ordem) < len(agenda):  # pegando cada nome do vetor 'agenda'
        ordem.append(agenda[n].nome)
        n += 1

    for x in agenda:  # pegando a primeira letra de cada nome
        letra1.append(x.nome[0])

    for n in range(0, len(letra1)):  # pegando a posicao de cada letra em 'letra1' no vetor 'alfabeto'
        for x in range(0, len(alfabeto)):
            if alfabeto[x] == letra1[n]:
                ordemden.append(x)

    aux = 0

    for n in range(0, len(ordem)):  # organizando os numeros de 'ordemden'
        for m in range(n, len(ordem)):
            if ordemden[n] > ordemden[m]:
                aux = ordemden[n]
                ordemden[n] = ordemden[m]
                ordemden[m] = aux

    for x in ordemden:  # colocando as letras em ordem alfabetica no vetor 'letra1ordem'
        letra1ordem.append(alfabeto[x])

    for x in letra1ordem:
        for y in agenda:
            if y.nome[0] == x:
                ordem2.append(y.nome)

while dig != 5:  # execucao
    menu()
