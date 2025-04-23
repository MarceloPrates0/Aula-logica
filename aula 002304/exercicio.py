import os
os.system("cls || clear")

listNum = []
par = 0
impar = 0

for i in range(1, 7):
    numero = int(input("Insira um numero: "))
    listNum.append(numero)
    if numero % 2 == 0:
        par +=1
    else:
        impar+=1


print(f"Você inseriu {par} pares e {impar} impares : ")

for i, numero in enumerate(listNum, start=1):
    print(f"{i}: {numero}")

