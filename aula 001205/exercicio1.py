import os
import time
from dataclasses import dataclass
os.system("cls || clear")

arquivo = "dadosFuncio.txt"
@dataclass
class Funcionario:
    nome: str
    dataN: str
    cpf: str
    funcao: str

def adicionar(usuario):
    with open(arquivo, "a") as gravaDados:
        gravaDados.write(f"{usuario.nome} | {usuario.dataN} | {usuario.cpf} | {usuario.funcao} ")

def exibir():
    with open(arquivo, "r") as exibeDados:
        linhas = exibeDados.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")

def atualizar(usuario):
    nome_antigo = input("Insira o nome que deseja atualizar: ")
    if nome_antigo in arquivo:
        print("Está")

while True:
    print("==GERENCIADOS FUNCIONÁRIOS==")
    print("""
1 - Adicionar funcionário
2 - Listas nomes
3 - Atualizar
4 - Excluir""")
    ordem = int(input("Selecione uma opção: "))
    match ordem:
        case 1:
            funcionario1 = Funcionario(input("Insira seu nome: "),
                             input("Insira a data de seu nascimento: "), 
                             input("Insira o seu CPF: "), 
                             input("Insira a sua função: "), 
                             )
            adicionar(funcionario1)
        case 2:
            exibir()
        case 3:
            atualizar()
    time.sleep(3)
    os.system("cls || clear")



