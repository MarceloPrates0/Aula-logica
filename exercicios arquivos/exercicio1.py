import os
os.system("cls || clear")

print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt','a')
arquivo.write(texto + "\n")
print("Operação concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()

print("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()