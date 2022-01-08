print "iniciando testes com class"
print "criando class 'coisa'"

class coisa(object):
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
    
    def func1(self):
        print "printando self.var1: ", self.var1
        print "printando self.var2: ", self.var2
        
texto = str(raw_input("digite alguma string: "))
numero = int(raw_input("digite um numero inteiro: "))
        
teste = coisa(texto,numero)
teste.func1()
    
