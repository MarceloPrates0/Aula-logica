from dataclasses import dataclass
import os 
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int

    def exibir(self):
        print(f"Seu nome: {self.nome}\nSua idade: {self.idade}")


nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
pessoa1 = Pessoa(nome, idade)

pessoa1.exibir()
