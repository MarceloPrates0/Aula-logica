import os
from dataclasses import dataclass

os.system("cls || clear")
@dataclass

class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str


pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet("Pitoco", 5, "Vira-lata")

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")

print()
print(f"Raça: {pet1.raca}, idade: {pet1.idade}, nome: {pet1.nome}.")
