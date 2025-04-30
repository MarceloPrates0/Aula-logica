from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: float
    peso: float
    altura: float

    def exibirDado(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso} | Altura: {self.altura}\n")

QTD_PESSOAS = 4
listaPessoas = []

for i in range(QTD_PESSOAS):
    pessoas = Pessoa(
        input("Insira seu nome: "),
        float(input("Insira sua idade: ")),
        float(input("Insira seu peso: ")),
        float(input("Insira sua altura: "))
    )
    print()
    listaPessoas.append(pessoas)


os.system("cls || clear")
print("===EXIBINDO DADOS===")
for pessoas in listaPessoas:
    pessoas.exibirDado()