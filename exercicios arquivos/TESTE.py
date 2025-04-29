import os
os.system("cls || clear")

acumulante= 0
def tabuada(numero, multiplicador):
    return numero * multiplicador

algarismo = int(input("Insira um número: "))
for i in range(1, 11):
    tabuada = tabuada(algarismo, i)
    print(f"{algarismo} x {i} = {tabuada}")
