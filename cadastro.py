import os      
os.system ("clear")

login = ["Marcelo", "Gabriel,", "Rafaela"]

login_entrada = input("Cadastre seu login: ")

if login_entrada in login:
    print("Login ja cadastrado.")
else:
    senha = [4530, 2059]

    senha_entrada = int(input("Cadastre uma senha: "))

    if senha_entrada in senha:
        print("Senha ja cadastrada.")

    if login_entrada not in login and senha_entrada not in senha:
        print("Login cadastrado com sucesso.")









