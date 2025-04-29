import os
os.system("cls || clear")

print("===Conversão Metros===")

metros = int(input("Insira uma quantidade em metro: "))

quilometro = metros // 1000
restoConversor = metros % 1000
hectometro = restoConversor // 100

conversorDecametro = restoConversor % 100
decametro = conversorDecametro // 10
metro = restoConversor % 10

print()
print(f"{metros}m dão: {quilometro}km; {hectometro}hm; {decametro}dam; {metro}m.")
