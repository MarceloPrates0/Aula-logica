import os
os.system ("cls || clear")

contador = 0
pares = 0
impares = 0
valor_pares = 0
numero_total = 0
while True:
    numero = int(input("Insira seu número: "))
    contador += 1
    numero_total += numero
    if numero % 2 == 0:
        pares += 1
        valor_pares += numero
    else:
        impares += 1
    if numero == 0:
        break

valor_pares_media = valor_pares / (pares - 1)
valor_geral = numero_total / (contador - 1)
print(f"Você colocou {pares - 1} números pares e {impares} números impares.")
print(f"A média dos valores pares é {valor_pares_media}")
print(f"A média geral é {valor_geral}")