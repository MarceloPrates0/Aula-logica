import os
os.system ("cls || clear")

contador = 0
soma = 0
while True:
    valor = float(input("Insira um valor: "))
    if valor > 0:
        soma += valor
        contador += 1
    else:
        break

media = soma / contador
print(f"\nSua média de números positivos: {media:.2f}")