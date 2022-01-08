print 'iniciando testes com arquivos'
arq_var = open('/mnt/sdcard/com.hipipal.qpyplus/scripts/arq.txt')
escreva = raw_input('escreva alguma coisa para ser adicionada ao arquivo arq.txt:\n')
arq_var.write(escreva)
print arq_var.read() 
arq_var.close()