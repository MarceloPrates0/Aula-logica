import os
os.system ("clear")

login= input("Insira seu login: ")

senha= input("\nInsira sua senha: ")

if login != "Marcelo" or senha != "1020":
    print("Login incorreto.")
else:
    print("Seja bem vindo!")
    