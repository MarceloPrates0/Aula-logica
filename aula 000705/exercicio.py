from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass 

class Cliente:
    nome: str
    dataN: str
    endereco: str


@dataclass

class Funcionario:
    nome: str
    dataN: str
    matricula: int
    endereco: str
    
QTD = 3
clientes = []
funcionarios = []
for i in range(QTD):
    funcionario1 = Funcionario(input("Insira seu nome: "),
                       input("Insira sua data de nascimento: "),
                       int(input("Insira sua matricula: ")),
                       input("Insira seu endereço: "))
    funcionarios.append(funcionario1)


for i in range(QTD):
    cliente1 = Cliente(input("Insira seu nome: "),
                       input("Insira sua data de nascimento: "),
                       input("Insira seu endereço: "))
    clientes.append(cliente1)

arquivo1 = 'dadosFuncionario.txt'
arquivo2 = 'dadosClientes.txt'

with open(arquivo1, 'a') as grava_dado:
    for funcionario1 in funcionarios:
        grava_dado.write(f"{funcionario1.nome} | {funcionario1.dataN} | {funcionario1.matricula} | {funcionario1.endereco}\n")


with open(arquivo2, 'a') as grava_dado2:
    for cliente1 in clientes:
        grava_dado2.write(f"{cliente1.nome} | {cliente1.dataN} | {cliente1.endereco}\n")
os.system("cls || clear")
print("===DADOS SALVOS===")