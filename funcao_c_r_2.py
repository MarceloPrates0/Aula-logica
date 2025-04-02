import os
os.system("cls || clear")

def calculo_media(a):
    media = a / i
    return media
acumulador = 0
for i in range(1, 4):
    nota = int(input("Insira uma nota: "))
    acumulador += nota

media = calculo_media(acumulador)
print(f"Sua média: {media:.2f}")
