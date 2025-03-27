import os
os.system ("cls || clear")

while True:
    permissao = int(input("1 - Adicionar; 2 - Visualizar; 3 - Sair"))
    match permissao:
        case 1: 
            login = input("Insira seu login: ")
            arquivo_login = open('arqlogin.txt', 'a')
            arquivo_login.write(login + "\n")
            arquivo_login.close()
            
            senha = input("Insira sua senha: ")
            arquivo_senha = open('arqsenha.txt', 'a')
            arquivo_senha.write(senha + "\n")
            arquivo_senha.close()

        case 2:
            print(login)
            print(senha)
            with open(arquivo_login, 'r') as file:
                linhas = file.readlines()
            print(linhas)
        case 3:
            break
        case _:
            print("Número inválido.")
