import os
os.system("cls || clear")

def impar_par(algarismo):
    par = 0
    impar = 0
    if algarismo % 2 == 0:
        par += algarismo
    else:
        impar += 1
    return par, impar


lista_numeros = []
QUANTIDADE = 5
pares = 0
impares = 0


for i in range(QUANTIDADE):
    numero = int(input("Insira um número: "))
    lista_numeros.append(numero)
    par, impar = impar_par(numero)
    pares += par
    impares += impar

for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}º Nº: {numero}")


print()
print(f"A soma total de numeros pares foi de: {pares}")
print(f"A quantidade de números impares inseridos foi de: {impares}")
