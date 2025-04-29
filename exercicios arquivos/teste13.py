import os
os.system("cls || clear")

def conversorZero(algarismo):
    if algarismo < 0:
        algarismo = 0
    return algarismo

VOLTAS = 5
numeros = []

for i in range(VOLTAS):
    numero = int(input("Insira um número: "))
    conversor = conversorZero(numero)
    numeros.append(conversor)

print()
for i, conversor in enumerate(numeros, start=1):
    print(f"{i}º número: {conversor}")