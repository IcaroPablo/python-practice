print "iniciando um teste com ordenacao de vetores"
vetor=[1,2,3,4,5,6,7,8,9,10]
aux=0
a=9
b=0
c=0
def ord():

    print "tentando fazer um metodo de ordenacao de vetores em python:"
    for c in range(0,10):
        vetor[c] = raw_input("digite um numero inteiro:")
    for a in range(0,10):
        for b in range(0,10):
            if vetor[a]>vetor[b]:
                aux = vetor[a]
                vetor[a]=vetor[b]
                vetor[b]=aux

quick()
def bubble():
    for c in range(0,10):
        vetor[c] = raw_input("digite um numero inteiro:")
    for a in range(9,0): # bubble sort
        for b in range(0,a):
            if vetor[a] < vetor[b+1]:
                aux = vetor[b]
                vetor[b] = vetor[b+1]
                vetor[b+1] = aux
def teste():
    x = "frase"

print teste()

bubble()

print "mudando alguns elementos de 'vetor': vetor[3]->(oi) e vetor[4]->(5)"
print vetor
vetor[3]='oi'
vetor[4]=5
print vetor[3],vetor[5]

