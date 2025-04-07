import os
os.system("cls || clear")

def subtracao(numero1, numero2):
    subtrair = numero1 - numero2
    total = print(f"Total da subtração: {subtrair}")
    return total
def adicao(numero1, numero2):
    adicionar = numero1 + numero2
    total = print(f"Total da adição: {adicionar}")
    return total
def multiplicacao(numero1, numero2):
    multiplicar = numero1 * numero2
    total = print(f"Total da multiplicação: {multiplicar}")
    return total
def divisao(numero1, numero2):
    dividir = numero1 / numero2
    total = print(f"Total da divisão: {dividir}")
    return total

algarismo1 = float(input("Insira o primeiro numero: "))
algarismo2 = float(input("Insira o segunda numero: "))
print()
subtracao(algarismo1, algarismo2)
adicao(algarismo1, algarismo2)
multiplicacao(algarismo1, algarismo2)
divisao(algarismo1, algarismo2)
