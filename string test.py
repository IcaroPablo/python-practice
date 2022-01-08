
print "na verdade isso e um teste com vetores e.e"
print "vou criar o vetor 'vetor' e.e"

for r in range(0,100):
    print "........carregando........"
print "deve ter dado certo, quer que eu adicione alguma coisa ao vetor (se vc digitar 'sim' vai dar um bug)?"
resposta = raw_input(">")
i = 0

if resposta == "sim":
    ndi = input("quantos itens vc quer q eu adicione no vetor ?\n>")
    ndi2 = int(ndi)
    vetor = [ndi2]
    
    for i in range(0,ndi2):
        vetor[i] = raw_input("digite >")
        print "vc adicionou %s" %vetor[i]
    print vetor
    print "ok entao, vamos para o proximo passo"
else: 
    print "ok entao, vamos para a proxima etapa, ja q a anterior deu merda\n"
   
print "testes com o comando '.append()'"
elements = []
vetor2 = []
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand 
    elements.append(i)
    
print "digite sim pra pular essa etapa (ou qualquer outra coisa pra dar bug)"
h = raw_input(">")
if h != "sim":
    vetor2[3] = raw_input("adicione algo ao vetor2[3]")
    print vetor2

print "outro bug, digite 'ok' para pular"

v = raw_input("vai dar merda\n>")
if v != "ok":
    print "criei um novo vetor chamado vetor3, quantos elementos vc quer q eu adicione ao vetor3?"
    v3 = raw_input(">")
    v4 = int(v3)
    vetor3 = [v3]
    for j in range(0,v4):
        vetor3[j] = raw_input("digite >")
        print "vc adicionou", vetor3[j]
    print "o vetor3 foi completado"
print "teste com '.append()' dnv"
vetorteste = []
m = raw_input("digite alguma coisa\n>")
vetorteste.append(m)
print "vc adicionou  ao %s 'vetorteste' " % vetorteste
print "o vetorteste e", vetorteste

print "ok agora vou tentari um novo metodo"
num = raw_input("digite a quantidade de elementos q vc quer adicionar ao vetor lista\n>")
lista = []
num = int(num)
for g in range(0,num):
    print "adicionando slot", g
    lista.append(g)

print lista

x = lista.len()

for s in range(0,x):
    lista[s] = raw_input("digite\n>")

print lista
