#-*-coding:utf8;-*-
#qpy:2
#qpy:console
print 'iniciando testes com funcoes'
def teste1(x):
    print 'a funcao deve exibir a string: %s' %x
    return 2

x = 'testando a funcao'
y = 'testando de novo'

teste1(x)
teste1(y)

var_1 = 10
print 'o valor de var_1 é %r' %var_1

def teste2(var_1):
    var_2 = var_1*50
    return var_2
    
var_2 = teste2(var_1)
    
var_1 = teste2(var_1)
    
print 'agora o valor de var_1 e %r' %var_1

print teste1(x)
print var_2
