from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass

class Indiv:
    nome: str
    idade: int
    peso: float
    altura: float

def IMC(a, p):
    i = p / (a ** 2)
    return i

nomeP = input("Insira seu nome: ")
idadeP = int(input("Insira sua idade: "))
pesoP = float(input("Insira seu peso: "))
alturaP = float(input("Insira sua altura: "))

coletanea = Indiv(nomeP, idadeP, pesoP, alturaP)
im = IMC(coletanea.peso, coletanea.altura)
print(f"Seu nome: {coletanea.nome} \nSua idade: {coletanea.idade} \nSeu peso: {coletanea.peso} \nSua altura: {coletanea.altura}")
print(f"Seu IMC: {im}")