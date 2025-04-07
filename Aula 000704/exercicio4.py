import os
os.system("cls || clear")

def positivo_negativo(algarismo):
    if algarismo < 0:
        print("É negativo.")
    elif algarismo == 0: 
        print("É neutro.")
    else:
        print("É positivo.")
        
numero = int(input("Insira um número: "))
positivo_negativo(numero)
        