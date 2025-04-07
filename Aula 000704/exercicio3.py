import os
os.system("cls || clear")

def algarismo(par_impar):
    if par_impar % 2 == 0:
        print("É par")
    else:
        print("É impar")
        
numero = int(input("Insira um número: "))
algarismo(numero)