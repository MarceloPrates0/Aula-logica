import os
os.system("cls || clear")
soma = 0
for i in range(1, 5):
    numero = int(input("Insira sua nota: "))
    soma += numero
    
media = soma / i

print(f"Sua média é {media}")
    