import os
os.system("cls || clear")

TdsNotas = []

def maior(numero):
    maior = max(numero)
    return maior

def menor(numero):
    menor = min(numero)
    return menor

for o in range(5):
    nota = float(input("Insira uma nota: "))
    TdsNotas.append(nota)

for i, nota in enumerate(TdsNotas, start=1):
    print(f"{i}ª nota: {nota}")

print(f"\nA menor nota: {menor(TdsNotas)}")
print(f"A maior nota: {maior(TdsNotas)}")