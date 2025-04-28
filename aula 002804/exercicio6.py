from dataclasses import dataclass
import os
os.system("cls || clear")


@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

    


@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def exibicao(self):
        print("\n===SEUS DADOS INSERIDOS===")
        print(f"Seu nome: {self.nome}")
        print(f"Seu email: {self.email}")
        print("\n===Exibindo endereço===")
        print(f"Seu logradouro: {self.endereco.logradouro}")
        print(f"Seu número: {self.endereco.numero}")
        print(f"Sua cidade: {self.endereco.cidade}")


print("===Rastreador Correio===")

nome = input("Insira seu nome: ")
email = input("Insira seu email: ")

enderecoLogra = input("Insira seu o logradouro de seu endereço: ")
enderecoNum = input("Insira seu número de seu endereço: ")
enderecoCid = input("Insira a cidade de seu endereço: ")

endereco1 = Endereco(enderecoLogra, enderecoNum, enderecoCid)
tudo = Pessoa(nome, email, endereco1)
tudo.exibicao()

