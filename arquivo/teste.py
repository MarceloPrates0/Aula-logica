import os
os.system("cls ||clear")

# with open('arqlogin.txt', 'a', encoding = "UTF-8") as arquivo:
#     login = input("Insira seu login: ")
#     arquivo.write(login + "\n")

# print(arquivo)

arquivo = open('/workspaces/Aula-logica/arquivo/arqlogin.txt', 'a')
login = input("Insira seu login: ")
arquivo.write(login + "\n")
arquivo.close()
