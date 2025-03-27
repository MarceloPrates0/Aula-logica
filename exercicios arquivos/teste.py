import os
os.system ("cls || clear")

arquivo = open('arq01.txt', 'r')
print('Posição atual no arquivo: ' + arquivo.tell(1))
print(arquivo.read())
print('Posição atual no arquivo: ' + arquivo.tell(2))
print(arquivo.read())
arquivo.seek(0)
print('Posição atual no arquivo: ' + arquivo.tell(3))
print(arquivo.read())
arquivo.close()