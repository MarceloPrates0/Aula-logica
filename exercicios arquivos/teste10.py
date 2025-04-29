import os
os.system("cls || clear")

print("===Consumo médio de combustível===")

quilometros = int(input("Quantos quilômetros percorridos: "))
combustivel = float(input("Quantos litros de combustível: "))

total = quilometros / combustivel

print(f"{total:.3f} km/l")  