import os
os.system ("cls || clear")

print("===Cálculo de média===")

valor_nota = 0
for i in range(3):
    nota = float(input("Insira sua nota: "))
    while nota < 0 or nota > 10:
        nota = float(input("Valor inválido, insira sua nota novamente: "))
    valor_nota += nota

media = valor_nota / 3
print(f"Sua média: {media:.2f}")

# 7 - aprovado
# 5 a 6,9 - recuperação 
# 4,9 - reprovado
if media < 5:
    print("Reprovado.")
elif media < 7:
    print("Recuperação.")
else:
    print("Aprovado.")

    


 