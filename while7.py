import os
os.system ("clear")
login = "Marcelo"
senha = "1515"
insira_l = input("Insira seu login: ")
insira_S = input("Insira sua senha: ")
while True:
    if insira_l != login and insira_S != senha:
        for i in range(1, 3):
            print("Login ou senha incorretos.")
            insira_l
            insira_S 
        print("Você excedeu o número de tentativas.")
        
    else:
        print("Acesso permitido")
        break
