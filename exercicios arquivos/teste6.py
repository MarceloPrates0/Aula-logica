import os
os.system("cls || clear")

def imc(peso, altura):
    indice_massa = peso / (altura * altura)
    return indice_massa

altura = float(input("Insira sua altura em metro: "))
peso = float(input("Insira seu peso em quilos: "))

if altura > 4:
    altura = altura / 100

print()
print(f"Seu IMC: {(imc(peso, altura)):.2f}")