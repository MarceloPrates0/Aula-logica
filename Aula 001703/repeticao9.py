import os
os.system("cls || clear")

soma = 0
for i in range(1, 4):
    nota = float(input("Insira sua nota: "))
    soma += nota
    
media = soma / i
print(f"\nSua média foi {media:.2f}.")
if media < 4:
    print("REPROVADO!")
else:
    print("APROVADO!")
    