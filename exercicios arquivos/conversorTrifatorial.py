# Desenvolva um algoritmo em que o usuario insira três inteiros no objetivo de se calcular o 
# fatorial deles. Utilize array e função def

import os
os.system("cls || clear")

def fatorar(algarismo):
    contador = 1
    total = 1
    for contador in range(1, algarismo):
        contador +=1
        total *= contador
    return total


def msg():
    print("===CONVERSOR FATORIAL===")


listaN = []
fatoriais = []
QUANTIDADE_VEZES = 3

msg()
for i in range(QUANTIDADE_VEZES):
    fator = int(input("Insira um numero: "))
    numerosInse = listaN.append(fator)
    fatorando = fatorar(fator)
    fatoriais.append(fatorando)

os.system("cls || clear")
msg()

for i, (fator, fatorando) in enumerate(zip(listaN, fatoriais), start=1):
    print(f"{i}ª conversão: {fator}! = {fatorando}")