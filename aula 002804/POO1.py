import os
from dataclasses import dataclass
os.system("cls || clear")

# POO


@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: Endereco
    def exibindo_dados(self):
        print(f"\nSeu nome: {self.nome}")
        print(f"Sua email: {self.email}")
        print(f"Seu telefone: {self.telefone}")
        print(f"Seu endereço: {self.endereco.logradouro}")

nomeSeu = input("Insira seu nome: ")
emailSeu = input("Insira seu email: ")
teleSeu = int(input("Insira seu telefone: "))
enderSeu = input("Insira seu endereço: ")

coletanea = Pessoa(nomeSeu, emailSeu, teleSeu, enderSeu)
coletanea.exibindo_dados()