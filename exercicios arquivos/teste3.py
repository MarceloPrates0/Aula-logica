import os
os.system("cls || clear")

def media(divisor, dividendo):
    media = divisor / dividendo
    return media

acumulador = 0
for i in range(1, 3):
    numero = int(input("Insira um numero: "))
    acumulador += numero

total = media(acumulador, i)
print(f"Sua media: {total}")
