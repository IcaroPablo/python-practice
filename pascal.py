#-*-coding:utf8;-*-

lmax = input("digite o numero de linhas para o triangulo: ")
cache = [1]
atual = [1]
cont = 0
tam = 0


def mod(lin):
    while len(lin) < cont - 1:
        lin.append(0)
    while len(atual) < cont:
        atual.append(0)
    tam = 0
    while tam < cont:
        if tam == len(lin) and len(lin) != 1 or tam == 0:
            atual[tam] = 1
        if tam != 0 or tam != len(lin):
            atual[tam] = lin[tam] + lin[tam-1]
        tam += 1
            
    print atual

while cont <= lmax:
    mod(cache)
    cache = atual
    cont += 1