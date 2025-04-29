import os
os.system("cls || clear")

def par_impar(numero):
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número impar")

algarismo=  int(input("Insira um número: "))
par_impar(algarismo)