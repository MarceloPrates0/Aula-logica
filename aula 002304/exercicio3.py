import os
os.system("cls || clear")

lista_numero = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = int(input("Insira um número: "))
    lista_numero.append(numero)

def positivo(algarismo):
    soma = 0
    if algarismo > 0:
        soma += algarismo
    return soma

print(positivo(lista_numero))   