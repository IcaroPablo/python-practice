import os
import random

#contadores:
#c1=0 contador de erros
#c2=0 contador de elementos na string
#c3=0 contador de letras iguais
#c4=0 contador de erros

#e=0 verificar se ha letras digitadas ou nao

resp = 1

while resp == 1:
    os.system("clear")

    letra = "0"

    p0 = "o n i b u s"
    dica0 = "transporte coletivo"

    p1 = "b a l e i a"
    dica1 = "mamifero marinho"

    p2 = "e s p a d a"
    dica2 = "usada por samurais"

    p3 = "c h a p e u"
    dica3 = "arma do kung lao"

    p4 = "f o g o"
    dica4 = "maior exemplo de plasma"

    p5 = "f o g u e t e"
    dica5 = "nasa"

    p6 = "d e n t i s t a"
    dica6 = "motorzinho irritante no consultorio"

    p7 = "m a c a r r o n a d a"
    dica7 = "prato feito com macarrao"

    p8 = "l a r a n j a"
    dica8 = "uma fruta com o nome de uma cor"

    p9 = "a m e r i c a"
    dica9 = "o nome do seu continente"

    pal = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]
    dica = [dica0, dica1, dica2, dica3, dica4, dica5, dica6, dica7, dica8, dica9]
    dig = []  # criando lista de letras digitadas
    c4 = 0
    forca = random.choice(pal)  # atribuindo a p1 uma palavra randomica

    for j in range(0, 10):
        if pal[j] == forca:
            dicaforca = dica[j]

    c1 = 0
    e = 0
    print "iniciando jogo da forca;"
    print "essa eh a palavra sorteada:"
    pgen1 = "_ " * len(forca.split())
    print pgen1
    while (c1 < 7) and (pgen1 != forca):  # iniciando o jogo em si
        c2 = 0
        c3 = 0
        if c1 == 6:
            print "exibindo dica: ", dicaforca

        letra = str(raw_input("digite uma letra:\n>>>"))
        #os.system('cls')  # comando de limpeza de tela
        os.system('clear')

        dig = "-".join(dig)  # juntando letras digitadas para funcionar como string
        x = dig.find(letra)  # procurando letras ja digitadas
        dig = dig.split("-")  # separando letras digitadas em lista novamente
        if x == -1:
            dig.append(letra)  # registro de letras digitadas

        forca = forca.split()  # separacao em lista
        pgen1 = pgen1.split()  # separacao em lista

        while c2 < len(forca):  # "leitura" da palavra
            if letra == forca[c2]:
                c3 = c3 + 1  # contagem de letras iguais na palavra
                pgen1[c2] = forca[c2]  # substituicao de caracteres
            c2 = c2 + 1

        print "%i letra(s) '%c' encontradas" % (c3, letra)

        pgen1 = ' '.join(pgen1)  # juncao em string
        forca = ' '.join(forca)  # juncao em string
        e = forca.find(letra)
        if e == -1:
            c4 = c4 + 1

        print pgen1  # exibir palavra generica alterada
        print dig  # exibir letras digitadas
        print "vc pode errar mais %i vezes" % (7 - c4)

        if x != -1:
            print "letra ja digitada"

        if c3 == 0:  # contador de erros
            c1 = c1 + 1

    if pgen1 == forca:
        print "vc venceu :D"
    if pgen1 != forca:
        print "vc perdeu D:"

    forca = ''.join([x for x in forca if x != ' '])
    print "a palavra eh: ", forca
    resp = int(raw_input("continuar jogando ?\n1 - sim\n2 - nao\n>>>"))