import os
os.system("cls || clear")

def tabuada(numero, mult):
    return  numero * mult

algarismo = int(input("Insira um número: "))
while algarismo > 9:
    print("Insira um número abaixo de 10")
    algarismo = int(input("Insira um número: "))

for i in range(1, 11):
    print(f"{algarismo} x {i} = {tabuada(algarismo, i)}")    
    
 