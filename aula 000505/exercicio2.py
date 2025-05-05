from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    dataNasci: str
    rg: str
    cpf: str

listaPess = []
QTD = 5

for i in range(QTD):
    individuo = Pessoa(input("Insira seu nome: "),
                       input("Insira sua data de nascimento: "),
                       input("Insira seu RG: "),
                       input("Insira seu CPF: "),)
    
    listaPess.append(individuo)

arquivo = "Funcionarios.txt"
with open(arquivo, "a") as gravaDados:
    for individuo in listaPess:
        gravaDados.write(f"{individuo.nome}, {individuo.dataNasci}, {individuo.rg}, {individuo.cpf}\n")

try:
    with open(arquivo, "r") as exibe_arquivo:
        linhas = exibe_arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}\n")
except FileExistsError:
    print("Arquivo não existe.")