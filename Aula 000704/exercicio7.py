import os
os.system("cls || clear")

def centimetros(metro):
    conversao = metro * 100
    total = print(f"Seus {metro}m correspondem a:\n{conversao}cm.")
    return total

numero = int(input("Insira uma quantiade de metros: "))
centimetros(numero)