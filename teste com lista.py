lista = "1 2 3 4 5"
lista = lista.split()
algo = [1,2,3,2,5]
print lista[3]
num = raw_input("digite um numero inteiro menor q 5: ")
num = int(num)
while num > 0:
    lista.append(lista[num])
    num = num - 1

print lista

lista = ",".join(lista)

print lista.find("2")