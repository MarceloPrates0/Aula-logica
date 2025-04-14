import os
os.system("cls || clear")

pares_impares = []

def ParOuImpar(algarismo):
    if algarismo % 2 == 0:
        print(f"{algarismo} é par")
    else:
        print(f"{algarismo} é impar")
        
def ParOuImpar(algarismo):
    if algarismo % 2 == 0:
        print(f"{algarismo} é par")
    else:
        print(f"{algarismo} é impar")
        

for i in range(1, 7):
    numero = float(input("Insira um numero: "))
    pares_impares.append(numero)

print()
for i, numero in enumerate(pares_impares, start=1):
    print(f"{i}ª número: {numero}")

print()
for numero in pares_impares:
    ParOuImpar(numero)    