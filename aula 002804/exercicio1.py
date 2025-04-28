import os
os.system("cls || clear")

def conversor(algarismo):
    if algarismo < 0:
        algarismo = 0
    return algarismo

listaNum = []
QTD = 5
for i in range(QTD):
    numero = int(input("Insira um número: "))
    convertido = conversor(numero)
    listaNum.append(convertido)

for i, convertido in enumerate(listaNum, start=1):
    print(f"{i}º Numero: {convertido}")

