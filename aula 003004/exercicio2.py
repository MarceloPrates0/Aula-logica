from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"\nNome: {self.nome} \nIdade: {self.idade}\n")

listaPaci = []
QTD_PACI = 1
for i in range(QTD_PACI):
    paciente1 = Paciente(
        input("Insira seu nome: "),
        int(input("Insira sua idade: "))
    )
    listaPaci.append(paciente1)

arquivo = "arqDado.txt"
with open(arquivo, "a") as arquivo_pessoas:
    for pessoas in listaPaci: 
        arquivo_pessoas.write(f"Paciente: {paciente1.nome} | Idade: {paciente1.idade}")



print("===Pessoas===")
for paciente1 in listaPaci:
    paciente1.exibir_dados()