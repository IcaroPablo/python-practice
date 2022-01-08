print "criando um dicionario de 5 'slots':"
slot=["slot0","slot1","slot2","slot3","slot4"]
dic = {slot[0]:"termo0",
       slot[1]:"termo1",
       slot[2]:"termo2",
       slot[3]:"termo3",
       slot[4]:"termo4"
       }
print"-"*50
nome = ["a"]
nome.pop()
a=0
while a < 5:
    nome.append(raw_input("digite algo para o slot %d:\n" %a))
    a=a+1

print "exibindo vetor 'nome':"
print nome

print "exibindo dicionario 'dic':"
print dic
print "\nadicionando termos digitados ao dicionario 'dic'"
a=0
while a < 5:
    dic[slot[a]]=nome[a]
    a=a+1
print"-"*50

print "exibindo dicionario 'dic':"
print dic

b=raw_input("fim")