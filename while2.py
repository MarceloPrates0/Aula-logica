import os
os.system ("clear")

idade = int(input("Insira sua idade: "))

while idade <18:
    print("Somente maiores de 18 anos.")
    idade = int(input("Insira sua idade: "))

print("\nFIM")
