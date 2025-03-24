import os
os.system("clear")

login = ["Marcelo"]
senha = ["1515"]

for i in range(3):
    inserir_l = input("Insira seu login: ")
    inserir_s = input("Insira sua senha: ")
        
    if inserir_l in login and inserir_s in senha:
        print("Acesso permitido")
        break
    else:
        print("Login errado ou senha errados.")
        if i == 2:
            print("Número excedente de tentativas.")
            
            
            

        